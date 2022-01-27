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

    # promote some errors to warnings 
    $content = $content -replace 'warning: Class declaration ', 'error: Class declaration ' 

    # #remove some noise 
    $content = $content | Select-String -Pattern 'for type "None"' -NotMatch

    $content | Out-File $file

}