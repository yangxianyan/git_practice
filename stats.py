# 操作说明
print("可连续输入数字，按 q 退出")

# 定义一个空列表
numbers = []

# 添加数字
while True:
    user_input = input("请输入数字：")
    
    # 1. 先拦截退出条件
    if user_input.lower() == "q":
        break
        
    # 2. 尝试把输入转成数字
    try:
        num = float(user_input)  # 用 float 支持小数
        numbers.append(num)      # 直接追加，不要赋值
    except ValueError:
        # 3. 如果转数字失败（比如输入了 abc），提示并继续循环
        print("输入无效，请输入有效的数字！")
        continue

# 4. 循环结束后，先判断有没有输入数据（防空报错）
if len(numbers) == 0:
    print("您没有输入任何数字。")
else:
    # 只有有数据时，才计算和输出
    print(f"一共输入了 {len(numbers)} 个数字")
    print(f"最大值是：{max(numbers)}，最小值是：{min(numbers)}")
    print(f"平均值是：{sum(numbers) / len(numbers):.2f}")
