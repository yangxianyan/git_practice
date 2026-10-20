import requests  #引入网络请求库

# 定义要请求的网址（这是Github提供的公开API，用来获取用户信息）
url = "http://api.github.com/users/yangxianyan"

print("正在连接Github 服务器获取数据...")

try:

	# 发送请求
	response = requests.get(url, timeout = 5)

	# 检查状态码是否为200（200代表成功）
	if response.status_code == 200:
		print("获取成功!")
		# 把服务器返回的JSON数据转换成Python的字典（dict）
		data = response.json()

		# 从字典里提取我们想要的信息
		print(f"用户名：{data['login']}")
		print(f"公开仓库数：{data['public_repos']}个")
		print(f"注册时间为：{data['created_at']}")

		# =========新增的保存文件的功能========
		with open("history.txt", "a", encoding = "utf-8") as f:
			f.write(f"用户名：{data['login']},公开仓库数：{data['public_repos']},注册时间：{data['created_at']}\n")
		print("√ 查询记录已成功追加保存到github_history.txt!")
	else:
		print(f"获取失败，状态码：{response.status_code}")

except requests.exceptions.RequestsException as e:
	print(f"网络出错了：{e}")
