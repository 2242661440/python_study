# 函数也有数据类型，被称为函数类型
# 函数可以被另一个函数返回，也可以被另一个函数作为参数
def sum(*nums): # 定义一个相加用的函数
    sum1 = 0
    for num in nums:
        sum1 += num
    return sum1

def sub(*nums): # 定义一个相减用的函数
    sub1 = nums[0]
    for num in nums[1:]:
        sub1 -= num
    return sub1

def calc(mark): # 定义一个判断并且返回函数的函数
    if mark == "+":
        return sum
    if mark == "-":
        return sub
    
calc_sum = calc("+") #此时calc_sum为sum函数
calc_sub = calc("-") #此时calc_sub为sub函数

print(calc_sum(1,2))
print(calc_sub(1,2))