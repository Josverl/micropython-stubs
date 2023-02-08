param(
    $pattern = ".py"
)

Write-host "::group:: git status"
# show current working directory
Write-Host "pwd: $(pwd)" -ForegroundColor Green

if ($env:ACT) {
    # running in github act simulator 
    $files = @("foo.py", "bar.py")
}
else {
    $files = @(git status --porcelain | Where-Object { $_.Contains($pattern) })
}
$count = $files.count

$changed = "changed=$(if ($count -eq 0){"false"}else{"true"})"
$changed >> $env:GITHUB_OUTPUT
"count=$count" >> $env:GITHUB_OUTPUT


# create a summary
if ($count -gt 0) {
    '### detected new stubs :rocket:' >> $env:GITHUB_STEP_SUMMARY
    $files | ForEach-Object { "- $_" >> $env:GITHUB_STEP_SUMMARY }
}

write-host "::endgroup::"
