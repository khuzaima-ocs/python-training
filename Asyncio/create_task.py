import asyncio

async def fetch(id):
    print(f"Start of fetch with id : {id}")
    await asyncio.sleep(2)
    print(f"End of fetch with id : {id}")

async def main():
    print("Start of main")
    task1 = asyncio.create_task(fetch(1))
    task2 = asyncio.create_task(fetch(2))
    task3 = asyncio.create_task(fetch(3))

    # These will run concurrently
    await task1
    await task2 
    await task3

    print("End of main")

asyncio.run(main())