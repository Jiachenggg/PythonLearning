"""
    函数的定义
    def 函数名（参数）:
        函数体
        return 返回值
"""


# None是类型NoneType的字面量，表示空的、无意义的
# None用于函数返回值
def say_hi():
    print("Hi!")
    return None  # 可以省略


say_hi()
result = say_hi()
print(f"无返回值函数，返回的内容是{result},返回的类型是{type(result)}")


# None应用于if判断
def check_age(age):
    if (age > 18):
        return "success"
    else:
        return None


result = check_age(16)
if not result:
    print("未成年")

# None用于声明无初始内容的变量
name = None


def add(x, y):
    """
    函数说明文档
    :param x:
    :param y:
    :return:
    """
    result = x + y
    print(f"{x}+{y}={result}")


add(13, 14)


def add(x, y):
    result = x + y
    return result  # 函数体遇到return结束，所以写在函数体内return后的语句不会执行


r = add(13, 14)
print(r)


def check_temp(temp):
    if temp <= 37:
        print(f"{temp}度，体温正常")
    else:
        print(f"{temp}度，体温异常")


check_temp(38.5)

# Python中允许函数的嵌套定义和嵌套调用

# 局部变量作用域在函数体内部，临时保存数据，当函数调用完成后，则销毁局部变量
# def fun():
#     num=100
#     print(num)
# fun()
# print(num)

# 全局变量是在函数体内、外都能生效的变量
# num=200
# def fun1():
#     print(num)
# def fun2():
#     print(num)
# fun1()
# fun2()
# print(num)


# num=200
# def fun1():
#     print(num)
# def fun2():
#     num=500
#     print(num)
# fun1()
# fun2()
# print(num)

# num=200
# def fun1():
#     print(num)
# def fun2():
#     global num# gloabl关键字在函数内声明变量为全局变量
#     num=500
#     print(num)
# fun1()
# fun2()
# print(num)

"""
    函数综合案例    
"""
money = 500000
name = None

name = input("请输入您的姓名：")

# 定义查询函数
def query(flag):
    if flag:
        print("--------查询----------")
    print(f"{name}，您好，您的账户余额{money}元")

# 定义存款函数
def saving(num):
    global money
    money += num
    print("---------存款-------------")
    print(f"{name}，您好，您存款{money}元成功")
    query(False)

# 定义取款函数
def withdraw(num):
    global money
    money -= num
    print("---------取款-------------")
    print(f"{name}，您好，您取款{money}元成功")
    query(False)

# 定义主菜单函数
def main():
    print("-----------主菜单----------------")
    print(f"{name}，您好，欢迎来到本银行，请选择您的操作：")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("请输入您的选择：")

# 设置无限循环，确保程序不退出
while True:
    keyboard_input = main()
    if keyboard_input == "1":
        query(True)
        continue
    elif keyboard_input == "2":
        num = int(input("请输入您要存多少钱："))
        saving(num)
        continue
    elif keyboard_input == "3":
        num = int(input("请输入您要取多少钱："))
        withdraw(num)
        continue
    else:
        print("程序退出")
        break
