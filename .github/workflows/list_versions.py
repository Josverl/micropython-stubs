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
from packaging.version import parse


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


def main():
    matrix = {}
    # only run latests when running in ACT locally for testing
    if os.environ.get("ACT"):
        matrix["version"] = micropython_versions(start="v1.20")[:1] # only latest
    else:
       matrix["version"] = micropython_versions(start="v1.20")[:3] # last three

    add_latest = False
    if len(sys.argv) > 1 and (sys.argv[1].lower() in ["--latest", "-l"]):
        # print("Adding latest")
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

