# 定义一个函数，读取待办事项
def show_tasks():
	try:
	# 尝试打开文件，如果文件不存在，就跳到except
		with open("todo.txt","r", encoding = "utf-8") as f:
			tasks = f.readlines()
			if not tasks:
				print("当前没有待办事项。")
			else:
				print("\n---待办事项---")
				for i in range(len(tasks)):
					#tasks[i].strip()是去掉每一行末尾的换行符
					print(str(i + 1) + ". " + tasks[i].strip())
				print("--------------------\n")
	except FileNotFoundError:
		print("当前没有待办事项（文件不存在）。")

# 定义一个函数，添加待办事项
def add_task():
	task = input("请输入待办事项：")
	# 'a' 代表append（追加模式）），在文件末尾添加内容
	with open("todo.txt", "a", encoding="utf-8") as f:
		f.write(task + "\n")
	print("添加成功！")

# 主程序：循环菜单
while True:
	print("1.查看待办事项")
	print("2.添加待办事项")
	print("3.退出")
	choice = input("请选择操作（1/2/3）:")

	if choice == "1":
		show_tasks()
	elif choice == "2":
		add_task()
	elif choice == "3":
		print("再见！")
		break
	else:
		print("无效输入，请重新选择。")
