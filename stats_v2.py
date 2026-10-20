import datetime  #引入时间模块，用来获取当前时间

# ==========定义函数==========

def calculate_stats(numbers):
	"""计算并返回最大值、最小值和平均值"""
	max_val = max(numbers)
	min_val = min(numbers)
	avg_val = sum(numbers) / len(numbers)
	return max_val, min_val, avg_val

def save_to_file(count, max_val,min_val, avg_val):
	"""吧计算结果追加保存到history.txt文件中"""
	# 获取当前时间, 格式入：2026-10-20 10：30：00
	now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	# 拼接要保存的字符串
	record = f"[{now}]输入了{count}个数字，最大值为{max_val},最小值为{min_val},平均值为{avg_val:.2f}\n"
	# 用'a'追加模式打开文件写入
	with open("history.txt", 'a', encoding = "utf-8") as f:
		f.write(record)

def show_history():
	"""读取并打印历史记录"""
	try:
		with open("history.txt", 'r', encoding = "utf-8") as f:
			print("\n----历史记录----")
			print(f.read().strip())  # 读取全部内容并去掉多余的空行
			print("-----------------\n")
	except FileNotFoundError:
		print("\n暂无历史记录，这是我的第一次运行。\n")

# ==============主程序区=============
def main():
	show_history()  # 启动时先显示历史记录

	print("可连续输入数字，输入q则表示退出")
	numbers = []

	while True:
		user_input = input("请输入数字：")

		if user_input.lower() == "q" or user_input == "":
			break

		try:
			num = float(user_input)
			numbers.append(num)

		except ValueError:
			print("输入无效，请输入有效的数字！")
	if len(numbers) == 0:
		print("您没有输入任何数字。")
	else:
		# 调用函数计算
		max_val, min_val,avg_val = calculate_stats(numbers)
		print(f"一共输入了{len(numbers)}个数字")
		print(f"最大值是：{max_val},最小值是{min_val}")
		print(f"平均值是：{avg_val:.2f}")

		# 调用函数保存到文件
		save_to_file(len(numbers),max_val,min_val,avg_val)
		print("统计结果已经保存到history.txt!")

# 程序的入口：当前直接运行这个文件时，执行main()函数
if __name__ == "__main__":
	main()
