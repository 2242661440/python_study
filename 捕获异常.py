# 创建一个简单的计算用代码块用来捕获异常
# i = int(input("请输入一个数字用来被8888除算:"))
# n = 8888

# try:
#     result = n / i
#     print(result)
#     print(f"{n}除以{i}等于{result}")

# except ZeroDivisionError as e:
#     print(f"不能除以0，异常为{e}")


# 创建一个让用户输入数字来计算的程序，如果用户输入0或者不是整数的话，输出错误信息，并让用户继续输入，直到成功为止

n = 8888
while True:
    try:
        i = int(input("请输入一个数字用来被8888除算:"))
        result = n / i
        print(result)
        print(f"{n}除以{i}等于{result}")
        break

    except ZeroDivisionError as e:
        print(f"不能除以0，异常为{e}")
    except ValueError as e:
        print(f"请输入正确的整数！错误：{e}")


# 更为规范的代码

n = 8888

while True:
    s = input("请输入一个数字用来被8888除算（输入 q 退出）: ").strip()
    if s.lower() in ("q", "quit", "exit"):
        print("已退出。")
        break

    # 先单独处理整数转换错误
    try:
        i = int(s)
    except ValueError:
        print("请输入正确的整数！请重新输入。")
        continue

    # 再单独处理除零错误
    try:
        result = n / i
    except ZeroDivisionError:
        print("不能除以0，请重新输入。")
        continue

    # 成功则输出并跳出循环
    print(f"{n}除以{i}等于{result}")
    break
