



$header = @"
# Overview of firmware stubs 

| folder | sysname | version |  machine | # stubs | stubber version 
|--------|---------|---------|----------|---------|----------------

"@ 

$Workspace = split-path $PSScriptRoot -Parent

$configs = Get-ChildItem ( join-path $Workspace 'modules.json' )  -Recurse | Sort-Object -Property BaseName
# new file with header 
$docfile = join-path $Workspace "firmwares.md"
$_ = new-item -Path $docfile -Value $header -Force


foreach ($file in $configs) {
    # Write-Host( $file.Directory.Parent.BaseName)
    $mods = Get-Content $file.FullName | convertfrom-json
    $path = $file.DirectoryName.replace($pwd.Path, '.')
    $path = $path.replace('\', '/')
    $sysname = $firmware.machine

    # for frozen modules use the parent folder name (stm32, esp32, rp2) to identify the system
    # todo: update logic in generating the frozen manifest files
    if ($file.DirectoryName.Contains('-frozen')) {
        $sysname = $file.Directory.Parent.BaseName
    }
    if ([string]::IsNullOrEmpty($mods.firmware.version )) {
        # old format 
        $firmware = $mods[0]
        $stub_ver = $mods[1].stubber
        $mod_count = $mods.Count - 2 
    }
    else {
        # new module format
        $firmware = $mods.firmware
        $stub_ver = $mods.stubber.version
        $mod_count = $mods.modules.Count 
    }

    $line = "| [{0}]({6})| {1} | {2} | {3} | {4} | {5} " -f `
        $file.Directory.BaseName, $sysname, `
        $firmware.version, `
        $firmware.machine, $mod_count, $stub_ver, $path
    #write-host $line
    Add-Content -Value $line -Path $docfile
}


