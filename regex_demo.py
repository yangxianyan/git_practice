import re # 导入python的正则模块

# 一段乱七八糟的文本
text = """
大家好，我是张三，我的电话号码是15345678910。
如果有问题，请发邮件到zhangsan@test.com。
另外，李四的电话19284746465 也可以联系到我。
我的备用邮箱是 lisi_2026@work.cn。
"""

print("===1. 电话号码===")
# 正则公式：1[3-9]\d{9}意思是：以1开头，第二位事故3-9，后面跟着9个数字
phone_pattern = r"1[3-9]\d{9}"
phones = re.findall(phone_pattern, text)
for p in phones:
	print(p)


print("===2.提取邮箱===")
# 正则公式：[a-zA-Z0-9_]+@[a-zA-Z0-9]+\.[a-zA-Z]+
# 意思是：一堆字母数字下划线+ @ + 一堆字母数字 + . + 一堆字母
email_pattern = r"[a-zA-Z0-9_]+@[a-zA-Z0-9]+\.[a-zA-Z]+"
emails = re.findall(email_pattern, text)
for e in emails:
	print(e)

print("===3.替换敏感词===")
# 把张三和李四替换成**
# re.sub(规则，替换成什么，原文本)
new_text = re.sub(r"张三|李四", "**", text)
print(new_text)
