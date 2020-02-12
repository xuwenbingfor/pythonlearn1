# 对于一个二分类问题来说，这个准确率似乎不太行，接下来用逻辑回归算法试下
import pandas as pd

titanic = pd.read_csv('../pd/titanic.csv')
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

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

# 2、逻辑回归
predictors = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
alg = LogisticRegression(random_state=1)
scores = cross_val_score(alg, titanic[predictors], titanic["Survived"], cv=3)
print(scores.mean())
