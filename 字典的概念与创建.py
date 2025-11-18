report_sheet = {"小明":{"语文":85,"数学":96,"英文":88},"小红":{"语文":72,"数学":80,"英文":91},"小亮":{"语文":83,"数学":69,"英文":75}}

stu = input("请输入学生名字：")
subject = input("请输入学科名字：")

grade = report_sheet[stu][subject]

print(f"{stu}的{subject}为{grade}")


total_grade = sum(report_sheet[stu].values())

print(f"{stu}的总分数为:{total_grade}")

