param(
    $path = "C:\develop\MyPython\micropython-stubs", #  ${{inputs.path}}
    $pattern = ".py"
)

Write-host "::group:: git diff --name-only:"
# include untracked files in diff
git add --intent-to-add .
$files = @(git diff --name-only $path | Where-Object{ $_.Contains($pattern)})
$count = $files.count

$changed = "changed=$(if ($count -eq 0){"false"}else{"true"})"
if ($GITHUB_OUTPUT){
    $changed | add-content $GITHUB_OUTPUT
    "count=$count" | add-content $GITHUB_OUTPUT
}
Write-host "Changed: $changed, count: $count"

if ($GITHUB_STEP_SUMMARY){
    # create a summary
    if ($count -gt 0) {
        '### detected new stubs :rocket:' | add-content $GITHUB_STEP_SUMMARY
        $files | ForEach-Object{ "- $_" | Add-Content $GITHUB_STEP_SUMMARY }
    }
}
write-host "::endgroup::"
