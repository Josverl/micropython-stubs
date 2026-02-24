#!/usr/bin/env python3
"""Enhanced snippet score comparison with multi-version support and history tracking.

Structure of SNIPPET_SCORE:
{
  "stable": {
    "v1.27.0": {
      "pass_rate": 0.95,
      "executed": 100,
      "passed": 95,
      "failed": 5,
      "timestamp": "2026-02-24T12:34:56Z",
      "commit": "abc123"
    }
  },
  "preview": {
    "pass_rate": 0.92,
    "executed": 100,
    "passed": 92,
    "failed": 8,
    "timestamp": "2026-02-24T12:34:56Z",
    "version": "v1.28.0-preview"
  },
  "recent_majors": {
    "pass_rate": 0.93,
    "executed": 300,
    "passed": 279,
    "failed": 21,
    "timestamp": "2026-02-24T12:34:56Z",
    "versions": ["v1.27.0", "v1.26.1", "v1.25.0"]
  },
  "history": {
    "v1.27.0": [
      {"pass_rate": 0.95, "executed": 100, "timestamp": "...", "commit": "..."},
      ...  # up to last 10 records
    ],
    "preview": [...],
    "recent_majors": [...]
  }
}
"""
import json
import os
import sys
from datetime import datetime, timezone
from typing import Optional

import requests
from dotenv import load_dotenv

try:
    load_dotenv()
    load_dotenv(".secrets")
except:
    pass

# Thresholds
PASS_RATE_TOLERANCE = 0.05  # 5% drop tolerance
MIN_EXECUTED_FRACTION = 0.50  # require 50% of baseline executed
MAX_HISTORY_RECORDS = 10  # keep last 10 records per version


def get_version_type() -> str:
    """Get version type from environment variable."""
    return os.getenv("VERSION_TYPE", "stable")  # stable, preview, or recent_majors


def get_current_version() -> Optional[str]:
    """Get the specific version being tested (for stable)."""
    return os.getenv("TEST_VERSION", None)


def load_baseline_scores() -> dict:
    """Load baseline scores from environment variable."""
    try:
        scores = json.loads(os.getenv("SNIPPET_SCORE", "{}"))
        if not scores or "stable" not in scores:
            # Migrate old format
            return {
                "stable": {},
                "preview": {},
                "recent_majors": {},
                "history": {}
            }
        return scores
    except json.decoder.JSONDecodeError:
        return {
            "stable": {},
            "preview": {},
            "recent_majors": {},
            "history": {}
        }


def load_new_scores() -> dict:
    """Load new test results."""
    with open("results/snippet_score.json", "r") as f:
        return json.load(f)


def add_summary(msg: str, version_type: str, new_scores: dict, baseline: dict):
    """Add summary to GitHub Actions step summary."""
    summary_file = os.getenv("GITHUB_STEP_SUMMARY")
    if not summary_file:
        print("GITHUB_STEP_SUMMARY not available")
        return
    
    with open(summary_file, "a") as f:
        f.write(f"# Snippet Test Results ({version_type})\n\n")
        f.write(f"{msg}\n\n")
        f.write("## New Results\n```json\n")
        json.dump(new_scores, f, indent=2)
        f.write("\n```\n\n")
        f.write("## Baseline\n```json\n")
        json.dump(baseline, f, indent=2)
        f.write("\n```\n")


def update_var(var_name: str, value: str):
    """Update GitHub repository variable."""
    repo = os.getenv("GITHUB_REPOSITORY", "Josverl/micropython-stubs")
    gh_token_vars = os.getenv("GH_TOKEN_VARS", os.getenv("GH_TOKEN", "-"))
    
    if gh_token_vars == "-":
        print("No token available to update repository variable")
        return False
    
    url = f"https://api.github.com/repos/{repo}/actions/variables/{var_name}"
    headers = {
        "Authorization": f"token {gh_token_vars}",
        "Content-Type": "application/json",
        "User-Agent": "josverl",
    }
    data = {"name": var_name, "value": value}
    
    try:
        response = requests.patch(url, headers=headers, json=data)
        response.raise_for_status()
        return True
    except Exception as e:
        print(f"Failed to update variable: {e}")
        return False


