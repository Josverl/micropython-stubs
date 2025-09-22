#!/usr/bin/env python3
"""
Enhanced diff checker for micropython-stubs workflow.

This script checks for changes in the repository and determines if a commit should be made
based on whether there are non-JSON file changes. JSON files are included in commits
but don't trigger commits by themselves.
"""

import os
import subprocess
import sys
from pathlib import Path


def run_git_command(cmd):
    """Run a git command and return the output."""
    try:
        result = subprocess.run(
            cmd, 
            shell=True, 
            capture_output=True, 
            text=True, 
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running git command '{cmd}': {e}", file=sys.stderr)
        return ""


def get_changed_files():
    """Get list of changed files using git status --porcelain."""
    output = run_git_command("git status --porcelain")
    if not output:
        return []
    
    changed_files = []
    for line in output.split('\n'):
        if line.strip():
            # Extract filename from git status output (remove status indicators)
            filename = line[3:].strip()  # Skip the first 3 characters (status indicators and space)
            changed_files.append(filename)
    
    return changed_files


def categorize_files(files):
    """Categorize files into JSON and non-JSON files."""
    json_files = []
    non_json_files = []
    
    for file in files:
        if file.lower().endswith('.json'):
            json_files.append(file)
        else:
            non_json_files.append(file)
    
    return json_files, non_json_files


def set_github_output(key, value):
    """Set GitHub Actions output variable."""
    github_output = os.getenv('GITHUB_OUTPUT')
    if github_output:
        with open(github_output, 'a', encoding='utf-8') as f:
            f.write(f"{key}={value}\n")
    else:
        print(f"::set-output name={key}::{value}")


def set_github_summary(content):
    """Set GitHub Actions step summary."""
    github_step_summary = os.getenv('GITHUB_STEP_SUMMARY')
    if github_step_summary:
        with open(github_step_summary, 'a', encoding='utf-8') as f:
            f.write(f"{content}\n")


def main():
    """Main function to check for changes and determine commit behavior."""
    verbose = os.getenv('VERBOSE', 'false').lower() in ('true', '1', 'yes')
    
    if verbose:
        print("::group::Enhanced diff check")
        print(f"Current working directory: {os.getcwd()}")
    
    # Get all changed files
    changed_files = get_changed_files()
    total_count = len(changed_files)
    
    if total_count == 0:
        if verbose:
            print("No changes detected.")
        set_github_output("changed", "false")
        set_github_output("count", "0")
        set_github_output("json_count", "0")
        set_github_output("non_json_count", "0")
        if verbose:
            print("::endgroup::")
        return
    
    # Categorize files
    json_files, non_json_files = categorize_files(changed_files)
    json_count = len(json_files)
    non_json_count = len(non_json_files)
    
    # Decision logic: commit only if there are non-JSON file changes
    should_commit = non_json_count > 0
    
    # Set outputs
    set_github_output("changed", "true" if should_commit else "false")
    set_github_output("count", str(total_count))
    set_github_output("json_count", str(json_count))
    set_github_output("non_json_count", str(non_json_count))
    
    # Create summary
    if should_commit:
        summary_content = f"### Detected {total_count} changed files - Commit will proceed :rocket:\n"
        summary_content += f"- Non-JSON files: {non_json_count} (triggers commit)\n"
        summary_content += f"- JSON files: {json_count} (included in commit)\n\n"
        
        if non_json_files:
            summary_content += "**Non-JSON files changed:**\n"
            for file in non_json_files:
                summary_content += f"- {file}\n"
        
        if json_files:
            summary_content += "\n**JSON files changed (included in commit):**\n"
            for file in json_files:
                summary_content += f"- {file}\n"
        
        set_github_summary(summary_content)
        
        if verbose:
            print(f"### Commit will proceed - {non_json_count} non-JSON file(s) changed")
            print("Non-JSON files:")
            for file in non_json_files:
                print(f"  - {file}")
            if json_files:
                print("JSON files (included in commit):")
                for file in json_files:
                    print(f"  - {file}")
    
    else:
        summary_content = f"### Detected {total_count} changed files - No commit needed\n"
        summary_content += f"- Only JSON files changed: {json_count}\n"
        summary_content += "- Non-JSON files: 0 (commit not triggered)\n\n"
        summary_content += "**JSON files changed (commit skipped):**\n"
        for file in json_files:
            summary_content += f"- {file}\n"
        
        set_github_summary(summary_content)
        
        if verbose:
            print(f"### No commit needed - only {json_count} JSON file(s) changed")
            print("JSON files (no commit triggered):")
            for file in json_files:
                print(f"  - {file}")
    
    if verbose:
        print("::endgroup::")


if __name__ == "__main__":
    main()