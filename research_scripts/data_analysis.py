import pandas as pd
import re
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import math
from decimal import Decimal
from datetime import time

def time_to_minutes(t):
    total_minutes = t.hour * 60 + t.minute
    return total_minutes

def reverse_score(score):
    return (4 - score)

df = pd.read_excel('data/coursework_results.xlsx')


list_swl1 = df[('В большинстве аспектов моя жизнь близка к идеалу.')].tolist()
list_swl2 = df[('Условия моей жизни отличные.')].tolist()
list_swl3 = df[('Я доволен(-на) своей жизнью.')].tolist()
list_swl4 = df[('На сегодняшний день я достиг(-ла) важных целей в жизни.')].tolist()
list_swl5 = df[('Если бы я мог(-ла) начать свою жизнь заново, я почти ничего бы не изменил(-а).')].tolist()

summed_list_swl = [sum(item) for item in zip(list_swl1, list_swl2, list_swl3, list_swl4, list_swl5)]

print(df.columns)

list_pss1 = df[('Как часто за последний месяц вы были расстроены из-за чего-то, что произошло неожиданно?')].tolist()
list_pss2 = df[('Как часто за последний месяц вы чувствовали, что неспособны контролировать важные вещи в вашей жизни?')].tolist()
list_pss3 = df[('Как часто за последний месяц вы чувствовали себя нервно и напряженно?')].tolist()
list_pss4 = df[('Как часто за последний месяц вы чувствовали себя уверенно в своих способностях справляться с личными проблемами?')].tolist()
list_pss5 = df[('Как часто за последний месяц вы чувствовали, что всё идёт по вашему плану?')].tolist()
list_pss6 = df[('Как часто за последний месяц вы чувствовали, что не можете справиться со всеми вещами, которые вам необходимо сделать?')].tolist()
list_pss7 = df[('Как часто за последний месяц вы могли контролировать раздражающие факторы в вашей жизни?')].tolist()
list_pss8 = df[('Как часто за последний месяц вы чувствовали, что контролируете ситуацию?')].tolist()
list_pss9 = df[('Как часто за последний месяц вы злились из-за вещей, которые были вне вашего контроля?')].tolist()
list_pss10 = df[('Как часто за последний месяц вы чувствовали, что трудности становились настолько непреодолимыми, что вы не могли справиться с ними?  ')].tolist()

lists_pss = [list_pss1, list_pss2, list_pss3, list_pss4, list_pss5, list_pss6, list_pss7, list_pss8, list_pss9, list_pss10]

modified_lists_pss = [[x - 1 for x in lst] for lst in lists_pss]

lists_to_reverse = [3, 4, 6, 7]

for i in lists_to_reverse:
    modified_lists_pss[i] = [reverse_score(x) for x in modified_lists_pss[i]]

modified_list_pss = [sum(item) for item in zip(*modified_lists_pss)]


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



list_commute = df[("Сколько в среднем вы тратите времени на дорогу от дома до университета / места работы? Укажите время в формате часы:минуты.")]


list_commute = [time_to_minutes(t) for t in list_commute]

# physical health перекодировать
list_sleep = df[("Сколько часов в день вы в среднем спите?")].tolist()

for i in range(len(list_sleep)):
    if list_sleep[i] == "Меньше 6 часов":
        list_sleep[i] = 3
    if list_sleep[i] == "6-7 часов":
        list_sleep[i] = 2
    if list_sleep[i] == "7-8 часов":
        list_sleep[i] = 1
    if list_sleep[i] == "Больше 8 часов":
        list_sleep[i] = 0


list_sick = df[("Сколько раз вы болели (простудой, COVID-19, гриппом и другими заболеваниями) за последний учебный год?")].tolist()

for i in range(len(list_sick)):
    if list_sick[i] == "0 раз":
        list_sick[i] = 0
    if list_sick[i] == "1-2 раза":
        list_sick[i] = 1
    if list_sick[i] == "3-4 раза":
        list_sick[i] = 2
    if list_sick[i] == "Больше 4 раз":
        list_sick[i] = 3


list_tired = df[("Оцените свой уровень физической усталости после завершения рабочего дня по шкале от 1 до 5, где 1 — очень низкий уровень усталости, 5 — очень высокий уровень усталости.")].tolist()

for i in range(len(list_tired)):
    list_tired[i] -= 1

health_values = [list_sleep, list_sick, list_tired]
list_health = [sum(score) for score in zip(*health_values)]

list_commute_squared = [score ** 2 for score in list_commute]
def normalize_and_convert(value):
    if value[1] == '.':
        value[1] = ','
        return float(value)

list_grades = df[('Укажите ваш текущий GPA (средняя оценка по курсам, доступная в приложении HSE App X и в рейтинге на сайте).')].tolist()

