i = 0
a = 0
n = int(input("请输入相加次数"))
for _ in range(n):
    print(f"进行第{_}次计算")
    i = i + 1
    print(f"i:{i}")
    a = a + i
    print(f"结果为 {a}")

print(a)



i = 0

n = int(input("请输入相加次数"))
for a in range(1, n + 1):
    print(f"进行第{a}次计算")
    i = i + a
    print(i)

print(i)