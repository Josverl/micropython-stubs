"""
This module retrieves the versions of Micropython from the Micropython repository on GitHub.
It is used to generate a matrix of versions to create stubs for using Github Actions.

It provides a function `micropython_versions` that returns a list of versions starting from a specified version.
The module also includes a main block that generates a matrix of versions based on command-line arguments and environment variables.
The matrix is printed as JSON and can be optionally written to a file if running in a GitHub Actions workflow.
"""
import argparse
import json
import os
import sys
from functools import lru_cache

from github import Auth, Github
from packaging.version import Version, parse

# Token with no permissions to avoid throttling
# https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api?apiVersion=2022-11-28#getting-a-higher-rate-limit
PAT_NO_ACCESS = (
    "github_pat" + "_11AAHPVFQ0qAkDnSUaMKSp" + "_ZkDl5NRRwBsUN6EYg9ahp1Dvj4FDDONnXVgimxC2EtpY7Q7BUKBoQ0Jq72X"
)
PAT = os.environ.get("GITHUB_TOKEN") or PAT_NO_ACCESS

@lru_cache()
def micropython_versions(start="v1.10"):
    g = Github(auth=Auth.Token(PAT))
    try:
        repo = g.get_repo("micropython/micropython")
        # Suppress `v1.22.0-preview` tags
        tags = sorted([tag.name for tag in repo.get_tags() if "-preview" not in tag.name and parse(tag.name) >= parse(start)], reverse=True)
    except Exception as e:
        print(f"Error: {e}")
        tags = ["stable"]
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
    matrix = {}
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--stable", "--latest","-s", action=argparse.BooleanOptionalAction,default=True, help="Add latest version")
    parser.add_argument("--preview", "-p", action=argparse.BooleanOptionalAction, default=False, help="Add preview version")
    parser.add_argument("--max", "-m", type=int, default=3, help="Maximum number of versions")

    args = parser.parse_args()

    # only run latests when running in ACT locally for testing
    if os.environ.get("ACT"):
        args.max = 1
    matrix["version"] = major_minor(micropython_versions(start="v1.20"))[1:args.max] 


    # print(args)
    if args.stable:
        matrix["version"].insert(0, "stable")
    if args.preview:
        matrix["version"].insert(0, "preview")
    matrix["version"]=matrix["version"][:args.max]
    # GITHUB_OUTPUT is set by github actions
    if os.getenv('GITHUB_OUTPUT'):
        with open(os.getenv('GITHUB_OUTPUT'), 'a') as file:   #  type: ignore
            file.write(f"versions={json.dumps(matrix)}\n")
            file.write(f'mp_versions={json.dumps(matrix["version"])}\n')
    else:
        print(json.dumps(matrix, indent=4))

# sourcery skip: assign-if-exp, merge-dict-assign
if __name__ == "__main__":
    main()

