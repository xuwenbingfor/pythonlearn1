# 1、列表
# list1 = [1, 2, 3]
# list1[0] = -1
# print(list1)
# list1[1:-1] = [-2, -3, -4]
# print(list1)

# list1.pop(1)
# print(list1)

# print(3 in list1)

# print(list1.index(3))

# print(list1.count(1))

# 2、元组
# 原始功能
# (one, two, three, four) = (1, 2, 3, 4)
# print(one)
# 等号右侧的值会被打包为元组，然后拆包到左侧的变量中中
# one, two, three, four = 1, 2, 3, 4
# print(two)
# 扩展拆包，允许带*的元素接收任意数量的未匹配元素
# one, two, *three = 1, 2, 3, 4
# print(one)
# print(three)
# print(type(three))

# 3、集合
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# print(type(set1))
# print(type(set2))
# print(set1 | set2)
# print(set1 & set2)

# 4、字符串
print(','.join(['a', 'b', 'c']))
print('a,b,c'.split(','))
