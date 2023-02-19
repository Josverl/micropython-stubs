param(
    $pattern = ".py",
    $verbose = "true"
)
# take string and booleans as input
try {
    $verbose = [System.Convert]::ToBoolean($verbose) 
}
catch [FormatException] {
    $verbose = $false
}


Write-host "::group:: git status -verbose:$verbose"
# show current working directory
Write-Host "pwd: $(pwd)" -ForegroundColor Green


$files = @(git status --porcelain | Where-Object { $_.Contains($pattern) })
$count = $files.count

$changed = "changed=$(if ($count -eq 0){"false"}else{"true"})"
$changed >> $env:GITHUB_OUTPUT
"count=$count" >> $env:GITHUB_OUTPUT


# create a summary
if ($count -gt 0) {
    "### Detected $count new/changed stubs :rocket: :" >> $env:GITHUB_STEP_SUMMARY
    $files | ForEach-Object { "- $_" >> $env:GITHUB_STEP_SUMMARY }
    if ($verbose) {
        write-host "### detected $count new stubs:" 
        $files | ForEach-Object { write-host "- $_" }
    }
}
else {
    if ($verbose) {
        write-host '### no new stubs detected.'
    }
}

write-host "::endgroup::"
