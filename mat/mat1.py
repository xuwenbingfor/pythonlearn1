from matplotlib import pyplot as plt

x = range(0, 10, 1)
y = range(10, 30, 2)
# 折线图
plt.plot(x, y)
plt.xlabel('Years')
plt.ylabel('Get')
plt.title('History Of Programmer')
plt.show()

# 一般流程
# 1、总体配置
#   plt.rcParams：run configuration
# 2、创建画布和创建子图
#   api
# 3、添加画布内容
#   api
# 4、保存和显示图形
#   api
