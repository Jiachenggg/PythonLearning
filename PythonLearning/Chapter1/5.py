# 函数的多返回值
import time

def test_return():
    return 1, "Hello", True


x, y, z = test_return()
print(x, y, z)


def user_info(name, age, gender):
    print(f"姓名：{name} 年龄：{age} 性别：{gender}")


user_info('xchen', 23, '男')  # 位置参数
user_info(name='xchen', age=23, gender='男')  # 关键字参数
user_info(age=23, gender='男', name='xchen')  # 关键字参数可以不按照参数的定义顺序传参
user_info('xchen', gender='男', age=23)  # 函数调用时，如果有位置参数，位置参数必须在关键字参数前面，但关键字参数之间不存在先后顺序


def user_info(name, age, gender='男'):  # 缺省参数（默认参数）：当调用函数时没有传递参数，就会默认使用缺省参数对应的值。所有位置参数必须出现在默认参数之前
    print(f"姓名：{name} 年龄：{age} 性别：{gender}")


user_info('xchen', 23)
user_info('xhan', 24, gender='女')


# 不定长参数：不确定调用的时候会传递多少个参数

# 不定长参数--位置传递类型
def user_info(*args):  # 以元组的形式接收参数
    print(f"args参数类型：{type(args)} 内容:{args}")

user_info(1, 2, 3, 'xchen', '男', 666)


# 不定长参数--关键字传递类型
def user_info(**kwargs):  # 以字典的形式接收参数
    print(f"kwargs参数类型：{type(kwargs)} 内容:{kwargs}")

user_info(name='xchen', age=23, gender='男', tel=131)


# 函数作为参数传递到另一个函数中使用
def test_fun(compute):
    result = compute(1, 2)
    print(type(compute))
    print(result)

def compute(x, y):
    return x + y

test_fun(compute)


# def定义带有名称的函数；lambda定义匿名函数
# 有名称的函数，可以基于名称重复使用；无名称的匿名函数，只可临时使用一次
# lambda 传入参数:函数体(一行代码)：匿名函数的定义
def test_fun(compute):
    result = compute(1, 2)
    print(result)

test_fun(lambda x, y: x + y)  # 匿名函数用于临时构建一个函数，只用一次的场景

# open(name,mode,encoding) name:要打开的目标文件名的字符串，可以包含文件所在的具体路径；mode:打开文件的模式：r只读、w写入、a追加等；encoding:编码格式
"""
    mode访问模式：
        1 r-以只读方式打开文件。文件指针放在文件的开头（默认模式）
        2 w-打开一个文件用于写入。如果文件已存在，则打开文件从头开始编辑，并删除原有内容；如果该文件不存在，则创建新文件进行写入
        3 a-打开一个文件用于追加。如果文件已存在，新的内容被写入到已有内容之后；如果该文件不存在，创建新文件进行写入
"""
# 打开文件获取文件对象
f = open("D:/resource/PycharmProjects/PythonLearning/test_txt/test1.txt", "r", encoding="UTF-8")
print(type(f))

# 文件对象.read(num):num表示从文件中读取的数据长度，单位是字节。如果没有传入num，表示读取文件的所有数据
# print(f.read(5))
# print(f.read())

# 文件对象.readines():按照行的方式把整个文件中的内容进行一次性读取，并且返回一个列表，每一行的数据为一个元素
# lines=f.readlines()
# print(lines)
# print(type(lines))
# print("-----")

# 文件对象.readine():一次读取一行内容
# line1=f.readline()
# line2=f.readline()
# line3=f.readline()
# print(line1)
# print(line2)
# print(line3)
# print("-----")

# for循环读取文件行
# for line in f:# 每一个line临时变量，就记录了文件的一行数据
#     print(line)

# 文件的关闭
f.close()  # 如果不调用close,同时程序没有停止运行，那么这个文件将一直被Python程序占用

