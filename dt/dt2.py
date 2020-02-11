# 遍历选择最合适的参数组合。
# cv：交叉验证：将训练集平分为3份A、B、C：
# A+B为训练集，C为训练集
# A+C为训练集，B为训练集
# C+B为训练集，A为训练集
# 求三次验证得分平均值
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

# 创建随机森林模型
rf = RandomForestClassifier()

# 设置需要调优的参数和其范围，GridSearchCV会帮助我们在范围中找到最优值
parameters = {"n_estimators": range(1, 11)}

# 加载数据集
iris = load_iris()

# 使用 GridSearchCV 进行参数调优
clf = GridSearchCV(estimator=rf, param_grid=parameters)

# 对 iris 数据集进行分类
clf.fit(iris.data, iris.target)

# 提供优化过程期间观察到的最好的评分
print(" 最优分数： %.4lf" % clf.best_score_)

# best_params_：描述了已取得最佳结果的参数的组合
print(" 最优参数：", clf.best_params_)
