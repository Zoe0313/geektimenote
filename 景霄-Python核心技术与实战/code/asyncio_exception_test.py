import time
import asyncio

async def worker_1():
    await asyncio.sleep(1)
    return 1

async def worker_2():
    await asyncio.sleep(2)
    return 2 / 0

async def worker_3():
    await asyncio.sleep(3)
    return 3

async def main():
    task_1 = asyncio.create_task(worker_1())
    task_2 = asyncio.create_task(worker_2())
    task_3 = asyncio.create_task(worker_3())

    await asyncio.sleep(2)
    task_3.cancel()

    res = await asyncio.gather(task_1, task_2, task_3, return_exceptions=True)
    print(res)

#执行：
start = time.perf_counter()
asyncio.run(main())
end = time.perf_counter()
print('执行时间 took {} ms'.format((end - start) * 1000))
#[1, ZeroDivisionError('division by zero'), CancelledError()]
#执行时间 took 2003.537658 ms


#说明：
#return_exceptions=True这个参数若不设置，错误就会完整地throw到执行层，从而需要手动捕捉try except，
#一旦报错，这就意味着其他任务未执行就会被全部取消掉。为了避免这种局面，需要用到这个参数设定。








