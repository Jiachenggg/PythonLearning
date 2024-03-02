# 序列：内容连续有序，支持下表索引的一类数据容器，如列表、元组、字符串
# 序列支持切片：从一个序列中，取出一个子序列。不会影响序列本身，而是会得到一个新的序列

# 序列[起始下标:结束下标:步长]：从指定位置开始，依次取出元素，到指定位置结束，得到一个新序列
# 起始下标可以留空，表示从头开始；结束下标可以留空，表示截取到结尾
my_list = [0, 1, 2, 3, 4, 5, 6]
print(my_list[1:4])  # 步长默认是1，可以省略不写
print(my_list[3:1:-1])

my_tuple = (0, 1, 2, 3, 4, 5, 6)
print(my_tuple[:])  # 起始和结束下标不写，表示从头到尾
print(my_tuple[::-2])

my_str = "0123456"
print(my_str[::2])

my_str = "retteb,gnehc aij nehc,og"
print(my_str[::-1][3:17])
print(my_str[7:21][::-1])
print(my_str.split(",")[1][::-1])

# 集合中的数据是无序存储的，所以集合不支持下标索引访问；不允许重复数据存在，但是是允许修改的
my_set = {"chen jia cheng", "han yu jia", "better", "chen jia cheng", "han yu jia", "better"}
s1 = set()  # 定义空集合
print(my_set)
print(type(my_set))

# 添加元素
my_set.add("go")
my_set.add("better")
print(my_set)

# 移除元素
my_set.remove("go")
print(my_set)

# 集合.pop():从集合随机取出一个元素
element = my_set.pop()
print(f"{my_set}被取出的元素为{element}")

# 清空集合
my_set.clear()
print(my_set)

# 集合1.difference(集合2)：取出集合1有而集合2没有的。结果：得到一个新集合，集合1和集合2不变
set1 = {1, 2, 3}
set2 = {1, 4, 5}
set3 = set1.difference(set2)
print(set3, set1, set2)

# 集合1.difference_update(集合2)：在集合1内，删除和集合2相同的元素。结果：集合1被修改，集合2不变
set1 = {1, 2, 3}
set2 = {1, 4, 5}
set1.difference_update(set2)
print(set1, set2)

# 集合1.union(集合2)：将集合1和集合2组成新集合。结果：得到新集合，集合1和集合2不变
set1 = {1, 2, 3}
set2 = {1, 4, 5}
set3 = set1.union(set2)
print(set3, set1, set2)

# 统计集合元素数量
set1 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
print(len(set1))

# 集合的遍历
# 由于集合不能使用下标索引，所以不能使用while循环，但是可以使用for循环
set1 = {1, 2, 3, 4, "chen"}
for element in set1:
    print(element)

# 字典同集合一样不可以使用下标索引，但是字典可以通过Key值来取得对应的Value
# 字典的Key和Value可以是任意数据类型（Key不可以为字典），表明字典是可以嵌套的
my_dict = {"xchen": 77, "xhan": 88, "xliu": 99}
print(my_dict)
print(type(my_dict))
# 定义空字典
my_dict = {}
my_dict = dict()

# 字典内Key不允许重复，重复添加等同于覆盖原有数据
my_dict = {"xchen": 77, "xchen": 88, "xliu": 99}
print(my_dict)

# 从字典中基于Key获取Value
my_dict = {"xchen": 77, "xhan": 88, "xliu": 99}
print(my_dict["xchen"])
print(my_dict["xhan"])
print(my_dict["xliu"])

# 定义嵌套字典
stu_dict = {
    "xchen": {
        "语文": 77,
        "数学": 88,
        "英语": 99
    },
    "xhan": {
        "语文": 99,
        "数学": 88,
        "英语": 77
    },
    "xliu": {
        "语文": 88,
        "数学": 77,
        "英语": 88
    }
}
print(stu_dict)
print(stu_dict["xchen"]["英语"])
print(stu_dict["xhan"]["语文"])

