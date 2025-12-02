# 原始字符串 在字符串前加上字符串前缀r 让字符串中的转义符为原始字符串功能
# 下面的例子里\n没有换行的功能
print(r"你好\n你好")

# 长字符串  用三个引号或者三个双引号将有排版的文章括起，打印输出的时候可以保留原排版
print("""
静夜思
床前明月光，
疑是地上霜。
举头望明月，
低头思故乡。
        """)

# 字符串转换成数值
print(int("AB",16))  # 16为转换的进制参数 指将AB转换为16进制的数值

# 数值转换为字符串
a = (str(123))
print(f"123的类型为：{type(a)}")


# 字符串分割
str_split1 = "A B C D"
str_split2 = "A,B,C,D"
str_split3 = "A&B&C&D"
print(f"用空格来分割\"A B C D\"，得到一个列表{str_split1.split(" ")}")
print(f"用逗号来分割\"A,B,C,D\"，得到一个列表{str_split2.split(",")}")
print(f"用&来分割\"A&B&C&D\"，得到一个列表{str_split3.split("&")}")

# 定下分割的次数
print(f"用空格来分割\"A B C D\"，分割次数为1，得到一个有两个元素的列表{str_split1.split(" ",maxsplit=1)}")
print(f"用空格来分割\"A B C D\"，分割次数为2，得到一个有三个元素的列表{str_split1.split(" ",maxsplit=2)}")
print(f"用空格来分割\"A B C D\"，分割次数为0，得到一个有一个元素的列表{str_split1.split(" ",maxsplit=0)}")