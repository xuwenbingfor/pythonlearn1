# 套索回归：使用L1作为正则化工具来训练的线性回归模型。
# 与L2 正则化不同的是， Ll 正则化会导致在使用套索回归的时候，有一部分特征的系数会正好等于0 。
# 也就是说，有一些特征会彻底被模型忽略掉，这也可以看成是模型对于特征进行自动选择的一种方式。
# 把一部分系数变成0 有助于让模型更容易理解，而且可以突出体现模型中最重要的那些特征。
# sci kit-learn 还提供了一种模型，称为弹性网模型（ Elastic Net ） 。
# 弹性网模型综合了套索回归和岭回归的惩罚因子。在实践中这两个模型的组合是效果最好的，然而代价
# 是用户需要调整两个参数，一个是L1 正则化参数，另一个是L2 正则化参数。


# 导人套索回归
import np as np
from sklearn.datasets import load_diabetes
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split

# 使用套索回归拟合数据
X, y = load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y)
lasso = Lasso(alpha=0.1,max_iter=100000).fit(X_train, y_train)
print('套索回归在训练数据集的得分{:.2f}'.format(lasso.score(X_train, y_train)))
print('套索回归在测试数据集的得分{:.2f} '.format(lasso.score(X_test, y_test)))
print('套索回归使用的特征数{} '.format(np.sum(lasso.coef_ != 0)))
