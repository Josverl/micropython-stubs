from pyscript.media import Device, list_devices


async def check_media():
    stream = await Device.request_stream(video=True)
    legacy_stream = await Device.load(video={"width": 1280})
    print(stream, legacy_stream)

    devices = await list_devices()
    for device in devices:
        print(device.id, device.group, device.kind, device.label)
        await device.get_stream()
