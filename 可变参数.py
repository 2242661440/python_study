# 可变参数有两种，一种是基于元组的可变参数，用一个*号标记 def sum(*parameter) 一种是基于字典的可变参数，用两个*号标记def class(**student)
# 基于元组的可变参数例def sum(*parameter)
def sum(*parameter):
    total = 0
    for num in parameter:
        total += num
    print(type(parameter)) #*parameter为元组类型
    return total

# 调用函数，传入三个参数
print(sum(10,20,30))

# 基于字典的可变参数例def class(**student)
def class1(**student):
    print(f"class1班级的学生成绩为")
    for key, Value in student.items():
        print(key,Value)
    print(type(student)) #**student为元组类型


class1(小明 = 300, 小红 = 400, 小林 = 500)