# Windows Development Considerations

This document outlines common issues and considerations when developing MicroPython projects on Windows, particularly when using various shell environments and tools.

## MSYS2 / Git Bash Path Conversion Issues

### The Problem

When using MSYS2 or Git Bash on Windows, you may encounter issues with MicroPython tools like `mpremote` due to automatic path conversion. MSYS2 automatically converts Unix-style absolute paths to Windows paths when passing arguments to non-MSYS2 programs.

**Example of the issue:**
```bash
# This fails in Git Bash:
mpremote mkdir /ramdisk/lib

# Error output:
mkdir :C:/Program Files/Git/ramdisk/lib
mpremote: Error with transport:
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
OSError: [Errno 22] EINVAL
```

MSYS2 converts `/ramdisk/lib` to `C:/Program Files/Git/ramdisk/lib`, which is not the intended path on the MicroPython device.

### Root Cause

This is a feature of MSYS2 that automatically translates Unix-style paths to Windows paths when calling Windows executables. The conversion is documented in the [MSYS2 filesystem paths documentation](https://www.msys2.org/docs/filesystem-paths/#windows-unix-path-conversion).

### Workarounds

There are several ways to work around this issue:

#### 1. Use the `:` Prefix (Recommended)

Prefix absolute paths with `:` to prevent MSYS2 path conversion:

```bash
# This works correctly:
mpremote mkdir :/ramdisk/lib
mpremote cp main.py :/lib/main.py
```

#### 2. Set Environment Variable

Disable path conversion for specific patterns using the `MSYS2_ARG_CONV_EXCL` environment variable:

```bash
# Disable conversion for all paths starting with /
MSYS2_ARG_CONV_EXCL=/ mpremote mkdir /ramdisk/lib

# Or disable conversion entirely
MSYS2_ARG_CONV_EXCL='*' mpremote mkdir /ramdisk/lib
```

You can also set this permanently in your shell profile:

```bash
# In ~/.bashrc or ~/.bash_profile
export MSYS2_ARG_CONV_EXCL=/
```

#### 3. Use PowerShell or Command Prompt

This issue is specific to MSYS2/Git Bash. Using PowerShell or Command Prompt avoids the problem entirely:

```powershell
# Works correctly in PowerShell:
mpremote mkdir /ramdisk/lib
```

### Affected Tools

This issue affects any tool that expects Unix-style paths when run from MSYS2/Git Bash:

- `mpremote` (MicroPython remote control)
- `mip` (MicroPython package installer)
- Any custom scripts that use absolute paths

### Best Practices

1. **Use PowerShell for MicroPython development** - It provides better compatibility with Python tools and doesn't have path conversion issues.

2. **If using Git Bash/MSYS2**, always use the `:` prefix for absolute paths when working with MicroPython tools.

3. **Set environment variables** if you frequently use MSYS2 and prefer not to modify your commands.

4. **Be consistent** within your team about which shell environment to use to avoid confusion.

## Other Windows Considerations

### File Path Separators

While not usually an issue with modern Python tools, be aware that:

- Windows uses backslashes (`\`) as path separators
- Unix/Linux uses forward slashes (`/`) 
- Python generally accepts both, but some tools may be sensitive to the difference

### Line Endings

Different line ending styles can cause issues:

- Windows: CRLF (`\r\n`)
- Unix/Linux: LF (`\n`)

Configure your editor or Git to handle line endings consistently:

```bash
# Configure Git to handle line endings automatically
git config --global core.autocrlf true
```

### Case Sensitivity

Windows file systems are case-insensitive by default, while MicroPython file systems may be case-sensitive. Be consistent with file and module naming to avoid issues when deploying to devices.

## References

- [MSYS2 Path Conversion Documentation](https://www.msys2.org/docs/filesystem-paths/#windows-unix-path-conversion)
- [MicroPython micropython/micropython#17093](https://github.com/micropython/micropython/issues/17093) - Original issue report
- [mpremote documentation](https://docs.micropython.org/en/latest/reference/mpremote.html)