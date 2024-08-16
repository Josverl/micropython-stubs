(pyright_advanced)=
(pylance_advanced)=
# Pylance/Pyright Advanced configuration

In some projects there may be a need to validate code against different ports of MicroPython, or against different versions of MicroPython or to mix and match MicroPython and CPython code.

To enable that in a single VSCode project two concepts are relevant:

1. Make use of a VSCode multi-root workspace
2. Create separate Pyright configuration files for different folders in the workspace

## Multi-Root workspace.

All VSCode project are already workspaces. A multi-root workspace is just one with an additional folder added to it.
The workspace folders can be sub-folders in the main project folder or completely different folders.

I usually create a root-folder, and then add sub-folders for each part of the project, and store the `.workspace` file in the top of the root folder. 
For more details see: https://code.visualstudio.com/docs/editor/multi-root-workspaces

## Pyright configuration files.

Pyright allows you to configure the behavior of the language server on a per folder basis.

The configuration can be stored in a variety of ways, but the easiest is to use a `pyrightconfig.json` or `pyproject.toml` file in the root of each of the workspace folders.
[Sample configuration files](https://github.com/microsoft/pyright/blob/main/docs/configuration.md#sample-config-file)

<!-- 
## example project structure and configuration.

TODO -->

[Pylance]: https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance
