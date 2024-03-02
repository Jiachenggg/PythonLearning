class Student:
    # 构造方法
    # 构造方法也是成员方法
    def __init__(self, name, age, tel):
        # 在构造方法中定义成员变量
        self.name = name
        self.age = age
        self.tel = tel
        print("Student类创建了一个类对象")


stu = Student("陈嘉程", 23, "131")
print(stu.name, stu.age, stu.tel)
