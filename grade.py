# 让用户输入分数
scores = input("请输入您的分数：")

try:
	score = int(scores)
	if score < 0 or score > 100:
		print("分数无效，请输入0-100的分数")
	elif  90 <= score:
		print("优秀")
	elif 80 <= score:
		print("良好")
	elif 70 <= score:
		print("中等")
	elif 60 <= score:
		print("及格")
	else: 
		print("不及格")
except ValueError:
	print("请输入有效的数字")
