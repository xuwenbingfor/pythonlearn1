from matplotlib import pyplot as plt

x = range(0, 10, 1)
y = range(10, 30, 2)
# 折线图
plt.plot(x, y)
plt.xlabel('Years')
plt.ylabel('Get')
plt.title('History Of Programmer')
plt.show()
