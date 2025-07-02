import pandas as pd
import re
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import math

def time_to_minutes(t):
    total_minutes = t.hour * 60 + t.minute
    return total_minutes

df = pd.read_excel("data/coursework_results.xlsx")

list_commute = df[("Сколько в среднем вы тратите времени на дорогу от дома до университета / места работы? Укажите время в формате часы:минуты.")]
list_commute = [time_to_minutes(t) for t in list_commute]

list_grades = df[('Укажите ваш текущий GPA (средняя оценка по курсам, доступная в приложении HSE App X и в рейтинге на сайте).')].tolist()
def to_float(value):
    try:
        if isinstance(value, str):
            value = value.replace(',', '.')
        float_value = float(value)
        return float_value
    except ValueError:
        if isinstance(value, str) and value.lower() == 'nan':
            return math.nan
        raise

def convert_and_clean_list(input_list):
    float_list = [to_float(value) for value in input_list]
    cleaned_list = [value for value in float_list if not math.isnan(value)]
    return cleaned_list

list_grades = convert_and_clean_list(list_grades)
print(list_grades)

list_income = df[('Укажите уровень дохода вашей семьи.')].tolist()

for i in range(len(list_income)):
    if list_income[i] == "Нам не хватает денег даже на питание":
        list_income[i] = 0
    if list_income[i] == "Нам хватает денег на питание, но не хватает на одежду":
        list_income[i] = 1
    if list_income[i] == "Нам хватает денег на питание и одежду, покупка более дорогих вещей, таких как телевизор или холодильник, вызывает у нас проблемы":
        list_income[i] = 2
    if list_income[i] == "Мы можем покупать некоторые дорогие вещи, такие как холодильник или телевизор, но не можем купить автомобиль":
        list_income[i] = 3
    if list_income[i] == "Мы можем купить автомобиль, но не можем сказать, что не стеснены в средствах":
        list_income[i] = 4
    if list_income[i] == "Мы можем ни в чем себе не отказывать":
        list_income[i] = 5


df_result = pd.DataFrame(list(zip(list_commute, list_income, list_grades)), columns=['commute_time', 'income_level', 'grades'])
print(df_result)

list_grades_new = np.square(list_grades)

plt.figure(figsize=(10, 6))
sns.histplot(list_grades_new, kde=True, bins=12, color='navajowhite')
plt.title('Распределение средних оценок студентов за 1 семестр')
plt.xlabel('Средняя оценка за 1 семестр')
plt.ylabel('Частота')
plt.show()


model_grades = sm.OLS.from_formula('list_grades ~ list_commute + list_income', data = df_result).fit(cov_type = "HC1")
print(model_grades.summary())


model_grades = sm.OLS.from_formula('list_grades_new ~ list_commute + list_income', data = df_result).fit(cov_type = "HC1")
print(model_grades.summary())
