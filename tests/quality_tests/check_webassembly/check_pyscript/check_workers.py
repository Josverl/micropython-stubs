from pyscript import create_named_worker, workers


async def check_workers():
    worker = await create_named_worker("worker.py", "micro-worker", type="mpy")
    print(worker)

    named_worker = await workers["micro-worker"]
    attribute_worker = await workers.micro_worker
    print(named_worker, attribute_worker)
