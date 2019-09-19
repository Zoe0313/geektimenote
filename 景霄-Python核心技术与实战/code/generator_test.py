#用生成器的方法验证恒等式(1 + 2 + 3 + ... + n)^2 = 1^3 + 2^3 + 3^3 + ... + n^3的正确性

def generator(k):
    i = 1
    while True:
        yield i ** k
        i += 1

gen_1 = generator(1)
gen_3 = generator(3)
print(gen_1)
print(gen_3)

def get_sum(n):
    sum_1, sum_3 = 0, 0
    for i in range(n):
        next_1 = next(gen_1)
        next_3 = next(gen_3)
        print('next_1 = {}, next_3 = {}'.format(next_1, next_3))
        sum_1 += next_1
        sum_3 += next_3
    print(sum_1 * sum_1, sum_3)

get_sum(8)

########## 输出 ##########

# <generator object generator at 0x000001E70651C4F8>
# <generator object generator at 0x000001E70651C390>
# next_1 = 1, next_3 = 1
# next_1 = 2, next_3 = 8
# next_1 = 3, next_3 = 27
# next_1 = 4, next_3 = 64
# next_1 = 5, next_3 = 125
# next_1 = 6, next_3 = 216
# next_1 = 7, next_3 = 343
# next_1 = 8, next_3 = 512
# 1296 1296
