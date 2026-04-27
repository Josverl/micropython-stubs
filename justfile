# https://just.systems

# Set shell for Windows OSs:
set windows-shell := ["pwsh.exe", "-NoLogo", "-Command"]
# use uv
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
stdlib_publish:
    # /// script
    # requires-python = ">=3.9"
    # dependencies=["keyring"]
    # ///
    import keyring
    import subprocess
    # Get the token from the keyring
    pypi_token = keyring.get_password("pypi", "uv_publish")
    # TODO: now run "uv publish" using the retrieved tokens
    # subprocess.run(
    #     ["uv", "publish", "--repository", "pypi", "--token", pypi_token], 
    #     check=True, 
    #     cwd="publish/micropython-stdlib-stubs"
    #     )




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
    stubber merge --port {{p}} --board {{b}} --version {{v}}
    stubber build --port {{p}} --board {{b}} --version {{v}}
