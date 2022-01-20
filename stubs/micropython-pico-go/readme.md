# About the Pico Go Stubs
This folder contains a copy of the MicroPython stubs for the Raspberry Pi Pico
Any of the stubs located in this folder are copied from the /frozen folder and are re-arranged for the target linter (Pylint or Pylance).

These stubs are not generated. They're hand-written and maintained by Chris Wood, with a little help from micropython-stubber.


The default configuration used by Pico-Go is : 

{
    "python.linting.enabled": true,
    "python.analysis.typeshedPaths": [
        ".vscode\\Pico-Stub"
    ],
    "python.languageServer": "Pylance",
    "python.analysis.typeCheckingMode": "basic",
    "python.analysis.extraPaths": [
        ".vscode\\Pico-Stub\\stubs"
    ]
}

Origin:  
https://github.com/cpwood/Pico-Stub#readme
