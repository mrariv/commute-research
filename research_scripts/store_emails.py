import pandas as pd

file_path = 'data/coursework_sample.xlsx'

df = pd.read_excel(file_path)
values_list = df.values.flatten().tolist()

values_list = [value for value in values_list if pd.notna(value)]

values_list = set(values_list)

print(len(values_list))
values_list = values_list.shuffle()

for email in values_list:
    print(email)
