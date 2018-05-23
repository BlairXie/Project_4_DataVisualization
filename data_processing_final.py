# -*- coding: utf-8 -*-

import pandas as pd

data = pd.read_csv("train.csv")

# 计算所有乘客的生存率和死亡率
survive = data['Survived'].value_counts()
people = data['PassengerId'].count()
survived_ratio = survive/people


# 计算不同类别乘客的生存率


############# Pclass (Ticket class) ##############

class_amount = data['Pclass'].value_counts()
class1_survived_ratio = (data[(data['Pclass'] == 1) & (data["Survived"]==1)]['PassengerId'].count()) \
                        /float(class_amount[1])
class2_survived_ratio = (data[(data['Pclass'] == 2) & (data["Survived"]==1)]['PassengerId'].count()) \
                        /float(class_amount[2])
class3_survived_ratio = (data[(data['Pclass'] == 3) & (data["Survived"]==1)]['PassengerId'].count()) \
                        /float(class_amount[3])


############# 年龄 ##############
#年龄为空的不计入
minor_amount = data[data['Age'] <= 18]["PassengerId"].count()
elder_amount = data[data['Age'] >= 60]["PassengerId"].count()
else_survived_dead_amount = data[(data['Age'] > 18) & (data['Age'] < 60)]['Survived'].value_counts()
else_amount = data[(data['Age'] > 18) & (data['Age'] < 60)]['Survived'].count()
minor_survived_ratio = (data[(data['Age'] <= 18) & (data['Survived'] == 1)]['PassengerId'].count()) \
                      /float(minor_amount)
elder_survived_ratio = (data[(data['Age'] >= 60) & (data["Survived"]==1)]['PassengerId'].count()) \
                      /float(elder_amount)


else_survived_ratio = else_survived_dead_amount[1]/float(else_amount)



##################### 性别 ##########################
female_amount =  data[data['Sex']=='female']['Survived'].count()
male_amount = data[data['Sex']=='male']['Survived'].count()
female = data[data['Sex']=='female']['Survived'].value_counts()
male = data[data['Sex']=='male']['Survived'].value_counts()
female_survived_ratio = female[1]/float(female_amount)
male_survived_ratio = male[1]/float(male_amount)







############# Pclass+性别 ##############

class_female_amount = data[data['Sex'] == 'female']['Pclass'].value_counts()
class_male_amount = data[data['Sex'] == 'male']['Pclass'].value_counts()

class1_female_survived_ratio = (data[(data['Sex'] == "female") & (data['Pclass'] == 1) & (data["Survived"]==1)]['PassengerId'].count()) \
                                /float(class_female_amount[1])
class2_female_survived_ratio = (data[(data['Sex'] == "female") & (data['Pclass'] == 2) & (data["Survived"]==1)]['PassengerId'].count()) \
                                /float(class_female_amount[2])
class3_female_survived_ratio = (data[(data['Sex'] == "female") & (data['Pclass'] == 3) & (data["Survived"]==1)]['PassengerId'].count()) \
                                /float(class_female_amount[3])

class1_male_survived_ratio = (data[(data['Sex'] == "male") & (data['Pclass'] == 1) & (data["Survived"]==1)]['PassengerId'].count()) \
                                /float(class_male_amount[1])
class2_male_survived_ratio = (data[(data['Sex'] == "male") & (data['Pclass'] == 2) & (data["Survived"]==1)]['PassengerId'].count()) \
                                /float(class_male_amount[2])
class3_male_survived_ratio = (data[(data['Sex'] == "male") & (data['Pclass'] == 3) & (data["Survived"]==1)]['PassengerId'].count()) \
                                /float(class_male_amount[3])

my_dataset = [{"filter": "all", "category": "survived", "percentage": survived_ratio[1], "amount": survive[1]}, \
            {"filter": "all", "category": "dead", "percentage": survived_ratio[0], "amount": survive[0]}, \
            {"filter": "Ticket class", "category": "class 1", "survived percentage": class1_survived_ratio, "amount": class_amount[1]},\
            {"filter": "Ticket class", "category": "class 2", "survived percentage": class2_survived_ratio, "amount": class_amount[2]},\
            {"filter": "Ticket class", "category": "class 3", "survived percentage": class3_survived_ratio, "amount": class_amount[3]},\
            {"filter": "age", "category": "minor(<=18)", "survived percentage": minor_survived_ratio, "amount": minor_amount},\
            {"filter": "age", "category": "elder(>=60)", "survived percentage": elder_survived_ratio, "amount": elder_amount},\
            {"filter": "age", "category": "else", "survived percentage": else_survived_ratio, "amount": else_amount}, \
            {"filter": "sex", "category": "female", "survived percentage": female_survived_ratio, "amount": female_amount}, \
            {"filter": "sex", "category": "male", "survived percentage": male_survived_ratio, "amount": male_amount}, \
            {"filter": "Ticket class+sex", "category": "class 1", "survived percentage": class1_male_survived_ratio, "type":"male", \
            "amount": class_female_amount[1]},\
            {"filter": "Ticket class+sex", "category": "class 2", "survived percentage": class2_male_survived_ratio, "type":"male", \
            "amount": class_female_amount[2]},\
            {"filter": "Ticket class+sex", "category": "class 3", "survived percentage": class3_male_survived_ratio, "type":"male", \
            "amount": class_female_amount[3]},\
            {"filter": "Ticket class+sex", "category": "class 1", "survived percentage": class1_female_survived_ratio, "type":"female", \
            "amount": class_male_amount[1]},\
            {"filter": "Ticket class+sex", "category": "class 2", "survived percentage": class2_female_survived_ratio, "type":"female", \
            "amount": class_male_amount[2]},\
            {"filter": "Ticket class+sex", "category": "class 3", "survived percentage": class3_female_survived_ratio, "type":"female", \
            "amount": class_male_amount[3]}]
df2 = pd.DataFrame(data = my_dataset)
df2

df2.to_csv("Titanic_final2.csv", sep=',', encoding='utf-8')
