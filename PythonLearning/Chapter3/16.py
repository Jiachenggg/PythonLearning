# 设计类
class Student:
    # 成员变量：类的属性
    name = None
    gender = None
    age = None
    nationality = None
    native_place = None

    # 成员方法：类的行为
    # 函数是定义在类外的，定义在类的内部称为方法
    # self出现在形参列表中，但是不占用参数位置
    def say_hi(self):
        # 只有通过self,成员方法才能访问类的成员变量
        print(f"Hello,我是{self.name}")


# 创建对象
stu1 = Student()
# 对象属性赋值
stu1.name = "陈嘉程"
stu1.gender = "男"
stu1.age = 23
stu1.nationality = "中国"
stu1.native_place = "山西省"
print(stu1.name, stu1.gender, stu1.age, stu1.nationality, stu1.native_place)

stu2 = Student()
stu2.name = "xhan"
stu2.say_hi()
