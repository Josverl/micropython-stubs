# pyscript.fs
from pyscript import fs


async def foo_2():
    await fs.mount("/local")
    await fs.sync("/local")
    await fs.unmount("/local")

    await fs.mount("/local", id="my-app")
    revoked: bool = await fs.revoke("/local", id="my-app")
    print(revoked)
