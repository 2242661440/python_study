num1 = int(input("请输入班级1学生的人数"))
class1 = set()

for i in range(0,num1):
    stu = input("请输入学生的名字")
    class1.add(stu)

    print(f"班级1的学生是{class1}")

num2 = int(input("请输入班级2学生的人数"))
class2 = set()

for i in range(0,num2):
    stu = input("请输入学生的名字")
    class2.add(stu)

    print(f"班级2的学生是{class2}")

print(f"两个班级的同名学生名字为:{class1&class2}")
print(f"只在班级1中出现的同学名字:{class1-class2}")
print(f"两个班级所有同学的名字:{class1|class2}")