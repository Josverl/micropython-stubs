#!/usr/bin/env pwsh

<#
.SYNOPSIS
    This script updates the MicroPython stubs for a specified version, port, and board.

.DESCRIPTION
    The script accepts parameters for the port, board, version, and force flag. If no version is specified, it retrieves the latest version using a Python script. If no version is found, it falls back to using the "preview" and "stable" versions.

.PARAMETER port
    The port to update the stubs for. Defaults to "auto".

.PARAMETER board
    The board to update the stubs for. Defaults to "auto".

.PARAMETER version
    The version(s) of MicroPython to update the stubs for. Defaults to an empty array.

.PARAMETER force
    Forces the update of stubs for all versions, regardless of the specified version(s).

.NOTES
    This script requires Python 3 and the "stubber" package to be installed.

.EXAMPLE
    ./update-stubs.ps1 -port "esp32" -board "pyboard" -version "1.14"

    This example updates the stubs for MicroPython version 1.14, targeting the "esp32" port and "pyboard" board.

#>

param(
    [string]$port = "auto",
    [string]$board = "auto",
    [string[]]$version = @(),
    [switch]$force
)

if ($version.Count -eq 0) {
    # run the command and capture the output
    $info = Invoke-Expression "python3 ./.github/workflows/list_versions.py --latest" | ConvertFrom-Json
    $version = $info.version
}
if ($version.Count -eq 0) {
    # last resort
    $version = @("preview","stable")
}

# update the stubs (local ) do not push updates
foreach ($ver in $version) {
    if ($ver -eq "preview" -or $ver -eq "stable" -or $force ) {
        stubber get-docstubs --version $ver
        stubber get-frozen --version $ver
    }
    stubber merge --version $ver --port $port --board $board
    stubber build --version $ver --port $port --board $board
}
