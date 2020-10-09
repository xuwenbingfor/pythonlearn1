# 1、函数参数
## 默认值形参
def func1(a, b=1):
    print('a+b=', a + b)


# func1(1)
# func1(1, 2)


## 按形参位置传递
## 按形参名称传递:适用于函数有大量形参且大多数形参都有默认值,同时需要修改某个默认值的情况
## 变长形参
# 1. 位置实参数量不定时的处理
def func2(a, b, *c):
    print(a)
    print(b)
    print(c)


func2(1, 2, 3, 4)
# 2. 关键字实参数量不定时的处理
# def func2(a, b, **c):
#     print(a)
#     print(b)
#     print(c)
#
#
# func2(1, 2, x=3, y=4)

# 混合使用顺序

# 2、将函数赋值给变量
# 3、lambda表达式
# 4、迭代器生成函数
# 5、装饰器
# 6、functools模块