def to_float(value):
    try:
        # Replace comma with dot
        if isinstance(value, str):
            value = value.replace(',', '.')
        # Convert to float
        float_value = float(value)
        return float_value
    except ValueError:
        # If conversion fails, check if value is nan (case-insensitive)
        if isinstance(value, str) and value.lower() == 'nan':
            return math.nan
        # If still fails, re-raise the exception
        raise

def convert_and_clean_list(input_list):
    # Convert values to float
    float_list = [to_float(value) for value in input_list]
    # Remove nan values
    cleaned_list = [value for value in float_list if not math.isnan(value)]
    return cleaned_list

# Example usage
list_grades = convert_and_clean_list(list_grades)
print(list_grades)

list_commute_log = np.log(list_commute)

df_result = pd.DataFrame(list(zip(list_commute, list_income, summed_list_swl, modified_list_pss, list_health, list_commute_squared, list_commute_log, list_sleep)), columns=['commute_time', 'income_level', 'life_satisfaction', 'stress_level', 'health_level', 'commute_squared', 'commute_log', 'sleep'])
print(df_result)


print(df_result['commute_log'].skew())

plt.figure(figsize=(10, 6))
sns.histplot(df_result["life_satisfaction"], kde=True, bins=8, color='forestgreen')
plt.title('Распределение уровней удовлетворенности жизнью студентов (SWLS)')
plt.xlabel('Значение метрики')
plt.ylabel('Частота')
plt.show()


plt.figure(figsize=(10, 6))
sns.histplot(df_result["commute_time"], kde=True, bins=12, color='skyblue')
plt.title('Распределение времени комьюта студентов')
plt.xlabel('Время комьюта (в минутах)')
plt.ylabel('Частота')
plt.show()


plt.figure(figsize=(10, 6))
sns.histplot(df_result["income_level"], kde=True, bins=5, color='maroon')
plt.title('Распределение уровня дохода')
plt.xlabel('Оценка дохода')
plt.ylabel('Частота')
plt.show()



plt.figure(figsize=(10, 6))
sns.histplot(df_result["stress_level"], kde=True, bins=12, color='plum')
plt.title('Распределение уровней стресса')
plt.xlabel('Оценка стресса')
plt.ylabel('Частота')
plt.show()

# income + commute ~ swl + pss + health + gpa
plt.figure(figsize=(10, 6))
sns.histplot(df_result["health_level"], kde=True, bins=7, color='navajowhite')
plt.title('Распределение оценки здоровья')
plt.xlabel('Оценка здоровья')
plt.ylabel('Частота')
plt.show()



income_level_new = [math.sqrt(score) for score in list_income]

plt.figure(figsize=(10, 6))
sns.histplot(income_level_new, kde=True, bins=7, color='navajowhite')
plt.title('Распределение оценки здоровья')
plt.xlabel('Оценка здоровья')
plt.ylabel('Частота')
plt.show()

res = 0
for i in list_commute:
    if i > 50:
        res += 1

print(res / 149, res)

list_commute_new = np.log(list_commute)

plt.figure(figsize=(10, 6))
sns.histplot(list_commute_new, kde=True, bins=12, color='navajowhite')
plt.title('Распределение оценки здоровья')
plt.xlabel('Оценка здоровья')
plt.ylabel('Частота')
plt.show()


model_dep_commute = sm.OLS.from_formula('list_commute ~ list_income', data=df_result).fit(cov_type="HC1")
print(model_dep_commute.summary())

model_dep_commute = sm.OLS.from_formula('np.log(list_commute) ~ list_income', data=df_result).fit(cov_type="HC1")
print(model_dep_commute.summary())



residuals = model_dep_commute.resid

model_swl = sm.OLS.from_formula('summed_list_swl ~ list_income + list_commute + commute_squared', data = df_result).fit(cov_type = "HC1")
print(model_swl.summary())

model_swl = sm.OLS.from_formula('summed_list_swl ~ list_income + list_commute + commute_squared', data = df_result).fit(cov_type = "HC3")
print(model_swl.summary())

model_swl = sm.OLS.from_formula('summed_list_swl ~ list_income + list_commute + commute_squared', data = df_result).fit()
print(model_swl.summary())




model_swl = sm.OLS.from_formula('summed_list_swl ~ list_income + list_commute', data = df_result).fit(cov_type = "HC1")
print(model_swl.summary())



model_swl_only_income = sm.OLS.from_formula('summed_list_swl ~ list_income', data = df_result).fit(cov_type = "HC1")
print(model_swl_only_income.summary())

model_pss = sm.OLS.from_formula('modified_list_pss ~ list_income + list_commute', data = df_result).fit(cov_type = "HC1")
print(model_pss.summary())

model_health = sm.OLS.from_formula('list_health ~ list_income + list_commute', data = df_result).fit(cov_type = "HC1")
print(model_health.summary())

model_health = sm.OLS.from_formula('list_health ~ list_income + list_commute', data = df_result).fit(cov_type = "HC1")
print(model_health.summary())




from sklearn.linear_model import LinearRegression
sns.lmplot(x="income_level", y="health_level", data=df_result)

