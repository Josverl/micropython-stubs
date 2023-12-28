#!/usr/bin/env pwsh

param(
    [string]$port = "auto",
    [string]$board = "auto",
    [string[]]$versions = @("v1.21.0", "v1.20.0", "v1.19.1" ) # "latest",
)
# update the stubs (local ) do not push updates
foreach ($version in $versions) {
    stubber -build --version $version --port $port --board $board
    # stubber publish --build --version $version --port $port --board $board
}

