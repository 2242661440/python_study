# 定义函数
def num_sum(num1,num2)->int:
    sum = num1 + num2
    return sum

# 调用函数
# 方法1 使用位置参数调佣函数 该方法实参会根据形参的位置来代入

sum1 = num_sum(1,2)
print(sum1)
print(type(sum1))

# 方法2 使用关键字参数调佣函数 该方法不用管形参的顺序
sum2 = num_sum(num2=1,num1=3)
print(sum2)

# 给函数参数默认值
def class_stu(stu1 = "Lin",stu2 = "Wang"):
    print(f"班级里有{stu1}同学和{stu2}同学")

# 调用函数时不提供实参
class_stu1 = class_stu()
# 也可以提供实参
class_stu2 = class_stu("林","王")