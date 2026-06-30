'''
report_sheet = {"小明":{"语文":85,"数学":96,"英文":88},"小红":{"语文":72,"数学":80,"英文":91},"小亮":{"语文":83,"数学":69,"英文":75}}

stu = input("请输入学生名字：")
subject = input("请输入学科名字：")

grade = report_sheet[stu][subject]

print(f"{stu}的{subject}为{grade}")


total_grade = sum(report_sheet[stu].values())

print(f"{stu}的总分数为:{total_grade}")

'''

a = ("语文",80)
b = ("数学",95)
c = ("英文",60)

dict_grade = dict((a,b,c))
print(dict_grade)


# 用集合作为参数代入字典的时候，因为集合是无序的，所以每次代入的时候，键和值每次都会发生变化
print("用集合作为参数代入字典")
a = {"语文",80}
b = {"数学",95}
c = {"英文",60}


dict_grade = dict((a,b,c))
print(dict_grade)

# 用列表作为参数代入字典
print("用列表作为参数代入字典")
a = ["语文",80]
b = ["数学",95]
c = ["英文",60]


dict_grade = dict((a,b,c))
print(dict_grade)

# 用zip函数打包元组代入字典
print("用zip函数打包元组代入字典")
zip_grade = zip(["语文","数学","英文"],[80,95,60])
dict_grade = dict(zip_grade)
print(dict_grade)

# 定义一个空字典
print("定义一个空字典并查看类型")
dict_null = {}
print(type(dict_null))

# 删除字典zip_grade里的键：语文
print(f"被删除的科目成绩为{dict_grade.pop("语文")}")
print(dict_grade)

# 增加字典键值对
print("增加一项体育的分数")
dict_grade["体育"] = 59
print(dict_grade)

# 修改字典里的值
print("修改体育项目的分数")
dict_grade["体育"] = 75
print(dict_grade)

# 返回字典中所有键值对
for a in dict_grade:
    if dict_grade[a] > 60:
        print(f"您的{a}成绩及格了，是{dict_grade[a]}分。")
    else:
        print(f"您的{a}成绩不及格，是{dict_grade[a]}分，请尽快补考。")

for k,v in dict_grade.items():
    if v > 60:
        print(f"您的{k}成绩及格了，是{v}分。")
    else:
        print(f"您的{k}成绩不及格，是{v}分，请尽快补考。")


# 返回字典里的所有键
print(f"成绩单里所有科目为：{dict_grade.keys()}")
print(type(dict_grade.keys()))

# 返回字典里的所有值
print(f"成绩单里所有科目的分数为：{dict_grade.values()}")
print(type(dict_grade.values()))