def add_to_history(all_scores: dict, version_type: str, version_key: str, new_scores: dict):
    """Add current results to history, keeping last MAX_HISTORY_RECORDS."""
    if "history" not in all_scores:
        all_scores["history"] = {}
    
    if version_key not in all_scores["history"]:
        all_scores["history"][version_key] = []
    
    history_entry = {
        "pass_rate": new_scores.get("pass_rate", 0),
        "executed": new_scores.get("executed", 0),
        "passed": new_scores.get("passed", 0),
        "failed": new_scores.get("failed", 0),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "commit": os.getenv("GITHUB_SHA", "unknown")[:7]
    }
    
    all_scores["history"][version_key].append(history_entry)
    # Keep only last MAX_HISTORY_RECORDS
    all_scores["history"][version_key] = all_scores["history"][version_key][-MAX_HISTORY_RECORDS:]


def compare_and_update(version_type: str, fail_on_drop: bool = False) -> int:
    """
    Compare new scores with baseline and update if appropriate.
    
    Args:
        version_type: "stable", "preview", or "recent_majors"
        fail_on_drop: If True, exit with error code 1 on quality drop
        
    Returns:
        0 for success, 1 for failure
    """
    all_scores = load_baseline_scores()
    new_scores = load_new_scores()
    
    # Add metadata
    new_scores["timestamp"] = datetime.now(timezone.utc).isoformat()
    new_scores["commit"] = os.getenv("GITHUB_SHA", "unknown")[:7]
    
    # Determine the key to store under
    if version_type == "stable":
        version = get_current_version()
        if not version:
            print("ERROR: TEST_VERSION not set for stable tests")
            return 1
        storage_key = version
        baseline = all_scores["stable"].get(version, {})
    elif version_type == "preview":
        storage_key = "preview"
        new_scores["version"] = get_current_version() or "unknown"
        baseline = all_scores.get("preview", {})
    elif version_type == "recent_majors":
        storage_key = "recent_majors"
        # Extract tested versions from new_scores if available
        baseline = all_scores.get("recent_majors", {})
    else:
        print(f"ERROR: Unknown version_type: {version_type}")
        return 1
    
    # Extract metrics
    new_executed = new_scores.get("executed", 0)
    baseline_executed = baseline.get("executed", 0)
    new_pass_rate = new_scores.get("pass_rate", 0)
    baseline_pass_rate = baseline.get("pass_rate", 0)
    
    # Check minimum executed threshold
    if baseline_executed > 0 and new_executed < baseline_executed * MIN_EXECUTED_FRACTION:
        msg = (
            f"⚠️ Too few tests executed: {new_executed} < "
            f"{MIN_EXECUTED_FRACTION:.0%} of baseline ({baseline_executed}). "
            f"Possible mass-skip or environment issue."
        )
        print(msg)
        add_summary(msg, version_type, new_scores, baseline)
        return 1 if fail_on_drop else 0
    
    # Compare pass rates
    rate_delta = new_pass_rate - baseline_pass_rate
    
    if baseline_pass_rate > 0 and new_pass_rate < baseline_pass_rate - PASS_RATE_TOLERANCE:
        msg = (
            f"❌ pass_rate dropped by more than {PASS_RATE_TOLERANCE:.0%}: "
            f"{baseline_pass_rate:.2%} → {new_pass_rate:.2%} "
            f"(Δ {rate_delta:.2%}, executed: {new_executed})"
        )
        print(msg)
        add_summary(msg, version_type, new_scores, baseline)
        return 1 if fail_on_drop else 0
    elif rate_delta >= 0 or baseline_pass_rate == 0:
        if baseline_pass_rate == 0:
            msg = f"✨ New baseline established: {new_pass_rate:.2%} (executed: {new_executed})"
        else:
            msg = f"✅ pass_rate: {baseline_pass_rate:.2%} → {new_pass_rate:.2%} (Δ {rate_delta:+.2%}, executed: {new_executed})"
        print(msg)
        add_summary(msg, version_type, new_scores, baseline)
        
        # Update scores
        all_scores[version_type][storage_key] = new_scores
        add_to_history(all_scores, version_type, storage_key, new_scores)
        
        # Only update on main branch
        if os.getenv("GITHUB_REF_NAME", "main") == "main":
            update_var("SNIPPET_SCORE", json.dumps(all_scores, indent=2))
        
        return 0
    else:
        msg = (
            f"⚠️ pass_rate decreased within tolerance: "
            f"{baseline_pass_rate:.2%} → {new_pass_rate:.2%} "
            f"(Δ {rate_delta:.2%}, executed: {new_executed})"
        )
        print(msg)
        add_summary(msg, version_type, new_scores, baseline)
        return 0


if __name__ == "__main__":
    version_type = get_version_type()
    fail_on_drop = (version_type == "stable")  # Only fail on stable drops
    
    print(f"Comparing {version_type} scores (fail_on_drop={fail_on_drop})")
    exit_code = compare_and_update(version_type, fail_on_drop)
    sys.exit(exit_code)
