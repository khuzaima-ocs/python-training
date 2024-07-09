import asyncio

async def fetch(id):
    print(f"Start of fetch with id : {id}")
    await asyncio.sleep(2)
    print(f"End of fetch with id : {id}")

async def main():
    print("Start of main")
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for i in range(3):
            task = tg.create_task(fetch(i))
            tasks.append(task)

    print("End of main")

asyncio.run(main())