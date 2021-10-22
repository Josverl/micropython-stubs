(create-symbolic-link)=
# Create a symbolic link
To create the symbolic link to the `micropython-stubs/stubs` folder the instructions differ slightly for each OS/
The below examples assume that the micropython-stubs repo is cloned 'next-to' your project folder.
please adjust as needed.

## Windows 10 
Requires `Developer enabled` or elevated powershell prompt.

``` powershell
# target must be an absolute path, resolve path is used to resolve the relative path to absolute
New-Item -ItemType SymbolicLink -Path "all-stubs" -Target (Resolve-Path -Path ../micropython-stubs/stubs)
```
or use [mklink](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/mklink) in an (elevated) command prompt
```
rem target must be an absolute path
mklink /d all-stubs c:\develop\micropython-stubs\stubs
```

## Linux/Macos/Unix

``` sh
# target must be an absolute path
ln -s /path/to/micropython-stubs/stubs all-stubs
```