my_dict = {"xchen": 77, "xhan": 88, "xliu": 99}
# 添加元素
my_dict["xwang"] = 66
print(my_dict)

# 更新元素
my_dict["xchen"] = 88
print(my_dict)

# 字典.pop(Key)：指定Key的数据被删除
my_dict.pop("xwang")
print(my_dict)

# 字典.clear()：字典的元素被清空
my_dict.clear()
print(my_dict)

# 字典.keys()：得到字典中的全部Key
my_dict = {"xchen": 77, "xhan": 88, "xliu": 99}
keys = my_dict.keys()
print(keys)

# 统计字典的元素数量
print(len(my_dict))

# 字典的遍历
for key in keys:
    print(key, my_dict[key])

for key in my_dict:
    print(key, my_dict[key])

staff_dict = {
    "jett": {
        "部门": "科技部",
        "工资": 3000,
        "级别": 1
    },
    "sage": {
        "部门": "市场部",
        "工资": 5000,
        "级别": 2
    },
    "skye": {
        "部门": "市场部",
        "工资": 7000,
        "级别": 3
    },
    "KAY/O": {
        "部门": "科技部",
        "工资": 4000,
        "级别": 1
    },
    "raze": {
        "部门": "市场部",
        "工资": 6000,
        "级别": 2
    }
}
print(staff_dict)

for name in staff_dict:
    if staff_dict[name]["级别"] == 1:
        staff_info_dict = staff_dict[name]  # 获取员工的信息字典
        staff_info_dict["级别"] += 1
        staff_info_dict["工资"] += 1000
        staff_dict[name] = staff_info_dict  # 将员工信息更新回staff_dict
print(staff_dict)

"""
    数据容器的分类
    1是否支持下标索引：
        支持：列表、元组、字符串--序列类型
        不支持：集合、字典--非序列类型
    2是否支持重复元素：
        支持：列表、元组、字符串--序列类型
        不支持：集合、字典--非序列类型
    3是否可以修改：
        支持：列表、集合、字典
        不支持：元组、字符串
    
    列表、元组、字符串支持while循环，集合、字典不支持（无法下标索引）
"""
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_str = "abcdefg"
my_set = {1, 2, 3, 4, 5}
my_dict = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5}
print(len(my_list), len(my_tuple), len(my_str), len(my_set), len(my_dict))
print(max(my_list), max(my_tuple), max(my_str), max(my_set), max(my_dict))
print(min(my_list), min(my_tuple), min(my_str), min(my_set), min(my_dict))

"""
    容器的通用转换：
        list(容器)：将给定容器转换为列表
        tuple(容器)：将给定容器转换为元组
        str(容器)：将给定容器转换为字符串
        set(容器)：将给定容器转换为集合
"""
print(list(my_list), list(my_tuple), list(my_str), list(my_set), list(my_dict))
print(tuple(my_list), tuple(my_tuple), tuple(my_str), tuple(my_set), tuple(my_dict))
print(str(my_list), str(my_tuple), str(my_str), str(my_set), str(my_dict))
print(set(my_list), set(my_tuple), set(my_str), set(my_set), set(my_dict))

# sorted(容器,[reverse=True])：将给定容器进行排序
my_list = [3, 1, 4, 5, 2]
my_tuple = (3, 1, 4, 5, 2)
my_str = "edgcfba"
my_set = {3, 1, 4, 5, 2}
my_dict = {"key3": 3, "key1": 1, "key4": 4, "key5": 5, "key2": 2}
print(sorted(my_list), sorted(my_tuple), sorted(my_str), sorted(my_set), sorted(my_dict))  # 顺序
print(sorted(my_list, reverse=True), sorted(my_tuple, reverse=True), sorted(my_str, reverse=True),
      sorted(my_set, reverse=True), sorted(my_dict, reverse=True))  # 逆序

print("abd" > "abc", "ab" > "a", "ab" > "a", "key2" > "key1")
