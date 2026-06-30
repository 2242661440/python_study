#创建列表
list1 = list("hello")
list2 = [1,2,3,4,5]

print(list1,"\n",list2)
# 去掉第二行的空格 对齐
print(f"{list1}\n{list2}")

# 列表扩展
# 往列表里追加一个元素
list1.append("word")
print(list1)

# 往列表里添加另一个列表所有元素
list3 = list("word")

# 使用+号扩展列表时，不会对原列表list1进行修改，会新建一个列表，性能相对低，更适合希望保留原列表时使用
list4 = list1 + list3

print(list4)
print(list1)

# 使用extend对列表扩展，会对原列表进行修改

list2.extend(list3)
print(list2)

# 往列表里面插入元素

print(f"list3列表里的元素为{list3}")
print("往列表list3的3号位置插入元素A")
list3.insert(3,"A")
print(f"插入元素后的列表list3为{list3}")

# 替换列表元素
print("把列表list3的3号位元素替换为5")
list3[3] = 5
print(f"替换后的列表list4为{list3}")

# 删除列表元素
# 根据元素值来删除
print("把列表list3的元素5删除")
list3.remove(5)
print(f"删除3号元素后的列表list3为{list3}")

# 根据元素的位置来删除
print(f"列表list3的元素为{list3}")
print("把列表list3的1号元素删除")
# 使用pop方法让元素从列表中弹出，弹出的元素会保留在内存中，可以被使用
list3.pop(1)

print(list3)

# 使用del方法直接删除元素，不会保留在内存中
print(f"列表list3的元素为{list3}")
print("把列表list3的2号元素删除")

del list3[2]
print(list3)