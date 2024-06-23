"""
This module retrieves the versions of Micropython from the Micropython repository on GitHub.
It is used to generate a matrix of versions to create stubs for using Github Actions.

It provides a function `micropython_versions` that returns a list of versions starting from a specified version.
The module also includes a main block that generates a matrix of versions based on command-line arguments and environment variables.
The matrix is printed as JSON and can be optionally written to a file if running in a GitHub Actions workflow.
"""
import json
import os
import sys

from github import Github
from packaging.version import parse, Version


def micropython_versions(start="v1.10"):
    g = Github()
    try:
        repo = g.get_repo("micropython/micropython")
        # Suppress `v1.22.0-preview` tags
        tags = sorted([tag.name for tag in repo.get_tags() if "-preview" not in tag.name and parse(tag.name) >= parse(start)], reverse=True)
    except Exception as e:
        print(f"Error: {e}")
        tags = ["v1.19.1"]
    return tags

def major_minor(versions):
    """create a list of the most recent version for each major.minor"""
    mm_groups = {}
    for v in versions:
        major_minor = f"{Version(v).major}.{Version(v).minor}"
        if major_minor not in mm_groups:
            mm_groups[major_minor] = [v]
        else:
            mm_groups[major_minor].append(v)
    return [max(v) for v in mm_groups.values()]

def main():
    # only run latests when running in ACT locally for testing
    max_versions = 1 if os.environ.get("ACT") else 3

    matrix = {}
    matrix["version"] = major_minor(micropython_versions(start="v1.20"))[:max_versions] # last three

    if len(sys.argv) > 1 and (sys.argv[1].lower() in ["--latest", "-l"]):
        matrix["version"].insert(0, "latest")

    # GITHUB_OUTPUT is set by github actions
    if os.getenv('GITHUB_OUTPUT'):
        with open(os.getenv('GITHUB_OUTPUT'), 'a') as file:   #  type: ignore
            file.write(f"versions={json.dumps(matrix)}")
    else:
        print(json.dumps(matrix))

# sourcery skip: assign-if-exp, merge-dict-assign
if __name__ == "__main__":
    main()

