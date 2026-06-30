course1 = int(input("请输入课程1分数"))
course2 = int(input("请输入课程2分数"))
course3 = int(input("请输入课程3分数"))

integral1 = (course1>60 and course1 < 90) + (course1 > 90)*2
integral2 = (course2>60 and course2 < 90) + (course2 > 90)*2
integral3 = (course3>60 and course3 < 90) + (course3 > 90)*2

integral = integral1 + integral2 + integral3

print(integral1)
print(integral2)
print(integral3)
print(f"总课程积分为：{integral}")