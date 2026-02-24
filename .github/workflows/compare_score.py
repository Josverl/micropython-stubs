import json
import os

import requests
from dotenv import load_dotenv

try:

    load_dotenv()  # load variables 
    load_dotenv(".secrets")  # load variables from the ".secrets" file
except:
    pass

# Thresholds for pass_rate comparison
PASS_RATE_TOLERANCE = 0.05   # allow up to 5% drop in pass_rate before failing
# 50%: enough to detect mass-skip scenarios (e.g. all stubs unavailable) while allowing
# natural variation as the stable version set changes over time
MIN_EXECUTED_FRACTION = 0.50  # require at least 50% of baseline executed count

# has been propagated from repo vars to env vars
try:
    current_scores = json.loads(os.getenv("SNIPPET_SCORE", '{"snippet_score": 0}'))
except json.decoder.JSONDecodeError:
    current_scores = {"snippet_score": 0}

# set by pytest in custom conftest reporting
new_scores = {}
with open("results/snippet_score.json", "r") as f:
    new_scores = json.load(f)


# Compare the scores and update the repository variable if necessary
def add_summary(msg, current_scores: dict, new_scores: dict):
    if os.getenv("GITHUB_STEP_SUMMARY") is None:
        print(f"The environment variable GITHUB_STEP_SUMMARY does not exist.")
        return
    with open(os.getenv("GITHUB_STEP_SUMMARY", 0), "a") as f:
        f.write("# Snippets\n")
        f.write(msg)
        f.write("\n```json\n")
        json.dump({"current": new_scores}, f)
        f.write("\n")
        json.dump({"previous": current_scores}, f)
        f.write("\n```\n")



def update_var(var_name: str, value: str):
    repo = os.getenv("GITHUB_REPOSITORY", "Josverl/micropython-stubs")
    gh_token_vars = os.getenv("GH_TOKEN_VARS", os.getenv("GH_TOKEN", "-"))
    if gh_token_vars == "-":
        print("No token available to update the repository variable")
        return
    # update the repository variable
    url = f"https://api.github.com/repos/{repo}/actions/variables/{var_name}"
    headers = {
        "Authorization": f"token {gh_token_vars}",
        "Content-Type": "application/json",
        "User-Agent": "josverl",
    }
    data = {"name": str(var_name), "value": str(value)}
    response = requests.patch(url, headers=headers, json=data)
    response.raise_for_status()


# Compute new metrics - use pass_rate/executed when available, fall back to snippet_score
new_executed = new_scores.get("executed", new_scores.get("passed", 0) + new_scores.get("failed", 0))
current_executed = current_scores.get("executed", 0)
new_pass_rate = new_scores.get("pass_rate", None)
current_pass_rate = current_scores.get("pass_rate", None)

# Check minimum executed threshold (50% of baseline) - only when baseline has data
if current_executed > 0 and new_executed < current_executed * MIN_EXECUTED_FRACTION:
    msg = (
        f"Too few tests executed: {new_executed} is less than "
        f"{MIN_EXECUTED_FRACTION:.0%} of baseline ({current_executed}). "
        f"Possible mass-skip or environment issue."
    )
    print(msg)
    add_summary(msg, current_scores, new_scores)
    exit(1)

# Compare using pass_rate when both baseline and current have it
if new_pass_rate is not None and current_pass_rate is not None:
    rate_delta = new_pass_rate - current_pass_rate
    if new_pass_rate < current_pass_rate - PASS_RATE_TOLERANCE:
        msg = (
            f"pass_rate dropped by more than {PASS_RATE_TOLERANCE:.0%}: "
            f"{current_pass_rate:.2%} -> {new_pass_rate:.2%} "
            f"(executed: {new_executed})"
        )
        print(msg)
        add_summary(msg, current_scores, new_scores)
        exit(1)
    elif rate_delta >= 0:
        msg = f"pass_rate improved or unchanged: {current_pass_rate:.2%} -> {new_pass_rate:.2%} (executed: {new_executed})"
        print(msg)
        add_summary(msg, current_scores, new_scores)
        if os.getenv("GITHUB_REF_NAME", "main") == "main":
            update_var(var_name="SNIPPET_SCORE", value=json.dumps(new_scores, skipkeys=True, indent=4))
    else:
        msg = (
            f"pass_rate decreased within tolerance: "
            f"{current_pass_rate:.2%} -> {new_pass_rate:.2%} "
            f"(delta: {rate_delta:.2%}, executed: {new_executed})"
        )
        print(msg)
        add_summary(msg, current_scores, new_scores)
else:
    # Fall back to legacy snippet_score comparison
    if new_scores["snippet_score"] < current_scores["snippet_score"]:
        msg = f"The snippet_score has decreased from {current_scores['snippet_score']} to {new_scores['snippet_score']}"
        print(msg)
        add_summary(msg, current_scores, new_scores)
        exit(1)
    elif new_scores["snippet_score"] == current_scores["snippet_score"]:
        msg = f"The snippet_score has not changed from {current_scores['snippet_score']}"
        print(msg)
        add_summary(msg, current_scores, new_scores)
    elif new_scores["snippet_score"] > current_scores["snippet_score"]:
        msg = f"The snippet_score has improved to {new_scores['snippet_score']}"
        print(msg)
        add_summary(msg, current_scores, new_scores)
        if os.getenv("GITHUB_REF_NAME", "main") == "main":
            update_var(var_name="SNIPPET_SCORE", value=json.dumps(new_scores, skipkeys=True, indent=4))

print("Done")
exit(0)
