# 创建一个类与对象
class Dog: #创建一个类
    def __init__(self,name,age): # 构造方法__init__ self指代这个类本身 name和age为这个类的属性
        self.name = name # 这一行是用来定义属性name
        self.age = age   # 这一行是用来定义属性age

    def run(self):   #定义一个实例方法
        print(f"{self.name}在奔跑")

    def behavior(self,action):   # 定义一个实例方法
        print(f"{self.name}在{action}")

dog = Dog("小鸡毛",8) # 创建一个对象
print(f"这是我家的小狗，他叫{dog.name},今年{dog.age}岁")
print("这是我家小狗，他叫{0},今年{1}岁".format(dog.name,dog.age))
dog.run()  #调用实例方法
dog.behavior("吃屎")   #调用实例方法
dog.name = "林斯"  # 中途变卦修改实例属性
dog.behavior("吃饭")   #调用实例方法