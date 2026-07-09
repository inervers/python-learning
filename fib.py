def fib(n):
    """返回第n个斐波那契数"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


n = int(input("请输入n："))
result = fib(n)
print(f"第{n}个斐波那契数是：{result}")
