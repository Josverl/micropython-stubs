# test script for publish process
$versions = @("v1.19.1")
$versions = @("v1.18","v1.19","v1.19.1")

# stubber clone --no-stubs
foreach ($version in $versions){
    stubber switch --tag $version
    # stubber get-frozen
    # stubber get-docstubs
    # stubber merge --version $version
    # stubber publish --test-pypi --version $version
    stubber publish --pypi --version $version
}
# # run the build steps for this mpy version
