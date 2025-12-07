class People():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


class Boyfrind(People):
    def __init__(self, name, age, sex="male"):
        super().__init__(name, age, sex)
        self.sex = sex

    def study(self, content):
        print(f"{self.name}正在学习{content}。")

    def play_game(self, game):
        if game == "影之诗":
            print("又打sb游戏和bb吵了一架")
        print(f"{game}这游戏真不错！")

    def sleep(self, time):
        if time >= 23:
            print("按时睡觉了")
            return
        print("今天累了早点睡")


bf1 = Boyfrind("小鸡毛", 7)
bf1.study("Python")
bf1.play_game("影之诗")
bf1.sleep(21)
