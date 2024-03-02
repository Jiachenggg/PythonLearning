# JSON是一种轻量级的数据交互格式，可以按照JSON指定的格式去组织和封装数据
# JSON本质是一个带有特定格式的字符串
# JSON是一种在各个编程语言中流通的数据格式，负责不同编程语言中的数据传递和交互
# Python使用JSON有很大的优势，因为JSON就是一个单独的字典或者一个内部元素都是字典的列表，所以JSON可以直接和Python的字典或列表进行无缝转换
import json

# 将Python数据类型转换为JSON字符串
data = [{"name": "小陈", "age": 23}, {"name": "小韩", "age": 23}, {"name": "小刘", "age": 23}]
json_str = json.dumps(data, ensure_ascii=False)
print(json_str)
print(type(json_str))

data = {"name": "小陈", "age": 23}
json_str = json.dumps(data, ensure_ascii=False)
print(json_str)
print(type(json_str))

# 将JSON字符串转换为Python数据类型
str = '[{"name":"小陈","age":23},{"name":"小韩","age":23},{"name":"小刘","age":23}]'
list = json.loads(str)
print(list)
print(type(list))

str = '{"name":"小陈","age":23}'
dict = json.loads(str)
print(dict)
print(type(dict))
