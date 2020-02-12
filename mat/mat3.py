from matplotlib import pyplot as plt

# 柱形图
bar_positions = [1, 2, 3, 4, 5]
bar_heights = [10, 5, 10, 5, 20]
# 0.3 标识柱宽度
plt.barh(bar_positions, bar_heights, 0.3)
plt.show()

# 柱形图 散点图 折线图
# data = {'apples': 10, 'oranges': 15, 'lemons': 5, 'limes': 20}
# names = list(data.keys())
# values = list(data.values())
#
# # plt.figure(figsize=(6,8)):表示figure 的大小为宽、长（单位为inch）
# fig, axs = plt.subplots(1, 3, figsize=(9, 3))
# print(axs)
# axs[0].bar(names, values)
# axs[1].scatter(names, values)
# axs[2].plot(names, values)
# fig.suptitle('Categorical Plotting')
# plt.show()
