# Save current directory and change to script location
$savedDir = Get-Location
Set-Location $PSScriptRoot

# Run mpy-cross commands
mpy-cross typing.py -O3
mpy-cross typing_extensions.py -O3

dir *.mpy | ForEach-Object {  Write-Host "Compiled: $($_.Name) Size: $((Get-Item $_).Length) bytes" }

# Change back to the saved directory
Set-Location $savedDir
