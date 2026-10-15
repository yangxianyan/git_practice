# 定义一个加法函数
def add(a, b):
	return a + b

# 定义一个减法函数
def substract(a, b):
	return a - b
print("欢迎使用建议计算器")

num1 = int(input("请输入第一个数字："))
num2 = int(input("请输入第二个数字："))
operation = input("请输入运算符（+或者-）:")

if operation == "+":
	result = add(num1, num2)
elif operation == "-":
	result = substract(num1, num2)
else:
	print("不支持该运算符")
	result = None
if result is not None:
	print("计算结果是：" + str(result))
