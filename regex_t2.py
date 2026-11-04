import re

print("====1.分组抓取====")
text = "联系我：admin@qq.com"

# 用括号（）包围的内容，就是一个分组（Group）
pattern = r"(\w+)@(\w+\.\w+)"
match = re.search(pattern, text) # search只找第一个匹配的
if match:
	print("完整匹配：",match.group(0)) #整个字符串
	print("用户名：",match.group(1)) # 第一个括号里的内容
	print("域名：",match.group(2)) #第二个括号里的内容

print("====2.三大匹配函数对比====")
t2 = "Python是一门很棒的语言，Python爬虫真的好用。"

# 1. match:只从字符串的【开头】开始匹配，如果开头不是，直接返回None
print("match:", re.match("Python",t2))  #能匹配到

# 2.search：扫描整个字符串，找到【第一个】匹配就返回，后面的不管
print("search:", re.search("爬虫",t2)) # 能匹配到，因为它在返回

# 3.findall:扫描整个字符串，返回【所有】匹配的结果（列表）
print("findall:", re.findall("Python", t2))
