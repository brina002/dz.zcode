#Скачайте любой датасет с сайта https://www.kaggle.com/datasets
#Загрузите набор данных из CSV-файла в DataFrame.
#Выведите первые 5 строк данных, чтобы получить представление о структуре данных.
#Выведите информацию о данных (.info()) и статистическое описание (.describe()).

import pandas as pd

df = pd.read_csv('healthy_eating_dataset.csv')
print(df.head())
print(df.info())
print(df.describe())

#Определите среднюю зарплату (Salary) по городу (City) - используйте файл приложенный к дз - dz.csv

df = pd.read_csv('dz.csv')

group1 = df.groupby('City')['Salary'].mean()
print(group1)

df.fillna(0, inplace=True)
print(df)

group2 = df.groupby('City')['Salary'].mean()
print(group2)

