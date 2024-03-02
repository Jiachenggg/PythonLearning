bool1 = True
bool2 = False
print(f"{bool1}类型{type(bool1)}")
print(f"{bool2}类型{type(bool2)}")

num1 = 10
num2 = 12
print(f"10==12 {num1 == num2}")
print(f"10!=12 {num1 != num2}")

name1 = "cjc"
name2 = "hyj"
print(f"cjc==hyj {name1 == name2}")
print(f"cjc!=hyj {name1 != name2}")

# Python通过空格缩进决定语句之间的层次关系
# age=int(input("请输入您的年龄："))# input获取到的数据都是字符串类型，需转换成整型
# if age>=18:
#     print("已成年")# 注意4个空格缩进
# else:
#     print("未成年")
# print("游玩愉快!")


# height=int(input("请输入您的身高："))
# level=int(input("请输入您的等级："))
# date=int(input("请输入日期："))
# if height<120:# 条件的判断是互斥且有序的
#     print("免费")
# elif level>3:
#     print("免费")
# elif date==15:
#     print("免费游玩")
# else:
#     print("需买票")


# if int(input("请输入您的身高："))<120:
#     print("免费游玩")
# elif int(input("请输入您的等级："))>3:
#     print("免费游玩")
# elif int(input("请输入日期："))==15:
#     print("免费游玩")
# else:
#     print("需买票")

# if int(input("请输入您的身高："))>120:
#     if int(input("请输入您的等级："))>3:
#         print("免费游玩")
#     else:
#         print("需买票")
# else:
#     print("免费游玩")


# i=1
# sum=0
# while i<=100:
#     sum+=i
#     i+=1
# print(f"1-100累加和是{sum}")


"""
    猜数字
"""
# 获取1-100的随机数字
# import  random
# num=random.randint(1,100)
#
# count=0# 记录猜测次数
# flag =True
# while flag:
#     guess_num=int(input("请输入1-100数字："))
#     count+=1
#     if guess_num==num:
#         print("猜中了")
#         flag=False# 终止循环
#     else:
#         if guess_num>num:
#             print("猜大了")
#         else:
#             print("猜小了")
# print(f"猜测次数{count}次")


# print("Hello",end='')
# print("World",end='')
# print()# 换行
#
# print("Hello\tcjc")
# print("Welcome\tcjc")


"""
    while循环打印九九乘法表
"""
# i=1
# while i<=9:
#     j=1
#     while j<=i:
#         print(f"{j}*{i}={j*i}\t",end='')# 不要换行
#         j+=1
#     i+=1
#     print()


"""
    for 临时变量 in 待处理的数据集（序列类型）:
        循环满足条件时执行的代码
"""
# 序列类型指内容可以一个个取出的一种类型，包括字符串、列表、元组等
# while循环的循环条件是自定义的，自行控制循环条件；for循环是一种轮询机制，是对一批内容进行逐个处理
# for循环无法定义循环条件，只能从被处理的数据集中，依次取出内容进行处理
# Python的for循环无法构建无限循环，因为被处理的数据不可能无限大
# 临时变量在编程规范上作用域只限定在for循环内部，如果在for循环外部访问临时变量是可以访问到的，但在编程规范上不建议这么做。如需访问临时变量，可以预先在循环外定义它

# name="chenjiacheng"
# for x in name:
#     print(x)
#
# name="chenjiacheng and hanyujia"
# count=0
# for x in name:
#     if x=="a":
#         count+=1
# print(f"总共有{count}个a")


# range()语句：获取数字序列
# for x in range(10):
#     print(x)
#
# for x in range(5,10):
#     print(x)
#
# for x in range(5,10,2):
#     print(x)


"""
    for循环打印九九乘法表
"""
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}*{i}={j*i}\t",end='')
#     print()


"""
    循环案例
"""
# money=10000
# for i in range(1,21):
#     import random
#     score=random.randint(1,100)
#
#     if score<60:
#         print(f"员工{i}绩效{score}不满足,下一位")
#         continue
#     if money>=1000:
#         money-=1000
#         print(f"员工{i}绩效{score}合格，发放工资，账户余额{money}")
#     else:
#         print(f"当前余额{money}，余额不足")
#         break
