# 随机森林：随机森林是用随机的方式构建的一个森林，而这个森林是由很多的相互不关联的决策树组成。
## 随机：数据采样随机，特征选择随机
## 所以理论上，随机森林的表现一般要优于单一的决策树，因为随机森林的结果是通过多个决策树结果投票来决定最后的结果。
## 简单来说，随机森林中每个决策树都有一个自己的结果，随机森林通过统计每个决策树的结果，选择投票数最多的结果作为其最终结果。
# -----------------------------------------------------------
# 集成算法：
## Bagging：训练多个分类器取平均，代表就是随机森林
## Boosting：从弱学习器开始加强，再加分析残差
## Stacking：可以堆叠各种分类器/回归（KNN、SVM、RF等）；分阶段：第一阶段得出各自结果，第二阶段再用前一个阶段结果训练。
# -----------------------------------------------------------

# 参考网址https://www.cnblogs.com/xiaoyh/p/11321780.html
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold

titanic = pd.read_csv('../pd/titanic.csv')
# 1、数据预处理
## Age缺失值处理
titanic['Age'] = titanic['Age'].fillna(titanic['Age'].median())

## Sex字符串转数值
titanic.loc[titanic['Sex'] == 'male','Sex'] = 0
titanic.loc[titanic['Sex'] == 'female','Sex'] = 1

## Embarked缺失值处理和字符串转数值
titanic['Embarked'] = titanic['Embarked'].fillna('S')
titanic.loc[titanic['Embarked'] == 'S','Embarked'] = 0
titanic.loc[titanic['Embarked'] == 'C','Embarked'] = 1
titanic.loc[titanic['Embarked'] == 'Q','Embarked'] = 2

# 2、线性回归
predictors = ['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked']
alg = LinearRegression()
kf = KFold(n_splits=3,shuffle=False,random_state=1)
predictions = []
for train,test in kf.split(titanic):
    train_predictors = (titanic[predictors].iloc[train,:])
    train_target = titanic['Survived'].iloc[train]
    alg.fit(train_predictors,train_target)
    test_predictions = alg.predict(titanic[predictors].iloc[test,:])
    predictions.append(test_predictions)
predictions = np.concatenate(predictions,axis=0)
predictions[predictions > .5] = 1  # 映射成分类结果 计算准确率
predictions[predictions <= .5] = 0
accuracy = sum(predictions==titanic['Survived'])/len(predictions)
print(accuracy)

