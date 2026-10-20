import requests
from bs4 import BeautifulSoup

# 目标网址（这是一个专门用于测试爬虫的合法网站）
url = "http://quotes.toscrape.com/"

print("正在抓取网页内容...")
# 发送 GET 请求
response = requests.get(url)

# 检查状态码是否为 200（200 代表请求成功）
if response.status_code == 200:
    # 把返回的 HTML 文本交给 BeautifulSoup 解析
    soup = BeautifulSoup(response.text, "html.parser")

    # 找到所有的名言区块（观察网页源码，每句话都在一个 class 为 "quote" 的 div 里）
    quotes = soup.find_all("div", class_="quote")

    # 准备一个列表，用来收集整理好的数据
    data_to_save = []

    print("\n--- 正在解析数据 ---")
    for quote in quotes:
        # 提取名言文字 (在 span 标签，class 为 text 里面)
        text = quote.find("span", class_="text").text
        # 提取作者名字 (在 small 标签，class 为 author 里面)
        author = quote.find("small", class_="author").text

        # 打印前 20 个字符看看效果
        print(f"名言: {text[:20]}... 作者: {author}")

        # 整理成字符串，存入列表准备保存
        data_to_save.append(f"作者: {author} | 名言: {text}\n")

        # 我们只取前 5 条作为演示
        if len(data_to_save) >= 5:
            break

    # 将数据保存到本地文件（注意这里用的是 "w" 覆盖模式）
    with open("quotes.txt", "w", encoding="utf-8") as f:
        f.writelines(data_to_save)

    print("\n✅ 成功将前 5 条名言保存到 quotes.txt 文件中！")
else:
    print(f"网页请求失败！状态码: {response.status_code}")
