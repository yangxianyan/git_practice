names = []
print("请输入你想记录的名字，输入q结束：")
while True:
	name = input("请输入名字:")
	if name == "q":
		break
	names.append(name)
print("你一共输入了" + str(len(names)) + " 个名字。")
print("这些名字分别是")

for n in names:
	print("- " + n)