# 通过在with open语句块中对文件进行操作，可以在操作完成后自动关闭close文件，避免遗忘掉close方法
with open("D:/resource/PycharmProjects/PythonLearning/test_txt/test1.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(line)

# 读取文件案例
f = open("D:/resource/PycharmProjects/PythonLearning/test_txt/test2.txt", "r", encoding="UTF-8")
content = f.read()
count = content.count("xchen")
print(count)

# 直接调用write，内容并未真正写入文件，而是会存储在缓冲区，当调用flush的时候，内容会真正写入文件，这样做是避免频繁的操作硬盘
f = open("D:/resource/PycharmProjects/PythonLearning/test_txt/test3.txt", "w", encoding="UTF-8")
f.write("Hello!")
# 刷新内容到硬盘中
# f.flush()
# time.sleep(500000)
f.close()  # close()方法内置了flush()功能

f = open("D:/resource/PycharmProjects/PythonLearning/test_txt/test3.txt", "w", encoding="UTF-8")
f.write("World!")
f.close()

# f=open("D:/resource/PycharmProjects/PythonLearning/test_txt/test4.txt","a",encoding="UTF-8")
# f.write("Python")
# f.close()

f = open("D:/resource/PycharmProjects/PythonLearning/test_txt/test4.txt", "a", encoding="UTF-8")
f.write("Learning")
f.close()

"""
    演示文件操作综合案例：文件备份
"""
# fr = open("D:\\resource\\PycharmProjects\\PythonLearning\\bill.txt", "r", encoding="UTF-8")
# fw = open("D:\\resource\\PycharmProjects\\PythonLearning\\bill.txt.bak", "w", encoding="UTF-8")
#
# for line in fr:
#     line=line.strip()
#     if line.split(",")[4]=="测试":
#         continue
#     fw.write(line)
#     # 由于前面对内容进行了strip()的操作，所以要手动的写出换行符
#     fw.write("\n")
#
# fr.close()
# fw.close()


"""
    异常的捕获
    try:
        可能发生异常的语句
    except[异常 as 别名]:
        如果出现异常则执行的代码
    [else:]
        没有异常时要执行的代码
    [finally:]
        无论是否异常都要执行的代码
"""
# 基本的捕获
try:
    f = open("D:/resource/PycharmProjects/PythonLearning/test_txt/test5.txt", "r", encoding="UTF-8")
except:
    print("文件不存在！！！")
    f = open("D:/resource/PycharmProjects/PythonLearning/test_txt/test5.txt", "w", encoding="UTF-8")

# 捕获指定的异常
try:
    print(name)
except NameError as error1:
    print("变量未定义！！！")
    print(error1)

# 捕获多个异常
try:
    print(name)
    1 / 0
except:
    print("变量未定义！！！or除以0！！！")

# 捕获所有异常
try:
    # print("Hello")
    f = open("D:\\resource\\PycharmProjects\\PythonLearning\\test_txt\\test6.txt", "r", encoding="UTF-8")
except Exception as e:
    print("Error!!!")
else:  # else表示没有异常时要执行的代码
    print("No error")
finally:  # finally表示无论是否异常都要执行的代码
    print("有无异常都执行")
    f.close()


# 异常的传递性
def fun1():
    print("fun1开始执行")
    1 / 0
    print("fun1执行结束")

def fun2():
    print("fun2开始执行")
    fun1()
    print("fun2执行结束")

def main():
    try:
        fun2()
    except Exception as e:
        print(e)

main()

# 模块是一个Python代码文件，内含类、函数、变量，可以导入使用
# [from 模块] import [模块|类|变量|函数|*][as 别名]:模块的导入

# import time
# print("one")
# time.sleep(3)
# print("two")


# from time import sleep
# print("one")
# sleep(3)
# print("two")

# 使用*导入time模块的所有功能
# from time import *
# print("one")
# sleep(3)
# print("two")

# import time as t
# print("one")
# t.sleep(3)
# print("two")

# from time import sleep as s
# print("one")
# s(3)
# print("two")

# 自定义模块
# import my_module
# my_module.addition(1,1)

# from my_module import addition
# addition(1,1)

# 不同模块同名的功能如果都被导入，那么后导入的会覆盖先导入的

# from my_module import *
# addition(1,1)
# subtraction(1,1)


# 包可以包含许多Python模块，而每个模块又内含许多的功能。所以，我们可以认为：一个包，就是一堆同类型功能的集合体
# import my_package.my_module1
# import my_package.my_module2
# my_package.my_module1.test1()
# my_package.my_module2.test2()

# from my_package import my_module1
# from my_package import my_module2
# my_module1.test1()
# my_module2.test2()

# from my_package.my_module1 import test1
# from my_package.my_module2 import test2
# test1()
# test2()

# 通过all变量控制import *
# __all__针对的是 ’ from ... import * ‘ 这种方式对 ‘ import xxx ’ 这种方式无效
# from my_package import *
# my_module1.test1()
# my_module2.test2()
