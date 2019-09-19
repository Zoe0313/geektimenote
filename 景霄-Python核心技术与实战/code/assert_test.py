"""
assert 的检查是可以被关闭的，比如在运行 Python 程序时，加入-O这个选项就会让 assert的检查被关闭。
Python test.py -O
那么程序中所有的 assert 语句都会失效，常数__debug__便为 False；反之__debug__则为 True。

总的来说，assert 并不适用 run-time error的检查。
比如你试图打开一个文件，但文件不存在；
再或者是你试图从网上下载一个东西，但中途断网了了等等。
"""

def apply_discount(price, discount):
    updated_price = price * (1 - discount)
    assert 0 <= updated_price <= price, 'price should be greater or equal to 0 and less or equal to original price'
    return updated_price

print(apply_discount(100, 0.2))#80.0

#apply_discount(100, 2)
#AssertionError: price should be greater or equal to 0 and less or equal to original price

def calculate_average_price(total_sales, num_sales):
    assert num_sales > 0, 'number of sales should be greater than 0'
    return total_sales / num_sales

print(calculate_average_price(68932, 1089))#63.3

def func(input):
    assert isinstance(input, list), 'input must be type of list'
    # 下面的操作都是基于前提：input 必须是 list
    if len(input) == 1:
        print("list length = 1")
    elif len(input) == 2:
        print("list length = 1")

func([1,2])
func("string")
