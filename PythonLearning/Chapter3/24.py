"""
    多态：同一个行为，使用不同的对象获得不同的状态
"""

class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("Wolf")

class Cat(Animal):
    def speak(self):
        print("Miao")

def make_noise(animal: Animal):
    animal.speak()


dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)


# 抽象类：多用于做顶层设计，以便子类做具体实现
class AC:
    # 抽象方法：没有具体实现的方法(pass)
    def cool_wind(self):
        pass

    def hot_wind(self):
        pass

    def swing_l_r(self):
        pass


class Midea_AC(AC):
    def cool_wind(self):
        print("美的空调制冷")

    def hot_wind(self):
        print("美的空调制热")

    def swing_l_r(self):
        print("美的空调左右摆风")


class Gree_AC(AC):
    def cool_wind(self):
        print("格力空调制冷")

    def hot_wind(self):
        print("格力空调制热")

    def swing_l_r(self):
        print("格力空调左右摆风")


def make_cool(ac: AC):
    ac.cool_wind()


midea_ac = Midea_AC()
gree_ac = Gree_AC()

make_cool(midea_ac)
make_cool(gree_ac)
