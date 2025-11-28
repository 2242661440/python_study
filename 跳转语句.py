for i in range(10):
    if i == 8:
        break
    print(i)

for i in range(10):
    if i == 8:
        continue
    print(i)

# def num(a):
#     return f"当前循环数字为{a}"


# for i in range(10):
#     if i == 8:
#        print(num(i))

print("from here")
def func():
    for i in range(10):
        if i == 8:
            return "到此为止"
        print(i)
        
result = func()
print(result)
