# 给定两个序列，判定第一个是不是第二个的子序列。
# （LeetCode 链接如下：https://leetcode.com/problems/is-subsequence/ ）
# 先来解读一下这个问题本身：
# 序列就是列表，子序列则指的是，一个列表的元素在第二个列表中都按顺序出现，但是并不必挨在一起。
# 举个例子，[1, 3, 5] 是 [1, 2, 3, 4, 5] 的子序列，[1, 4, 3] 则不是。

def is_subsequence(a, b):
    b = iter(b)
    return all(i in b for i in a)

print(is_subsequence([1, 3, 5], [1, 2, 3, 4, 5]))
print(is_subsequence([1, 4, 3], [1, 2, 3, 4, 5]))

########## 输出 ##########
# True
# False
