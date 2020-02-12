import numpy as np
import pandas as pd
from sklearn.feature_selection import SelectKBest,f_classif
import matplotlib.pyplot as plt

titanic = pd.read_csv('../pd/titanic.csv')
# 1、数据预处理
## Age缺失值处理
titanic['Age'] = titanic['Age'].fillna(titanic['Age'].median())

## Sex字符串转数值
titanic.loc[titanic['Sex'] == 'male', 'Sex'] = 0
titanic.loc[titanic['Sex'] == 'female', 'Sex'] = 1

## Embarked缺失值处理和字符串转数值
titanic['Embarked'] = titanic['Embarked'].fillna('S')
titanic.loc[titanic['Embarked'] == 'S', 'Embarked'] = 0
titanic.loc[titanic['Embarked'] == 'C', 'Embarked'] = 1
titanic.loc[titanic['Embarked'] == 'Q', 'Embarked'] = 2

# 2、选择重要的特征
predictors = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
selector = SelectKBest(f_classif,k=5)
selector.fit(titanic[predictors],titanic['Survived'])
scores = -np.log10(selector.pvalues_)

plt.bar(range(len(predictors)),scores)
plt.xticks(range(len(predictors)),predictors,rotation='vertical')
plt.show()

# predictors = ['Pclass', 'Sex', 'Fare', 'Embarked']