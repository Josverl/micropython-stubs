(micropico)=
# MicroPico Configuration [Pylance]

[MicroPico](https://github.com/paulober/MicroPico) is a Visual Studio Code extension designed to simplify and accelerate the development of MicroPython projects for the Raspberry Pi Pico and Pico W boards. This tool streamlines the coding process, providing code highlighting, auto-completion, code snippets, and project management features, all tailored for the seamless development experience with MicroPython on Raspberry Pi Pico and Pico W micro controllers.

The stubs used by MicroPico are the  Raspberry Pico W stubs from the micropython-stubs project.  
MicroPico automatically installs the stubs for you, and sets the configuration, so you don't have to worry about setting up the stubs manually.

Under the hood is used the [Pylance] extension to provide performant Python language support.
and most of the the settings for vscode and pylance are set up for you.

The default configuration is:

``` json
{
    "python.languageServer": "Pylance",
    "python.analysis.typeCheckingMode": "basic",
    "python.analysis.diagnosticSeverityOverrides": {
        "reportMissingModuleSource": "none"
    },
    "python.analysis.typeshedPaths": [
        "~/.micropico-stubs/included"
    ],
    "python.analysis.extraPaths": [
        "~/.micropico-stubs/included",

    ],
    // MicroPico settings
    "micropico.syncFolder": "",
    "micropico.openOnStart": true,
}

```

Things to note:
- The stubs are stored in the `~/.micropico-stubs/included` folder, which is a location shared by all your projects.
- The location of the stubs is set by `python.analysis.extraPaths` rather than `python.analysis.stubPath`.
- MicroPico keeps the stubs up to date for you, so you don't have to worry about updating them manually, unless you want to.

