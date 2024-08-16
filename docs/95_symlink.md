(create-symbolic-link)=

# Create a symbolic link

This section is only relevant if you are using a local copy of the stubs and want to create a symbolic link from your project to a `stubs` or a `publish` sub-folder for testing or development purposes.

To create the symbolic link to the `micropython-stubs/stubs` folder the instructions differ slightly for each OS/
The below examples assume that the micropython-stubs repo is cloned 'next-to' your project folder.
please adjust as needed.

## Windows 10 / 11

Windows 10 and later requires **Developer Mode** to create symlinks as a regular user, or you can run the below commands from an elevated PowerShell prompt ( Run as Admin) .

Settings > Developer Settings > Developer Mode : On

Please see [Activate Developer Mode](https://learn.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development) for instruction on how to activate this. Or read the [blogpost](https://blogs.windows.com/windowsdeveloper/2016/12/02/symlinks-windows-10/) on the rationale and see some examples.

You can create a symlink using PowerShell or with the mklink cmdline tool.
Both methods achieve exactly the same result.

### Powershell

```powershell
New-Item -ItemType SymbolicLink -Path "all-stubs" -Target (Resolve-Path -Path ../micropython-stubs/stubs)
```

```{note}
The target must be an absolute path.  
Therefore `Resolve-Path` is used to resolve the relative path to an absolute path.
```

### mklink

or use [mklink](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/mklink) in an (elevated) command prompt.

```
mklink /d all-stubs c:\develop\micropython-stubs\stubs
```

```{note}
The `mklink` target (last path) must be an absolute path
```

## Linux/Macos/Unix

```sh
# target must be an absolute path
ln -s /path/to/micropython-stubs/stubs all-stubs
```

```{note}
The target (first path) must be an absolute path
```
