"""
二分法搜索数组中最小的一个数x，可以满足x*x>target。
不存在则返回-1
"""

def comp(x, target):
    return x * x > target


def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    ret = -1
    while l <= r:
        m = (l + r) // 2
        if comp(arr[m], target):
            ret = m
            r = m - 1
        else:
            l = m + 1
    return ret


def solve(arr, target):
    id = binary_search(arr, target)

    if id != -1:
        return arr[id]
    return -1


print(solve([1, 2, 3, 4, 5, 6], 8))
print(solve([1, 2, 3, 4, 5, 6], 9))
print(solve([1, 2, 3, 4, 5, 6], 0))
print(solve([1, 2, 3, 4, 5, 6], 40))
