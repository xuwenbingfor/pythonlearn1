import numpy as np

vector = np.array([1, 2, 3])
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
# 1 生成向量和矩阵
# print(vector)
# print(matrix)

# 2 矩阵形状和reshape
# print(matrix.shape)
# matrix_shape = matrix.reshape(1,9)
# print(matrix.shape)
# print(matrix_shape.shape)

# 3 向量类型必须一致
# print(vector.dtype)
# vector[0] = 100 # ok
# vector[0] = 'hello' # error
# print(vector.dtype)

# 4 取值
# print(matrix[1,1])

# 5 切片（左闭右开，仅数字表示具体行）
# print(vector[0:2])
# print(matrix[:,0:2])
# print(matrix[:,:1])
# print(matrix[1,:])

# 6 判断操作（对向量/矩阵每个元素操作）
# print(vector == 3)
# print(matrix == 3)
# print((matrix == 3).dtype)

# 7 取值（通过bool）
# vector_bool = vector == 3
# print(vector[vector_bool])
# matrix_5 = matrix[:,2] == 5
# print(matrix_5)
# print(matrix[matrix_5,:])

# 8 numpy类型转换
# # vector = vector.astype(float)
# vector = vector.astype(str)
# # vector = np.array(['hello'])
# print(vector.dtype)
# print(vector)

# 9 显示帮助
# print(help(vector.astype))

# 10 常用函数
# print(vector.min())
# print(matrix.max())
# print(matrix.sum(axis=1))
# print(matrix.sum(axis=0))
# print(np.arange(9).reshape(3,3).ndim) # ndim 几维矩阵，这里是二维矩阵
# print(matrix.size)
# print(np.zeros((3, 3)))
# print(np.ones((3, 3),dtype=np.int32))
# print(np.arange(10, 50, 10))
# print(np.random.random((3,3)))
# print(np.linspace(0,1,100))


# 11 直接数学运算
# a = np.array([1,2,3])
# b = np.array([0,1,2])
# print(a - b)
# print(a ** 2)

# 12 一般乘和矩阵乘
# a = np.array([[1, 1],
#               [0, 1]])
# b = np.array([[2, 0],
#               [3, 4]])
# print(a * b)
# print(a.dot(b))

# 13 矩阵拼接
# a = np.array([[1, 1],
#               [1, 1]])
# b = np.array([0, 0])
# print(np.vstack((a,b)))
# print(np.hstack((a,b.reshape(2,1))))

# 14 矩阵拆分
# print(np.hsplit(matrix,3))
# print(np.hsplit(matrix,(1,1)))

# 15 无复制
# matrix_copy = matrix
# matrix_copy.shape = 1, 9
# print(matrix.shape)
# print(matrix_copy.shape)
# print(matrix is matrix_copy)

# 16 浅复制
# matrix_copy = matrix.view()
# matrix_copy.shape = 1, 9
# print(matrix.shape)
# print(matrix_copy.shape)
# print(matrix is matrix_copy)
# matrix[0,0] = 100
# print(matrix)
# print(matrix_copy)

# 17 深复制
# matrix_copy = matrix.copy()
# matrix_copy.shape = 1, 9
# print(matrix.shape)
# print(matrix_copy.shape)
# print(matrix is matrix_copy)
# matrix[0,0] = 100
# print(matrix)
# print(matrix_copy)

# 18 索引(axis=0:跨行，axis=1：跨列)
# matrix = np.array([
#     [1, 2, 3, 100],
#     [4, 5, 6, 100],
#     [7, 8, 9, 100]
# ])
# ind = matrix.argmax(axis=0)
# print(ind)
# print(matrix[ind, range(matrix.shape[1])])

# 矩阵拓展
# print(np.tile(matrix,(2,2)))

# 排序
matrix = np.array([
    [1, 100, 3, 2],
    [4, 5, 6, 100],
    [100, 8, 9, 7]
])
print(np.sort(matrix,axis=0))
print(np.sort(matrix,axis=1))