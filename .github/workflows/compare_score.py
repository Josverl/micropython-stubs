import json
import os

import requests
from dotenv import load_dotenv

try:

    load_dotenv()  # load variables 
    load_dotenv(".secrets")  # load variables from the ".secrets" file
except:
    pass

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


if new_scores["snippet_score"] < current_scores["snippet_score"]:
    msg = f"The snippet_score has decreased from {current_scores['snippet_score']} to {new_scores['snippet_score']}"
    print(msg)
    add_summary(msg, current_scores, new_scores)
    exit(1)  # Fail the test
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
