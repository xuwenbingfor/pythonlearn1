from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import MinMaxScaler

# 多项式朴素贝叶斯只适合用来对非负离散数值特征进行分类
# 二项式分布可以通过抛硬币的例子来进行理解，那么多项式分布都可以用掷假子来理解。
scaler = MinMaxScaler()
X, y = make_blobs(n_samples=500, centers=5, random_state=1)
# print(X)
# 数据归一化到0-1
X = scaler.fit_transform(X)
# print(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

mnb = MultinomialNB().fit(X_train, y_train)
print('测试数据集多项式贝叶斯模型得分：{:.3f}'.format(
    mnb.score(X_test, y_test)
))
print('训练数据集多项式贝叶斯模型得分：{:.3f}'.format(
    mnb.score(X_train, y_train)
))
