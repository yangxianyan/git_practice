import re

html = "<h1>标题一</h1><p>内容</p><h1>标题二</h1>"

# 1.贪婪模式（默认）：*或者+会尽可能多地匹配字符
# 他会从第一个<h1>一直匹配到最后一个</h1>
greedy = re.findall(r"<h1>.*</h1>",html)
print("贪婪模式：", greedy)

# 2.非贪婪模式：在量词（*或+）后面加一个问号？
# 他会找到第一个满足条件的就立刻收手
non_greedy = re.findall(r"<h1>.*?</h1>",html)
print("非贪婪模式：", non_greedy)
