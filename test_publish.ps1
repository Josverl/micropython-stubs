# test script for publish process
$version = "v1.18"

stubber --version
stubber clone --no-stubs
stubber switch --tag $version
# run the build steps for this mpy version
stubber get-frozen
stubber get-docstubs
stubber merge --version $version
stubber publish --test-pypi --version $version
