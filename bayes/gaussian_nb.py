from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

# 事实上， 高斯朴素贝叶斯也确实是能够胜任大部分的分类任务， 这是因为在自然科学和社会科学领域，有大量的现象都是呈现出正态分布的状态
X, y = make_blobs(n_samples=500, centers=5, random_state=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

gnb = GaussianNB().fit(X_train, y_train)
print('测试数据集高斯贝叶斯模型得分：{:.3f}'.format(
    gnb.score(X_test, y_test)
))
print('训练数据集高斯贝叶斯模型得分：{:.3f}'.format(
    gnb.score(X_train, y_train)
))
