# Stub Locations

## Using / mixing different ports or boards

You should be aware that the stubs for different boards and ports are all installed into the same location.

So if you attempt to install or uninstall different stub-packages or versions into a folder or environment, then the result may be not what you expect, as it is essentially a "last writer wins" scenario, and it is likely there will be some stubs left, or missing.

This is one of the reasons I prefer to use a `typings` folder as that give good clarity on what is included, and what not, as it is simple to remove the folder and start over without affecting your Python environment..


### Typings folder

If you install into a typing folder, the resulting folder structure is:

```
.
└── typings
    ├── micropython_rp2_pico_w_stubs-1.20.0.post5.dist-info
    ├── micropython_stdlib_stubs-1.1.2.dist-info
    ├── stdlib
    │   ├── asyncio
    │   ├── collections
    │   ├── os
    │   ├── sys
    │   └── _typeshed
    └── uasyncio
```

### Virtual Environment

When you install into an virtual environment the stubs will be stored in `site-packages`

```
.venv/lib/python3.12/site-packages/
├── micropython_rp2_pico_w_stubs-1.20.0.post5.dist-info
├── micropython_stdlib_stubs-1.1.2.dist-info
├── pip
│   ├── ...
├── pip-24.0.dist-info
├── stdlib
│   ├── asyncio
│   ├── collections
│   ├── os
│   ├── sys
│   └── _typeshed
└── uasyncio
```
<!-- 
TODO: ADD MicroPico stub locations

 -->