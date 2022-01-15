[CmdletBinding()]
param (
    $Path = "./results"
)
foreach ( $file in (Get-ChildItem $Path -Filter "pyright*.log" )) {
    Write-Host "fix : " $file.FullName
    (Get-Content $file) `
        -replace ' - (warning|error):', ': $1:' `
        -replace ' - (info):', ': information:' `
    | Out-File $file
}
