# sorted对数据容器进行排序，sort方法可以对列表进行排序
# sort():列表.sort(key=选择排序依据的函数,reverse=True/False) key:要求传入一个函数，表示将列表的每一个元素都传入函数中，返回排序的依据  True表示降序，False表示升序
my_list = [["a", 11], ["b", 22], ["c", 33]]


# 基于带名函数
def choose_sort_key(element):
    return element[1]

my_list.sort(key=choose_sort_key, reverse=True)


# 基于匿名函数
# my_list.sort(key=lambda element:element[1],reverse=True)

print(my_list)
