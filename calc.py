def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

try:
    num1 = float(input("请输入第一个数字："))
    op = input("请输入运算符（+ - * /）：")
    num2 = float(input("请输入第二个数字："))

    if op == "+":
        result = add(num1, num2)
    elif op == "-":
        result = sub(num1, num2)
    elif op == "*":
        result = mul(num1, num2)
    elif op == "/":
        result = div(num1, num2)
    else:
        print("不支持的运算符")
        result = None

    if result is not None:
        with open("result.txt", "a", encoding="utf-8") as f:
            f.write(f"{num1} {op} {num2} = {result}\n")
        print(f"结果：{result}")

except ValueError:
    print("请输入有效数字")
except ZeroDivisionError:
    print("除数不能为零")
