from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

cancer = load_breast_cancer()
# print(cancer.keys())

X, y = cancer.data, cancer.target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
gnb = GaussianNB().fit(X_train, y_train)
print('乳腺癌测试数据集高斯贝叶斯模型得分：{:.3f}'.format(
    gnb.score(X_test, y_test)
))
print('乳腺癌训练数据集高斯贝叶斯模型得分：{:.3f}'.format(
    gnb.score(X_train, y_train)
))

print('模型预测结果：', gnb.predict([X[312]]))
print('真实结果：', y[312])
