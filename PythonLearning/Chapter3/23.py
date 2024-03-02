"""
    变量的注解类型：
        1.帮助IDE工具对代码进行类型推断，协助做代码提示
        2.帮助开发者对变量进行注解
    类型注解只是提示性的，并非决定性的
    语法1:变量:类型
    语法2:# type:类型
"""
import json
import random
from typing import Union

# #一般无法直接看出变量类型时会添加变量的类型注解
# # 基础数据类型注解
# var1:int=10
# var2:str="xchen"
# var3:bool=True
# # 类对象注解类型
# class Student:
#     pass
# stu:Student=Student()
# # 基础容器注解类型
# my_list:list=[1,2,3]
# my_tuple:tuple=(1,2,3)
# my_dict:dict={"xchen":666}
# # 容器类型详细注解
# # my_list:list[int]=[10,11,12]
# # my_tuple:tuple[int,str,bool]=(1,"xchen",True)
# # my_dict:dict[str,int]={"xchen":666}


# 在注释中进行类型注解
var1 = random.randint(1, 10)  # type:int
var2 = json.loads('{"name":"xchen"}')  # type:dict[str,str]


def fun():
    return 10

var3 = fun()  # type:int


# 对函数（方法）进行类型注解

# 对形参进行类型注解
def add(x: int, y: int):
    return x + y

# add()


# 对返回值进行类型注解
def fun(data: list) -> list:
    return data

# fun()
# print(fun([1,2,3]))


# Union联合类型注解
my_list: list[Union[int, str]] = [1, 2, 3, "xchen"]


def fun(data: Union[int, str]) -> Union[int, str]:
    pass
# fun()
