# # 数据容器：一种可以容纳多份数据的数据类型，容纳的每一个元素可以使任意类型的数据
# # 数据容器根据特点的不同，如是否支持重复元素、是否可以修改、是否有序分为5类：列表(List)、元组(tuple)、字符串(str)、集合(set)、字典(dict)
#
# my_list=["chen","jia","cheng"]
# print(my_list)
# print(type(my_list))
#
# my_list=["chen",23,True]# 元素的数据类型没有限制
# print(my_list)
# print(type(my_list))
#
# my_list=[[1,2,3],[4,5,6]]# 定义一个嵌套列表
# print(my_list)
# print(type(my_list))
#
# my_list=["a","b","c"]
# # 从前往后从0开始递增
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
#
# # 从后往前从-1开始递减
# print(my_list[-1])
# print(my_list[-2])
# print(my_list[-3])
#
# my_list=[[1,2,3],[4,5,6]]
# print(my_list[1][2])

# 函数是一个封装的代码单元，可以提供特定功能
# 在Python中，如果将函数定义为class的成员，那么称之为方法
# 方法和函数的功能一样，有传入参数，有返回值，只是方法的使用格式不同
def add(x, y):
    return x + y


class Student:
    def add(self, x, y):  # self!
        return x + y


add(13, 14)
student = Student()
num = student.add(13, 14)

# 列表的特点：1.可以容纳多个元素 2.可以容纳不同数据类型的元素 3.数据是有序存储的 4.允许数据重复存在 5.可以修改数据

# 列表.index(元素)：查找指定元素在列表的下标
my_list = ["chen", "jia", "cheng"]
index = my_list.index("cheng")
print(index)

# 修改指定下标索引的值
my_list[0] = "陈"
print(my_list)

# 列表.insert(下标,元素)：在指定的下标位置插入指定的元素
my_list.insert(3, "better")
print(my_list)

# 列表.append(元素)，将单个指定元素追加到列表的尾部
my_list.append("666")
print(my_list)

# 列表.extend(容器)：将其它数据容器的内容取出，依次追加到列表尾部
my_list2 = [9, 9, 9]
my_list.extend(my_list2)
print(my_list)

# 删除指定下标的元素
# 方法1：del 列表[下标]
my_list = ["chen", "jia", "cheng"]
del my_list[0]
print(my_list)

# 方法2：列表.pop(下标)
my_list = ["chen", "jia", "cheng"]
element = my_list.pop(0)
print(f"{my_list}删除元素为{element}")

# 列表.remove(元素)：删除某元素在列表中的第一个匹配项
my_list = ["chen", "jia", "cheng", "chen", "jia", "cheng"]
my_list.remove("chen")
print(my_list)

# 列表.clear()：清空列表内容
my_list.clear()
print(my_list)

# 列表.count(元素)：统计某元素在列表内的数量
my_list = ["chen", "jia", "cheng", "chen", "jia", "cheng"]
count = my_list.count("chen")
print(f"chen的数量：{count}")

# len(列表)：统计列表中的元素数量
my_list = ["chen", "jia", "cheng", "chen", "jia", "cheng"]
count = len(my_list)
print(f"列表的元素数量：{count}")

"""
    1.while循环可以自定循环条件，并自行控制；for循环不可以自定循环条件，只可以从一个个容器内取出数据
    2.while循环可以通过条件控制做到无限循环；for循环理论上不可以，因为遍历的容器不是无限的
    3.while循环适用于任何想要循环的场景；for循环适用于遍历数据容器的场景或简单的固定次数循环场景
"""


def fun1():
    """
    使用while循环遍历列表
    :return:
    """
    my_list = [1, 2, 3, 4, 5]
    index = 0
    while index < len(my_list):
        element = my_list[index]
        print(element)
        index += 1

fun1()


def fun2():
    """
    使用for循环遍历列表
    :return:
    """
    my_list = [1, 2, 3, 4, 5]
    # for 临时变量 in 数据容器
    for element in my_list:
        print(element)

fun2()

# 元组同列表一样，都是可以封装多个不同类型的元素在内，但最大的不同点在于：元组一旦定义完成，就不可修改
# 列表的特点：1.可以容纳多个元素 2.可以容纳不同数据类型的元素 3.数据是有序存储的 4.允许数据重复存在 5.不可以修改数据
my_tuple = ("chen", 23, True)
# 定义空元组
tuple1 = ()
tuple2 = tuple()
print(my_tuple)
print(type(my_tuple))

# 元组只有一个元素时，这个元素后面要添加逗号，否则就不是元组类型
my_tuple = ("hello",)
print(my_tuple)
print(type(my_tuple))

my_tuple = ((1, 2, 3), (4, 5, 6))
print(my_tuple)
print(type(my_tuple))

print(my_tuple[1][2])

# 元组.index(元素)：查找指定元素在元组的下标
my_tuple = ("chen", "chen", "jia", "cheng")
print(my_tuple.index("cheng"))

# 元组.count(元素)：统计某元素在元组内的数量
print(my_tuple.count("chen"))

# len(元组)：统计元组中的元素数量
print(len(my_tuple))

# 元组的遍历：while循环
my_tuple = ("chen", "chen", "jia", "cheng")
index = 0
while index < len(my_tuple):
    print(my_tuple[index])
    index += 1

# 元组的遍历：for循环
for element in my_tuple:
    print(element)

my_tuple = (1, 2, ["jia", "cheng", 666])
print(my_tuple)
my_tuple[2][0] = "嘉"
my_tuple[2][1] = "程"
print(my_tuple)

# del my_tuple[2][2]
my_tuple[2].pop(2)
print(my_tuple)

my_tuple[2].append("Go")
print(my_tuple)

# 字符串数据容器只可以存储字符串；不可以修改数据
# 字符串是一个无法修改的数据容器
my_str = "chen jia cheng"
print(my_str[0], my_str[5], my_str[9])
print(my_str[-14])

# 字符串.index(元素)：查找指定元素在字符串的下标
print(my_str.index("a"))

# 字符串.replace(字符串1,字符串2)：将字符串1替换为字符串2。不是修改字符串本身，而是得到了一个新的字符串
new_my_str = my_str.replace("ch", "陈")
print(new_my_str)

# 字符串.split(分隔符字符串)：按照指定的分隔符字符串，将字符串划分为多个字符串，并存入列表对象中。字符串本身不变，而是得到了一个新的列表对象
my_str = "chen jia cheng and han yu jia"
my_str_list = my_str.split(" ")  # 字符串按照给定的字符串进行分割，变成多个子字符串，并存入一个列表对象中
print(my_str_list)

# 字符串.strip()：去除字符串的前后空格
my_str = " chen jia cheng "
new_my_str = my_str.strip()
print(new_my_str)

# 字符串.strip(字符串)：去除前后指定字符串
my_str = "123chen 12jia cheng321"
new_my_str = my_str.strip("12")  # 按照单个字符去除
print(new_my_str)

# 字符串.count(元素)：统计某字符串在字符串内的数量
my_str = "chen jia cheng"
print(my_str.count("ch"))

# len(字符串)：统计字符串中的元素数量
print(len(my_str))

# 字符串的遍历：while循环
my_str = "陈嘉程"

index = 0
while index < len(my_str):
    print(my_str[index])
    index += 1
# 字符串的遍历：for循环
for element in my_str:
    print(element)
