import asyncio

async def fetch(id):
    print(f"Start of fetch with id : {id}")
    await asyncio.sleep(2)
    print(f"End of fetch with id : {id}")

async def main():
    print("Start of main")
    results = await asyncio.gather(fetch(1),fetch(2),fetch(3))
    print("End of main")

asyncio.run(main())