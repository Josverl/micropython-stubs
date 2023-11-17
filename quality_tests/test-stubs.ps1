# Activate the venv

./.venv/bin/activate.ps1

. ./snippets/update-stubs.ps1
# then run the test with a clear cache to use the latest stubs
pytest -m 'snippets' --cache-clear
