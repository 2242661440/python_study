# 创建元组
a = (1,2,3) # 使用小括号创建元组
a1 = 1,2,3,4 # 不使用小括号
b = tuple("hello") # 使用tuple创建元组
c = 1, # 创建了只有一个元素的元组
d = () # 创建了一个空元组

list1 = [1,2]
e = tuple(list1) # 使用列表为参数创建元组

print(f"元组a为：{a}")
print(f"元组a1为：{a1}")
print(f"元组b为：{b}")
print(f"元组c为：{c}")
print(f"元组d为：{d}")
print(f"元组e为：{e}")

#元组拆包后赋值给其他变量

num,hanzi,zimu = (1,"林","lin")
print(num)
print(hanzi)
print(zimu)