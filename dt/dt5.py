import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestClassifier

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

# 2、随机森林
# predictors = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
predictors = ['Pclass', 'Sex', 'Fare', 'Embarked']
alg = RandomForestClassifier(random_state=1,
                             n_estimators=100,
                             min_samples_split=4,
                             min_samples_leaf=2)
kf = KFold(n_splits=3, shuffle=False, random_state=1)
scores = cross_val_score(alg, titanic[predictors], titanic["Survived"], cv=kf)
print(scores.mean())
