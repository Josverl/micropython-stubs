# https://just.systems

# Set shell for Windows OSs:
set windows-shell := ["pwsh.exe", "-NoLogo", "-Command"]
# use uv for [script] tasks:
set script-interpreter := ['uv', 'run', '--script']

default:
    @just --list

init:
    stubber clone
    git clone https://github.com/python/typeshed.git repos/typeshed

alias docs := docstubs
docstubs v="stable":
    stubber docstubs --version {{v}}

stdlib:
    python publish/micropython-stdlib-stubs/build.py

[script]
publish_stdlib:
    # /// script
    # requires-python = ">=3.9"
    # dependencies = ["keyring"]
    # ///
    import keyring
    import subprocess
    import sys
    print(f"Publishing micropython-stdlib-stubs to pypi")
    token = keyring.get_password("pypi", "uv_publish")
    if not token:
        sys.exit(f"No pypi token found in keyring")

    subprocess.run(
        ["uv", "publish", "--token", token, ],
        check=True,
        cwd="publish/micropython-stdlib-stubs",
    )


frozen v="stable":
    stubber frozen --version {{v}}

merge_all v="stable":
    stubber merge --port all --board all --version {{v}}
 
build_all v="stable":
    stubber build --port all --board all --version {{v}}

publish_all v="stable":
    stubber publish --port all --board all --version {{v}}

# build stubs for a specific port
port p="rp2" v="stable" b="all":
    stubber docstubs --version {{v}}
    stubber get-frozen --version {{v}}
    stubber merge --port {{p}} --board {{b}} --version {{v}}
    stubber build --port {{p}} --board {{b}} --version {{v}}

update_stubs v="stable":
    @just port all {{v}} all
    @just stdlib

# install all supported type-checkers and linters into the active venv (uv)
install-linters:
    uv pip install pyright mypy ruff basilisk-python

# run all snippet quality tests (pass extra pytest args, e.g. `just test --cache-clear`)
test *args="":
    pytest -m snippets {{args}}

# run snippet tests for the current stable release only
test-stable *args="":
    pytest -m snippets --stable-only {{args}}

# run snippet tests for the most recent preview build
test-preview *args="":
    pytest -m snippets --preview-only {{args}}

# run snippet tests for the last 3 stable major.minor releases
test-recent *args="":
    pytest -m snippets --recent-majors {{args}}

# run snippet tests for a single linter (pyright|mypy|ruff) on the stable release
test-linter linter="pyright" *args="":
    pytest -m snippets --stable-only -k "{{linter}}" {{args}}

# run snippet tests for a basilisk and show the xfail output (basilisk is experimental and may fail on some stubs)
test-basilisk *args="":
    pytest -m snippets --stable-only -k "basilisk"  --runxfail -rA {{args}}

# run snippet tests for a specific version (e.g. `just test-version v1.28.0`)
test-version version="v1.28.0" *args="":
    pytest -m snippets -k "{{version}}" {{args}}

release version commit :
    git tag {{version}} {{commit}}
    git push origin {{version}}
    gh release create {{version}} --title "MicroPython Stubs {{version}}" --draft --generate-notes