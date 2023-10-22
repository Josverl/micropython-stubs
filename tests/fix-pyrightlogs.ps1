[CmdletBinding()]
param (
    $Path = "./results"
)
foreach ( $file in (Get-ChildItem $Path -Filter "pyright*.log" )) {
    Write-Host "fix : " $file.FullName
    $content = (Get-Content $file) 
    # get the seperaters and labels fixed for testspace 
    $content = $content -replace ' - (error|warning|information):', ': $1:' `
        -replace ' - (info):', ': information:' 

    # Promote some errors to warnings 
    # $content = $content -replace 'warning: something (.*)', 'error: Something $1'  

    # Demote some warnings to info 
    $content = $content -replace ': warning: "None" is not iterable', ': information: "None" is not iterable' `
        -replace ': warning: "([\w|_]+)" is unknown import symbol', ': information: "$1" is unknown import symbol' `

    # Remove unwanted noise 
    $content = $content | Select-String -Pattern 'for type "None"' -NotMatch

    $content | Out-File $file
}