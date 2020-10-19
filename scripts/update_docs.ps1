

$docfile = "firmwares.md"


$header = @"
# Overview of firmware stubs 

| folder | sysname | version | release | machine | # stubs | stubber version 
|--------|---------|---------|---------|---------|---------|----------------

"@ 

$configs = Get-ChildItem modules.json -Recurse | Sort-Object -Property BaseName
# new file with header 
$_ = new-item -Path $docfile -Value $header -Force


foreach ($file in $configs) {
    $mods = Get-Content $file.FullName | convertfrom-json
    $path = $file.DirectoryName.replace($pwd.Path,'.')
    $path = $path.replace('\','/')
    
    if ([string]::IsNullOrEmpty($mods.firmware.version )) {
        # old format 
        $firmware = $mods[0]
        $stub_ver = $mods[1].stubber
        $mod_count = $mods.Count -2 
    } else {
        # new module format
        $firmware = $mods.firmware
        $stub_ver = $mods.stubber.version
        $mod_count = $mods.modules.Count 
        
    }

    $line = "| [{0}]({7})| {1} | {2} | {3} | {4} | {5} | {6}" -f `
        $file.Directory.BaseName, $firmware.sysname, `
        $firmware.version, $firmware.release, `
        $firmware.machine, $mod_count, $stub_ver, $path
    #write-host $line
    Add-Content -Value $line -Path $docfile
}


