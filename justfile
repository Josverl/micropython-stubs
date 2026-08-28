# https://just.systems

# Set shell for Windows OSs:
set windows-shell := ["pwsh.exe", "-NoLogo", "-Command"]
# use uv for [script] tasks:
set script-interpreter := ['uv', 'run', '--script']

default:
    @just --list

init:
    stubber clone

sync:
    uv sync --extra test 

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

# do all steps to build stubs for all ports and boards for a specific version (default: stable)
do-all v="stable":
    @just docstubs {{v}}
    @just stdlib
    @just frozen {{v}}
    @just merge-all {{v}}
    @just build-all {{v}}

frozen v="stable":
    stubber frozen --version {{v}}

merge-all v="stable":
    stubber merge --port all --board all --version {{v}}
 
build-all v="stable":
    stubber build --port all --board all --version {{v}}

publish-all v="stable":
    stubber publish --port all --board all --version {{v}}

# build stubs for a specific port
port p="rp2" v="stable" b="all":
    stubber docstubs --version {{v}}
    stubber get-frozen --version {{v}}
    stubber merge --port {{p}} --board {{b}} --version {{v}}
    stubber build --port {{p}} --board {{b}} --version {{v}}

update-stubs v="stable":
    @just port all {{v}} all
    @just stdlib

# install all supported type-checkers and linters into the active venv (uv)
install-linters:
    uv pip install pyright mypy ruff 
    # uv pip install basilisk-python

# clear the pytest cache
clear-cache:
    pytest -m snippets --cache-clear

fixup_pyscript v="1.29.0" f="1_29_0":
    stubber merge --version {{v}} --port webassembly
    # Now copy additional PyScript stubs for the webassembly-pyscript variant
    copy reference\pyscript\display.pyi stubs\micropython-v{{f}}-webassembly-pyscript-merged
    copy reference\pyscript\events.pyi stubs\micropython-v{{f}}-webassembly-pyscript-merged
    copy reference\pyscript\fetch.pyi stubs\micropython-v{{f}}-webassembly-pyscript-merged
    copy reference\pyscript\ffi.pyi stubs\micropython-v{{f}}-webassembly-pyscript-merged
    copy reference\pyscript\flatted.pyi stubs\micropython-v{{f}}-webassembly-pyscript-merged
    copy reference\pyscript\magic_js.pyi stubs\micropython-v{{f}}-webassembly-pyscript-merged
    copy reference\pyscript\media.pyi stubs\micropython-v{{f}}-webassembly-pyscript-merged
    copy reference\pyscript\polyscript.pyi stubs\micropython-v{{f}}-webassembly-pyscript-merged
    copy reference\pyscript\storage.pyi stubs\micropython-v{{f}}-webassembly-pyscript-merged
    copy reference\pyscript\util.pyi stubs\micropython-v{{f}}-webassembly-pyscript-merged
    copy reference\pyscript\web.pyi stubs\micropython-v{{f}}-webassembly-pyscript-merged
    copy reference\pyscript\websocket.pyi stubs\micropython-v{{f}}-webassembly-pyscript-merged
    copy reference\pyscript\workers.pyi stubs\micropython-v{{f}}-webassembly-pyscript-merged

    stubber build --version {{v}} --port webassembly

# run all snippet quality tests (pass extra pytest args, e.g. `just test --cache-clear`)
test *PARAMS:
    pytest -m snippets {{PARAMS}}

# run snippet tests for the current stable release only
test-stable *PARAMS:
    pytest -m snippets --stable-only {{PARAMS}}

# run snippet tests for the most recent preview build
test-preview *PARAMS:
    pytest -m snippets --preview-only {{PARAMS}}

# run snippet tests for the last 3 stable major.minor releases
test-recent *PARAMS:
    pytest -m snippets --recent-majors {{PARAMS}}

# run snippet tests for a single linter (pyright|mypy|ruff) on the stable release
test-linter linter="pyright" *PARAMS:
    pytest -m snippets --stable-only -k "{{linter}}" {{PARAMS}}

# run snippet tests for a basilisk and show the xfail output (basilisk is experimental and may fail on some stubs)
# test-basilisk *PARAMS:
#     pytest -m snippets --stable-only --no-cache -k "basilisk"  --runxfail -rA {{PARAMS}}

# run snippet tests for a specific version (e.g. `just test-version v1.28.0`)
test-version version="v1.28.0" *PARAMS:
    pytest -m snippets -k "{{version}}" {{PARAMS}}

release version commit :
    git tag {{version}} {{commit}}
    git push origin {{version}}
    gh release create {{version}} --title "MicroPython Stubs {{version}}" --draft --generate-notes