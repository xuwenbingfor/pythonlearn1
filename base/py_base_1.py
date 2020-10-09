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
# print(','.join(['a', 'b', 'c']))
# print('a,b,c'.split(','))
print(str([1, 2, 3]))
print(repr([1, 2, 3]))
# print('{0} is a {1}'.format('god', 'girl'))


# 5、map
# map1 = {'one': '1'}
# # print(type(map1))
# map1['two'] = '2'
# print(map1)
# print(map1['two'])
# print(map1.items())
# map1.pop('two')
# print(map1)

# for
# print(range(10))
# for i in range(10):
#     print(i)
# list1 = ['a', 'b', 'c']
# # # print(enumerate(list1))
# # for v, i in enumerate(list1):
# #     print('v:', v, 'i:', i)
# list0 = [0, 1, 2, 3]
# print(list(zip(list1, list0)))


# 列表和字典推导式
# list1 = [item * item for item in list0 if item > 0]
# print(list1)
# map1 = {item: item * item for item in list0 if item > 0}
# print(map1)

# 生成器表达式：和列表推导式异同

# 模块和作用域
# 1、global/nonlocal：https://www.cnblogs.com/huwt/p/11185516.html
# 2-1、包__init__,__all__
# 2-2、模块或直接对象; import，https://www.cnblogs.com/moonpool/p/11333117.html
# import sys
#
# for v in sys.path:
#     print(v)
# print(__name__)
# from bayes.import_test import import_test
# from bayes import import_test
# print(import_test)

# 异常处理
# 继承关系、raise Exception('')
# with和上下文管理器。文件对象就是一种上下文管理器，更多信息见标准库contextlib文档。