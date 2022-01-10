LATEST = "Latest"


def clean_version(
    version: str,
    *,
    build: bool = False,
    patch: bool = False,
    commit: bool = False,
    drop_v: bool = False,
    flat: bool = False,
):
    "Clean up and transform the many flavours of versions"
    # 'v1.13.0-103-gb137d064e' --> 'v1.13-103'

    if version in ["", "-"]:
        return version
    nibbles = version.split("-")
    if not patch:
        if nibbles[0] >= "1.10.0" and nibbles[0].endswith(".0"):
            # remove the last ".0"
            nibbles[0] = nibbles[0][0:-2]
    if len(nibbles) == 1:
        version = nibbles[0]
    elif build and build != "dirty":
        if not commit:
            version = "-".join(nibbles[0:-1])
        else:
            version = "-".join(nibbles)
    else:
        version = "-".join((nibbles[0], LATEST))
    if flat:
        version = version.strip().replace(".", "_")
    if drop_v:
        version = version.lstrip("v")
    else:
        # prefix with `v` but not before latest
        if not version.startswith("v") and version.lower() != "latest":
            version = "v" + version
    return version


from typing import Union
import subprocess
import os
from typing import Union, List


def git_branch():
    "run a external (git) command in the repo's folder and deal with some of the errors"
    try:
        # cmd = "git rev-parse --abbrev-ref HEAD".split()
        cmd = "git show -s --pretty=%D".split()
        result = subprocess.run(cmd, capture_output=True, check=True)
    except subprocess.CalledProcessError as e:
        # add some logging for github actions
        print("Exception on process, rc=", e.returncode, "output=", e.output)
        if e.returncode == 128:
            pwd = os.system("pwd")
            print(f"current directory: {pwd}")
        return ""
    if result.stderr != b"":
        print(result.stderr.decode("utf-8"))
        raise Exception(result.stderr.decode("utf-8"))

    if result.returncode < 0:
        raise Exception(result.stderr.decode("utf-8"))
    output = result.stdout.decode().strip()
    # format : HEAD -> v_version, origin/v_version
    branch = output.split()[2].rstrip(",")
    if branch == "->":
        # happens in github action
        branch = "main"
    return branch
