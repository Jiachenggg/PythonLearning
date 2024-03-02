def addition(a, b):
    print(a + b)


def subtraction(a, b):
    print(a - b)


# __all__ = ['addition']# __all__变量可以控制import *时哪些功能可以被导入

if __name__ == '__main__':
    addition(1, 1)
