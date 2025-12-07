# 创建一个父类
class Royal:
    def __init__(self, name):
        self.name = name

    def mode(self):
        print(f"{self.name}正在狗打牌")
        return (f"{self.name}正在狗打牌")

    def card(self):
        print(f"{self.name}使用了一张牛郎")
        return (f"{self.name}使用了一张牛郎")
# 再创建一个父类
class Witch:
    def __init__(self, name, game_result):
        self.name = name
        self.game_result= game_result

    def mode(self):
        print(f"{self.name}正在猪打牌")
        return (f"{self.name}正在猪打牌")

    def card(self):
        print(f"{self.name}使用了一张撒旦")
        return (f"{self.name}使用了一张撒旦")


class Gamer(Royal, Witch):
    def __init__(self, name, game_result, style):
        Royal.__init__(self, name)
        Witch.__init__(self, name, game_result)
        self.style = style

    def szb(self):
        if self.style == "Royal":
            mode = Royal.mode(self)
            card = Royal.card(self)
        else:
            mode = Witch.mode(self)
            card = Witch.card(self)
        print(f"{mode}, {card}, 然后{self.game_result}")


bb = Gamer("王桑","赢了", style = "Witch")
laosi = Gamer("四哥", "输了", style = "Royal")
bb.szb()
laosi.szb()
