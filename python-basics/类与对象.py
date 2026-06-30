# 创建一个类与对象
class Dog: #创建一个类
    # 定义类变量
    eye = 2
    foot = 4

    def __init__(self, name, age, true_age): # 构造方法__init__ self指代这个类本身 name和age为这个类的属性
        self.name = name # 这一行是用来定义属性name
        self.age = age   # 这一行是用来定义属性age
        self.__true_age = true_age  #定义一个私有变量

    # 创建一个get私有变量的方法
    @property
    def true_age(self):
        if self.__true_age < 0:
            raise ValueError("年龄应该为正数")
        return self.__true_age
    # 创建一个set私有变量的方法
    @true_age.setter
    def true_age(self, true_age):
        if true_age < 0:
            raise ValueError(f"年龄应该为正数的{true_age}")
        self.__true_age = true_age

    def run(self):   # 定义一个实例方法
        print(f"{self.name}在奔跑")

    def behavior(self, action):   # 定义一个实例方法
        print(f"{self.name}在{action}")
    # 定义类方法
    @classmethod
    def count(cls, dog_count):
        eye_count = dog_count * Dog.eye
        foot_count = dog_count * Dog.foot
        return print(f"{dog_count}只狗有{eye_count}只眼睛，{foot_count}只脚")

dog = Dog("小鸡毛", 8, 6) # 创建一个对象
print(f"这是我家的小狗，他叫{dog.name},今年{dog.age}岁")
print("这是我家小狗，他叫{0},今年{1}岁".format(dog.name,dog.age))
dog.run()  #调用实例方法
dog.behavior("吃屎")   #调用实例方法
dog.name = "林斯"  # 中途变卦修改实例属性
print(f"小鸡毛的真实年龄为{dog.true_age}岁") # 使用一个私有变量
dog.true_age = -6
dog.behavior("吃饭")   #调用实例方法
Dog.count(3)