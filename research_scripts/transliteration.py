import pandas as pd
from transliterate import translit, detect_language

def custom_translit(text, custom_rules):
    result = []
    for char in text:
        result.append(custom_rules.get(char, char))
    return ''.join(result)

custom_rules = {
    'а': 'f', 'б': ',', 'в': 'd', 'г': 'u', 'д': 'l', 'е': 't', 'ё': '\\',
    'ж': ";", 'з': 'p', 'и': 'b', 'й': 'q', 'к': 'r', 'л': 'k', 'м': 'v',
    'н': 'y', 'о': 'j', 'п': 'g', 'р': 'h', 'с': 'c', 'т': 'n', 'у': 'e',
    'ф': 'a', 'х': '[', 'ц': 'w', 'ч': 'x', 'ш': 'i', 'щ': 'o', 'ъ': ']',
    'ы': 's', 'ь': 'm', 'э': "'", 'ю': '.', 'я': 'z',

    'А': 'F', 'Б': '<', 'В': 'D', 'Г': 'U', 'Д': 'L', 'Е': 'T', 'Ё': '|',
    'Ж': ':', 'З': 'P', 'И': 'B', 'Й': 'Q', 'К': 'R', 'Л': 'K', 'М': 'V',
    'Н': 'Y', 'О': 'J', 'П': 'G', 'Р': 'H', 'С': 'C', 'Т': 'N', 'У': 'E',
    'Ф': 'A', 'Х': '{', 'Ц': 'W', 'Ч': 'X', 'Ш': 'I', 'Щ': 'O', 'Ъ': '}',
    'Ы': 'S', 'Ь': 'M', 'Э': '"', 'Ю': '>', 'Я': 'Z'
}

df = pd.read_excel('data/coursework_sample.xlsx')

for column in df.columns:
    df[column] = df[column].apply(lambda name: custom_translit(str(name), custom_rules) if pd.notnull(name) else name)

df.to_excel('transliterated_file.xlsx', index=False)
