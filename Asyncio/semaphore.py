import asyncio


async def fetch(id, semaphore):
    async with semaphore:
        print(f"Lock Acquired by id : {id}")
        await asyncio.sleep(2)

    print(f"Lock released by id : {id}") 

async def main():
    print("Start of main")
    semaphore = asyncio.Semaphore(2)
    await asyncio.gather(*(fetch(i, semaphore) for i in range(5)))

    print("End of main")

asyncio.run(main())