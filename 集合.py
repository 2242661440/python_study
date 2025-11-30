set1 = {1,2,3}
print(type(set1))

num1 = int(input("请输入班级1学生的人数"))
class1 = set()   # 创建空集合时，必须使用set函数，只使用{}的话，会创建成一个空的字典

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

# 修改集合
# 删除集合元素

print(class1)
stu_remove = input("请输入想要除名学生的名字")
class1.remove(stu_remove)
print(f"目前班级的学生名单如下：{class1}")