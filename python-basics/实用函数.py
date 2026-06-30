# 过滤函数 filter(过滤规则函数，可迭代对象) 第一个参数一定是函数类型
def filter_condition(x):
    return x > 50

data1 = [75,85,60,30,20,45,90,73,51,13]
data2 = filter(filter_condition,data1)
print(type(data2))
print(list(data2))

# 变换函数 map(提供变换规则的函数，可迭代对象) 第一个参数一定是函数类型
def map_condition(x):
    return x * 2

data3 = (1,2,3,4,5)
data4 = map(map_condition,data3)
print(data3)
print(tuple(data4))

# lambda函数  定义匿名函数 用于一次性使用不需要反复调用的函数，lambda函数没有函数名
lambda_sample1 = filter(lambda num: num > 50, data1)
print(list(lambda_sample1))

lambda_sample2 = map(lambda num: num * 2, data3)
print(tuple(lambda_sample2))