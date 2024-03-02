"""
    魔术方法：Python内置的类方法
"""

class Student:
    # 构造方法，用于创建类对象时初始化
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 用于实现类对象转字符串
    def __str__(self):
        return f"Student类对象,name:{self.name},age:{self.age}"

    # 用于两个类对象进行小于或大于比较
    def __lt__(self, other):
        return self.age < other.age

    # 用于两个类对象进行小于等于或大于等于比较
    def __le__(self, other):
        return self.age <= other.age

    # 用于两个类对象进行相等比较
    def __eq__(self, other):
        return self.age == other.age


stu = Student("陈嘉程", 23)
print(stu)
print(str(stu))

stu1=Student("xchen",23)
stu2=Student("xhan",24)
print(stu1<stu2)
print(stu1>stu2)

stu1=Student("xchen",23)
stu2=Student("xhan",23)
print(stu1<=stu2)
print(stu1>=stu2)

stu1 = Student("xchen", 23)
stu2 = Student("xhan", 23)
print(stu1 == stu2)
print(stu1 == stu2)
