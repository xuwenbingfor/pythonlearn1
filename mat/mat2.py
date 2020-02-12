from matplotlib import pyplot as plt
import numpy as np

# 画子图
fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)

ax1.plot(np.random.randint(1,5,5),np.arange(5))
plt.show()