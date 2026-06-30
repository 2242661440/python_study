# 创建一个父类
class Animal:
    def __init__(self,name): # 父类构造函数
        self.name = name

    def speak(self):  # 创建父类方法
        return f"{self.name}在狗叫"
    
    def move(self):   # 创建父类方法
        return f"{self.name}在狂奔"


class Dog(Animal):
    def __init__(self, name, age, sex): # 子类的构造函数
        super().__init__(name)  # 调用父类构造函数
        self.age = age
        self.sex = sex

    def speak(self):
        print(super().speak())  # 调用父类的方法
    
    def move(self):  # 调用父类的方法并扩展
        parent_move = super().move()
        parent_speak = super().speak()
        print(f"{self.name}今年{self.age}岁，是一只{self.sex}狗狗, {parent_move}, {parent_speak}")
    

dog = Dog("小鸡毛", 68 , "雌性")
dog.speak()
dog.move()