plt.title("Regression Plot of Health Level vs. Income Level")
plt.xlabel("Income Level")
plt.ylabel("Health Level")

plt.show()

# может быть связь квадратичная

sns.lmplot(x="health_level", y="commute_time", data=df_result)

plt.title("Regression Plot of Health Level vs. Income Level")
plt.xlabel("Health Level")
plt.ylabel("Income Level")

plt.show()



sns.lmplot(x="income_level", y="life_satisfaction", data=df_result)

plt.title("Regression Plot of Life Satisfaction vs. Income Level")
plt.xlabel("Income Level")
plt.ylabel("Life Satisfaction")

plt.show()

import statistics

print("commute")
print(statistics.mean(list_commute))
print(statistics.median(list_commute))
print(statistics.stdev(list_commute))

print("swl")
print(statistics.mean(summed_list_swl))
print(statistics.median(summed_list_swl))
print(statistics.stdev(summed_list_swl))

print("pss")
print(statistics.mean(modified_list_pss))
print(statistics.median(modified_list_pss))
print(statistics.stdev(modified_list_pss))

print("physical health")
print(statistics.mean(list_health))
print(statistics.median(list_health))
print(statistics.stdev(list_health))





model_health = sm.OLS.from_formula('list_grades ~ list_income + list_commute', data = df_result).fit(cov_type = "HC1")
print(model_health.summary())





X = df_result[['list_income', 'list_commute']]
y = df_result['modified_list_pss']

# Add a constant to the independent variables matrix
X = sm.add_constant(X)

# Calculate the predicted values
y_pred = model.fittedvalues

# Plot the original data points
plt.scatter(df_result['list_income'], y, color='blue', label='Actual data')

# Plot the regression line
# Create a sequence of values for list_income
income_values = np.linspace(df_result['list_income'].min(), df_result['list_income'].max(), 100)
# Use the model to predict the values of modified_list_pss for these income values
# We fix list_commute to its mean value
commute_mean = df_result['list_commute'].mean()
predicted_values = model.predict(sm.add_constant(pd.DataFrame({'list_income': income_values, 'list_commute': commute_mean})))

plt.plot(income_values, predicted_values, color='red', linewidth=2, label='Regression line')

# Add labels and title
plt.xlabel('Income Level')
plt.ylabel('Modified PSS')
plt.title('Linear Regression')

# Add legend
plt.legend()

# Show plot
plt.show()






from sklearn.linear_model import LinearRegression

print(df_result.columns)







# Fit the model
model = sm.OLS(df_result['life_satisfaction'], df_result[['Intercept', 'commute_time', 'income_level']]).fit()


df_result['predicted_life_satisfaction'] = model.predict(df_result[['Intercept', 'commute_time', 'income_level']])

# Plotting
plt.figure(figsize=(10, 6))

# Scatter plot of actual values
plt.scatter(df_result['commute_time'], df_result['life_satisfaction'], color='blue', label='Actual data')

# Regression line
sorted_df = df_result.sort_values('commute_time')
plt.plot(sorted_df['commute_time'], sorted_df['predicted_life_satisfaction'], color='red', linewidth=2, label='Regression line')

# Labels and title
plt.xlabel('Commute Time (minutes)')
plt.ylabel('Life Satisfaction')
plt.title('Life Satisfaction vs. Commute Time with Income Level as Control')
plt.legend()

# Show the plot
plt.show()










# Prepare data (assuming df_result is your DataFrame with 'list_income' and 'list_commute')
X = df_result[['income_level', 'commute_time']]  # Independent variables
y = df_result['life_satisfaction']  # Dependent variable

# Create linear regression object
model = LinearRegression()

# Fit the model
model.fit(X, y)

# Print coefficients
print('Intercept:', model.intercept_)
print('Coefficients:', model.coef_)

print(model.summary())
df['predicted_life_satisfaction'] = model.predict(df[['Intercept', 'commute_time', 'income_level']])

# Predict values
plt.figure(figsize=(10, 6))

# Scatter plot of actual values
plt.scatter(df['commute_time'], df['life_satisfaction'], color='blue', label='Actual data')

# Regression line
sorted_df = df.sort_values('commute_time')
plt.plot(sorted_df['commute_time'], sorted_df['predicted_life_satisfaction'], color='red', linewidth=2, label='Regression line')

# Labels and title
plt.xlabel('Commute Time (minutes)')
plt.ylabel('Life Satisfaction')
plt.title('Life Satisfaction vs. Commute Time with Income Level as Control')
plt.legend()

# Show the plot
plt.show()












residuals = model.resid

# Plot histogram of residuals
plt.hist(residuals, bins=10, edgecolor='k')
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.title('Histogram of Residuals')
plt.show()







lst = []








def normalize_and_convert(value):
    value = re.sub(r',', '.', value)
    return float(value)

normalized_grades = [normalize_and_convert(grade) for grade in string_list]

print(normalized_grades)

