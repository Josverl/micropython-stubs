#!/usr/bin/env pwsh

param(
    [string]$port = "auto",
    [string]$board = "auto",
    [string[]]$versions = @("latest","v1.21.0", "v1.20.0", "v1.19.1" )
)
# update the stubs (local ) do not push updates
foreach ($version in $versions) {
    stubber get-docstubs --version $version
    stubber get-frozen --version $version
    stubber merge --version $version --port $port --board $board
    stubber build --version $version --port $port --board $board
}

