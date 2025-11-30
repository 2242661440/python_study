a = "Lin"
b = input("请输入一个字母来确认它是否在单词之中")
if b in a:
    print(f"{b}在字母之中")
elif b not in a:
    print(f"{b}没有在字母之中")