import asyncio

async def fetch(id):
    print(f"Start of fetch with id : {id}")
    await asyncio.sleep(2)
    print(f"End of fetch with id : {id}")

async def main():
    print("Start of main")
    task1 = fetch(1)
    task2 = fetch(2)

    await task1
    await task2 # This will start after completion of task 1

    print("End of main")

asyncio.run(main())