import time
import asyncio


# #方法一：效率低下，所有执行时间的总和
# def crawl_page(url):
#     print('crawling {}'.format(url))
#     sleep_time = int(url.split('_')[-1])
#     time.sleep(sleep_time)
#     print('OK {}'.format(url))
#
# def main(urls):
#     for url in urls:
#         crawl_page(url)
# #执行：
# start = time.perf_counter()
# main(['url_1', 'url_2', 'url_3', 'url_4'])
# end = time.perf_counter()
# print('方法一 took {} ms'.format((end - start) * 1000))
# #方法一 took 10010.2433 ms

# #方法二：和方法一一样耗时，因为await是同步调用，相当于用异步接口写了同步代码
# async def crawl_page(url):
#     print('crawling {}'.format(url))
#     sleep_time = int(url.split('_')[-1])
#     await asyncio.sleep(sleep_time)
#     print('OK {}'.format(url))
#
# async def main(urls):
#     for url in urls:
#         await crawl_page(url)
#
# #执行：
# start = time.perf_counter()
# asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
# end = time.perf_counter()
# print('方法二 took {} ms'.format((end - start) * 1000))
# #方法二 took 10011.996675 ms

#方法三：通过asyncio.create_task来创建任务，代码不会阻塞在任务这里，
# 然后调用await task等待所有任务都结束
# 结果运行总时长是运行时间最长的爬虫
async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))

async def main(urls):
    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
    # for task in tasks:
    #     await task
    #for循环还可以写成：
    await asyncio.gather(*tasks)

#执行：
start = time.perf_counter()
asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
end = time.perf_counter()
print('方法三 took {} ms'.format((end - start) * 1000))
#方法三 took 4003.2274880000004 ms

