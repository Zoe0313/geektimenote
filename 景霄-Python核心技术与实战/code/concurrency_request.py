"""
python中的Futures模块，位于concurrent.futures和asyncio中，他们都表示带有延迟的操作。
Futures会将处于等待状态的操作包裹起来放到队列中，这些操作的状态可随时查询，他们的结果或是异常，
也能够在操作完成后被获取。

1. request.get 会触发：ConnectionError, TimeOut, HTTPError等，
所有显示抛出的异常都是继承requests.exceptions.RequestException
2. executor.map(download_one, urls) 会触发concurrent.futures.TimeoutError
3. result() 会触发Timeout，CancelledError
4. as_completed() 会触发TimeOutError
"""

import concurrent.futures
import requests
import threading
import time

def download_one(url):
    try:
        resp = requests.get(url)  # 该方法是线程安全的，因此在多线程环境下可以安全使用，不会出现race condition
        print('Read {} from {}'.format(len(resp.content), url))
    except requests.exceptions.ConnectionError:
        print('ConnectionError')
    except requests.exceptions.TimeOut:
        print('TimeOut')
    except requests.exceptions.HTTPError:
        print('HTTPError')
    except:
        print('requests Errors')

def download_all(sites):
    # 线程的数量并不是越多越好，线程的创建、维护和删除会带来一定的开销。
    # 我们往往根据实际需求来做一些测试，寻找最优的线程数量
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:#多线程并发
    #with concurrent.futures.ProcessPoolExecutor() as executor:#多进程并行
        #方法一：
        # try:
        #     executor.map(download_one, sites)#map函数表示对sites中的每一个元素并发的调用download_one
        # except concurrent.futures.TimeoutError:
        #     print('TimeoutError')

        #方法二：
        to_do = []
        for site in sites:
            future = executor.submit(download_one, site)
            to_do.append(future)
        try:
            for future in concurrent.futures.as_completed(to_do):
                future.result()
        except concurrent.futures.TimeoutError:
            print('TimeoutError')
        except concurrent.futures.Timeout:
            print('Timeout')
        except concurrent.futures.CancelledError:
            print('CancelledError')

def main():
    sites = [
        'https://en.wikipedia.org/wiki/Portal:Arts',
        'https://en.wikipedia.org/wiki/Portal:History',
        'https://en.wikipedia.org/wiki/Portal:Society',
        'https://en.wikipedia.org/wiki/Portal:Biography',
        'https://en.wikipedia.org/wiki/Portal:Mathematics',
        'https://en.wikipedia.org/wiki/Portal:Technology',
        'https://en.wikipedia.org/wiki/Portal:Geography',
        'https://en.wikipedia.org/wiki/Portal:Science',
        'https://en.wikipedia.org/wiki/Computer_science',
        'https://en.wikipedia.org/wiki/Python_(programming_language)',
        'https://en.wikipedia.org/wiki/Java_(programming_language)',
        'https://en.wikipedia.org/wiki/PHP',
        'https://en.wikipedia.org/wiki/Node.js',
        'https://en.wikipedia.org/wiki/The_C_Programming_Language',
        'https://en.wikipedia.org/wiki/Go_(programming_language)'
    ]
    start_time = time.perf_counter()
    download_all(sites)
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))

if __name__ == '__main__':
    main()
