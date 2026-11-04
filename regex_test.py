import re

IPname = "https://www.google.com/search?q=python"

# 将google提取出来
pattern = r"www\.(\w+)\.com"  # 公式：找www.后面跟着一串字母，然后是.com

result = re.search(pattern, IPname)
if result:
	#group(1)拿到的就是括号里面的内容
	print("提取到的域名主体是：", result.group(1))
else:
	print("没有匹配到")
