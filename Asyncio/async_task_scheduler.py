import asyncio as aio


async def foo(name: str, delay: int) -> None:
    if delay < -1:
        print("Delay cannot be in negative")
        return

    print(f"{name} started execution..")
    await aio.sleep(delay)
    print(f"{name} completed execution..")


async def main(tasks):
        tg_tasks = []
        async with aio.TaskGroup() as tg:
                for task in tasks:
                    tg_task = tg.create_task(foo(task["name"], task["delay"])) 
                    tg_tasks.append(tg_task)

no_of_tasks = int(input("How many tasks you want to create: "))
tasks = []

for i in range(no_of_tasks):
    name = input(f"Enter name of task {i + 1} : ")
    delay = int(input(f"Enter delay for task {i + 1} : "))
    tasks.append({"name": name, "delay": delay})

aio.run(main(tasks))