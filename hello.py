name=input("请输入您的名字")
age=input("请输入你的年龄")

#把年龄转成整数
age=int(float(age))

#输出欢迎语
print(f"你好，{name}!")

#判断是否成年
if age >= 18:
    print("你已经成年了。")
else:
    print("你还未成年。")
    