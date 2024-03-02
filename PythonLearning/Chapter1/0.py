print("Hello World")

# 字面量：被写在代码中的固定的值
print(318)
print(13.14)

# 单行注释
"""
    多行注释
"""

# 定义变量
money = 100
print("钱包：", money, "元")
money = money - 10
print("花费：10元", "剩余：", money, "元")

# type()语句：返回被查看数据的类型
# 使用print直接输出类型信息
print(type("陈嘉程"))
print(type(318))
print(type(13.14))
print("\n")

# 使用变量存储type()语句的结果
string_type = type("陈嘉程")
int_type = type(318)
float_type = type(13.14)
print(string_type)
print(int_type)
print(float_type)
print("\n")

# 使用type()语句查看变量中存储的数据类型信息
name = "陈嘉程"
name_type = type(name)
print(name_type)
print("\n")

# python中变量是没有类型的，但是变量存储的数据是有类型的
# 字符串变量表示存储了字符串而不是表示变量是字符串类型


# int(x)将x转换为一个整数
# float(x)将x转换为一个浮点数
# str(x)将x转换为一个字符串

# 将数字类型转换成字符串类型
num_str = str(10)
print(type(num_str), num_str)

float_str = str(13.14)
print(type(float_str), float_str)

# 将字符串类型转换为数字类型
str_num = int("10")
print(type(str_num), str_num)

str_float = float("13.14")
print(type(str_float), str_float)

# 任何类型都可以转换成字符串类型
# 如果字符串类型转换成数字类型，则字符串的内容必须都是数字


# 整数类型和浮点数类型的转换
int_float = float(10)
print(type(int_float), int_float)

float_int = int(13.14)
print(type(float_int), float_int)

# Python中的关键字：在Python文件命名和变量命名时不能使用
import keyword

print(keyword.kwlist)
# 标识符：变量、类、方法的名字--字母数字下划线组成；不能以数字开头；不能是关键字；严格区分大小写


# /除  //整除  %取余  **指数
print(9.5 / 2)
print(9 // 2)
print(9 % 2)
print(3 ** 2)

# 字符串的定义方式
name = '陈嘉程'
name = "陈嘉程"
name = """陈嘉程"""  # 三引号定义支持换行操作，使用变量接收就是字符串，不使用变量接收就作为多行注释使用

# 单引号内含双引号或双引号内含单引号
name = "'陈嘉程'"
print(name)
name = '"陈嘉程"'
print(name)
# 转义字符\' \"
name = "\'陈嘉程\'"
print(name)
name = '\"陈嘉程\"'
print(name)

# 使用+完成字面量和变量或变量和变量之间的拼接，只能适用字符串类型的拼接，无法和非字符串类型进行拼接
name = "陈嘉程"
university = "东北石油大学"
tel = 131
print("我是" + name + "学校" + university)

# 字符串的格式化1，占位符%，%s/%d/%f将内容转换成字符串/整型/浮点型，放入占位位置
# 通过占位的形式，完成字符串之间的拼接
name = "陈嘉程"
message = "姓名：%s" % name
print(message)
# 通过占位的形式，完成数字和字符串的拼接
id = 2023
tel = 131
score = 90.5
message = "姓名：%s 学号：%-11d 电话：%-11d 分数：%.2f" % (name, id, tel, score)
print(message)

# 字符串的格式化2：f"{占位}"快速格式化，不理会类型，不做精度控制
name = "陈嘉程"
university = "东北石油大学"
id = 2023
score = 90.5
print(f"姓名：{name} 学校：{university} 学号：{id} 分数：{score}")  # f:format

# 对表达式进行格式化
print("1*1=%d" % (1 * 1))
print(f"2*2={2 * 2}")

name = "传智播客"
stock_code = "001"
stock_price = 19.99
stock_factor = 1.2
growth_days = 7
final_stock_price = stock_price * stock_factor ** growth_days
print(f"公司：{name} 股票代码：{stock_code} 当前股价：{stock_price}")
print("每日增长系数：%.1f，经过%d天增长后，股价达到了%.2f" % (stock_factor, growth_days, final_stock_price))

# input()语句：无论键盘输入什么类型的数据，获得到的数据永远都是字符串类型
name = input("请输入姓名：")  # input("提示信息")
print("get it,%s" % name)
