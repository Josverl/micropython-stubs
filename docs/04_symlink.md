(create-symbolic-link)=
# Create a symbolic link
To create the symbolic link to the `micropython-stubs/stubs` folder the instructions differ slightly for each OS/
The below examples assume that the micropython-stubs repo is cloned 'next-to' your project folder.
please adjust as needed.

```{mermaid}
graph LR

    MS[Micropython-Stubs] --- S[Stubs]
    P1[Project-1] --- AS1[/All-Stubs/]
    P1 --- S1[Src]
    P1 --- T1[Tests]

    P2[Project-2] --> AS2[/All-Stubs/]
    P2 --- S2[Src]
    P2 --- T2[Tests]

    AS1 -.->S
    AS2 -.->S
```

## Windows 10 / 11
Windows 10 and later requires **Developer Mode** to create symlinks as a regular user, or you can run the below commands from an elevated PowerShell prompt ( Run as Admin) .

Settings > Developer Settings > Developer Mode : On

Please see [Activate Developer Mode](https://docs.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development) for instruction on how to activate this. Or read the [blogpost](https://blogs.windows.com/windowsdeveloper/2016/12/02/symlinks-windows-10/) on the rationale and see some examples.

You can create a symlink using PowerShell or with the mklink cmdline tool.
Both methods achieve exactly the same result.
### Powershell 
``` powershell
New-Item -ItemType SymbolicLink -Path "all-stubs" -Target (Resolve-Path -Path ../micropython-stubs/stubs)
```

```{note}
The target must be an absolute path.  
Therefore `Resolve-Path` is used to resolve the relative path to an absolute path.
```

### mklink
or use [mklink](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/mklink) in an (elevated) command prompt.

```
mklink /d all-stubs c:\develop\micropython-stubs\stubs
```

```{note}
The `mklink` target (last path) must be an absolute path
```

## Linux/Macos/Unix

``` sh
# target must be an absolute path
ln -s /path/to/micropython-stubs/stubs all-stubs
```

```{note}
Teh target must be an absolute path
```
