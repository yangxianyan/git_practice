import os
# 1. 指定你要操作的文件夹路径
folder_path = "batch_test"

# 2. 检查这个文件夹是否存在
if not os.path.exists(folder_path):
	print(f"找不到文件夹{folder_path}")
else:
	# 3.获取文件夹里面所有的文件名（返回一个列表）
	files = os.listdir(folder_path)

	# 4.遍历这些文件
	for i,filename in enumerate(files):
		# 过滤条件1：只处理.jpg结尾的文件
		if not filename.endswith(".jpg"):
			continue

		# 过滤条件2：如果已经改过名字了，就跳过，防止套娃
		if filename.startswith("holiday_"):
			continue

		# 拼接出完整的旧文件路径（比如：batch_test/img_1.jpg）
		old_file_path = os.path.join(folder_path, filename)

		# 生成新名字：比如"holiday_01_img_1.jpg"
		new_name = f"holiday_{i+1:02d}_{filename}"

		# 拼接出完整的新文件路径
		new_file_path = os.path.join(folder_path,new_name)

		# 5.真正执行重命名动作
		os.rename(old_file_path, new_file_path)
		print(f"改名成功：{filename} -> {new_name}")
