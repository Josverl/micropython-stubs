# pyscript.fs
from pyscript import fs

async def foo_2():
    await fs.mount("/local")
    await fs.sync("/local")
    await fs.unmount("/local")
