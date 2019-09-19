import time
import concurrent.futures

def cpu_bound(number):
    print(sum(i * i for i in range(number)))

def calculate_sums(numbers):
    with concurrent.futures.ProcessPoolExecutor() as executor:#多进程并行
        try:
            executor.map(cpu_bound, numbers)
        except concurrent.futures.TimeoutError:
            print('TimeoutError')
        except:
            print('other Error')


def main():
    start_time = time.perf_counter()
    numbers = [10000000 + x for x in range(20)]
    calculate_sums(numbers)
    end_time = time.perf_counter()
    print('Calculation takes {} seconds'.format(end_time - start_time))


if __name__ == '__main__':
    main()
