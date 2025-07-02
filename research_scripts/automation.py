import pyautogui
import time
import pyperclip
import pandas as pd

df = pd.read_excel('data/transliterated_file.xlsx')


pyautogui.hotkey('command','space', interval=0.1)
time.sleep(1)
pyautogui.write('HSE App')
pyautogui.press('return')

time.sleep(5)

pyautogui.hotkey('ctrl','space', interval=0.1)

search_field_x = 833
search_field_y = 779
pyautogui.click(search_field_x, search_field_y)


result_emails = []
need_to_redo = []
goal = df[('Востоковедение')].tolist()

for value in goal:

    search_field_x = 589.25
    search_field_y = 111.47
    pyautogui.click(search_field_x, search_field_y)

    pyautogui.write(value)

    time.sleep(5)

    person_x = 589.24
    person_y = 221.735
    pyautogui.click(person_x, person_y)

    time.sleep(4)

    email_x = 1000
    email_y = 272.4
    pyautogui.click(email_x, email_y)

    time.sleep(2)

    email_x = 840
    email_y = 445
    pyautogui.click(email_x, email_y)

    time.sleep(2)

    pyautogui.hotkey('command', 'c', interval=0.1)

    email = pyperclip.paste()

    if email or email in result_emails:
        result_emails.append(email)
        print(email)
    else:
        need_to_redo.append(value)

    time.sleep(1)

    cancel_x = 450
    cancel_y = 285
    pyautogui.click(cancel_x, cancel_y)

    cancel_x = 829.245
    cancel_y = 110
    pyautogui.click(cancel_x, cancel_y)

    time.sleep(2)

    cancel_x = 829.245
    cancel_y = 110
    pyautogui.click(cancel_x, cancel_y)

    time.sleep(1)

print("HERE'S THE END\n\n\n\n\n\n")







goal = df[('Востоковедение')].tolist()


for value in goal:

    search_field_x = 589.25
    search_field_y = 111.47
    pyautogui.click(search_field_x, search_field_y)

    pyautogui.write(value)

    time.sleep(5)

    person_x = 589.24
    person_y = 221.735
    pyautogui.click(person_x, person_y)

    time.sleep(4)

    email_x = 1000
    email_y = 272.4
    pyautogui.click(email_x, email_y)

    time.sleep(2)

    email_x = 840
    email_y = 445
    pyautogui.click(email_x, email_y)

    time.sleep(2)

    pyautogui.hotkey('command', 'c', interval=0.1)

    email = pyperclip.paste()

    if email or email in result_emails:
        result_emails.append(email)
        print(email)
    else:
        need_to_redo.append(value)

    time.sleep(1)

    cancel_x = 450
    cancel_y = 285
    pyautogui.click(cancel_x, cancel_y)

    cancel_x = 829.245
    cancel_y = 110
    pyautogui.click(cancel_x, cancel_y)

    time.sleep(1)

    cancel_x = 829.245
    cancel_y = 110
    pyautogui.click(cancel_x, cancel_y)

    time.sleep(3)

print("HERE'S THE END\n\n\n\n\n\n")



goal = df[('Медиакоммуникации')].tolist()


for value in goal:

    search_field_x = 589.25
    search_field_y = 111.47
    pyautogui.click(search_field_x, search_field_y)

    pyautogui.write(value)

    time.sleep(5)

    person_x = 589.24
    person_y = 221.735
    pyautogui.click(person_x, person_y)

    time.sleep(4)

    email_x = 1000
    email_y = 272.4
    pyautogui.click(email_x, email_y)

    time.sleep(2)

    email_x = 840
    email_y = 445
    pyautogui.click(email_x, email_y)

    time.sleep(2)

    pyautogui.hotkey('command', 'c', interval=0.1)

    email = pyperclip.paste()

    if email or email in result_emails:
        result_emails.append(email)
        print(email)
    else:
        need_to_redo.append(value)

    time.sleep(1)

    cancel_x = 450
    cancel_y = 285
    pyautogui.click(cancel_x, cancel_y)

    cancel_x = 829.245
    cancel_y = 110
    pyautogui.click(cancel_x, cancel_y)

    time.sleep(1)

    cancel_x = 829.245
    cancel_y = 110
    pyautogui.click(cancel_x, cancel_y)

    time.sleep(3)

print("HERE'S THE END\n\n\n\n\n\n")










goal = df[('Востоковедение')].tolist()


for value in goal:

    search_field_x = 589.25
    search_field_y = 111.47
    pyautogui.click(search_field_x, search_field_y)

    pyautogui.write(value)

    time.sleep(5)

    person_x = 589.24
    person_y = 221.735
    pyautogui.click(person_x, person_y)

    time.sleep(4)

    email_x = 1000
    email_y = 272.4
    pyautogui.click(email_x, email_y)

    time.sleep(2)

    email_x = 840
    email_y = 445
    pyautogui.click(email_x, email_y)

    time.sleep(2)

    pyautogui.hotkey('command', 'c', interval=0.1)

    email = pyperclip.paste()

    if email or email in result_emails:
        result_emails.append(email)
        print(email)
    else:
        need_to_redo.append(value)

    time.sleep(1)

    cancel_x = 450
    cancel_y = 285
    pyautogui.click(cancel_x, cancel_y)

    cancel_x = 829.245
    cancel_y = 110
    pyautogui.click(cancel_x, cancel_y)

    time.sleep(1)

    cancel_x = 829.245
    cancel_y = 110
    pyautogui.click(cancel_x, cancel_y)

    time.sleep(3)


print("HERE'S THE END\n\n\n\n\n\n")





result_emails = []
need_to_redo = []
goal = df[('Международная программа по экономике и финансам')].tolist()


for value in goal:

    search_field_x = 589.25
    search_field_y = 111.47
    pyautogui.click(search_field_x, search_field_y)

    pyautogui.write(value)

    time.sleep(5)

    person_x = 589.24
    person_y = 221.735
    pyautogui.click(person_x, person_y)

    time.sleep(4)

    email_x = 1000
    email_y = 272.4
    pyautogui.click(email_x, email_y)

    time.sleep(2)

    email_x = 840
    email_y = 445
    pyautogui.click(email_x, email_y)

    time.sleep(2)

    pyautogui.hotkey('command', 'c', interval=0.1)

    email = pyperclip.paste()

    if email or email in result_emails:
        result_emails.append(email)
        print(email)
    else:
        need_to_redo.append(value)

    time.sleep(1)

    cancel_x = 450
    cancel_y = 285
    pyautogui.click(cancel_x, cancel_y)

    cancel_x = 829.245
    cancel_y = 110
    pyautogui.click(cancel_x, cancel_y)

    time.sleep(1)

    cancel_x = 829.245
    cancel_y = 110
    pyautogui.click(cancel_x, cancel_y)

    time.sleep(3)


print("HERE'S THE END\n\n\n\n\n\n")










goal = df[('Реклама и связи с общественностью')].tolist()


for value in goal:

    search_field_x = 589.25
    search_field_y = 111.47
    pyautogui.click(search_field_x, search_field_y)

    pyautogui.write(value)

    time.sleep(5)

    person_x = 589.24
    person_y = 221.735
    pyautogui.click(person_x, person_y)

    time.sleep(4)

    email_x = 1000
    email_y = 272.4
    pyautogui.click(email_x, email_y) 

    time.sleep(2)

    email_x = 840
    email_y = 445
    pyautogui.click(email_x, email_y)

    time.sleep(2)

    pyautogui.hotkey('command', 'c', interval=0.1)

    email = pyperclip.paste()

    if email or email in result_emails:
        result_emails.append(email)
        print(email)
    else:
        need_to_redo.append(value)

    time.sleep(1)

    cancel_x = 450
    cancel_y = 285
    pyautogui.click(cancel_x, cancel_y)

    cancel_x = 829.245
    cancel_y = 110
    pyautogui.click(cancel_x, cancel_y)

    time.sleep(1)

    cancel_x = 829.245
    cancel_y = 110
    pyautogui.click(cancel_x, cancel_y)

    time.sleep(3)


print("HERE'S THE END\n\n\n\n\n\n")



goal = df[('Медиакоммуникации')].tolist()


for value in goal:

    search_field_x = 589.25
    search_field_y = 111.47
    pyautogui.click(search_field_x, search_field_y)

    pyautogui.write(value)

    time.sleep(5)

    person_x = 589.24
    person_y = 221.735
    pyautogui.click(person_x, person_y)

    time.sleep(4)


    email_x = 1000
    email_y = 272.4
    pyautogui.click(email_x, email_y)

    time.sleep(2)

    email_x = 840
    email_y = 445
    pyautogui.click(email_x, email_y)

    time.sleep(2)

    pyautogui.hotkey('command', 'c', interval=0.1)

    email = pyperclip.paste()

    if email or email in result_emails:
        result_emails.append(email)
        print(email)
    else:
        need_to_redo.append(value)

    time.sleep(1)

    cancel_x = 450
    cancel_y = 285
    pyautogui.click(cancel_x, cancel_y)

    cancel_x = 829.245
    cancel_y = 110
    pyautogui.click(cancel_x, cancel_y)

    time.sleep(1)

    cancel_x = 829.245
    cancel_y = 110
    pyautogui.click(cancel_x, cancel_y)

    time.sleep(3)


print("HERE'S THE END\n\n\n\n\n\n")



goal = df[('Международная программа по экономике и финансам')].tolist()


for value in goal:

    search_field_x = 589.25
    search_field_y = 111.47
    pyautogui.click(search_field_x, search_field_y)

    pyautogui.write(value)

    time.sleep(5)

    person_x = 589.24
    person_y = 221.735
    pyautogui.click(person_x, person_y)

    time.sleep(4)

    email_x = 1000
    email_y = 272.4
    pyautogui.click(email_x, email_y)

    time.sleep(2)

    email_x = 840
    email_y = 445
    pyautogui.click(email_x, email_y)

    time.sleep(2)

    pyautogui.hotkey('command', 'c', interval=0.1)

    email = pyperclip.paste()

    if email or email in result_emails:
        result_emails.append(email)
        print(email)
    else:
        need_to_redo.append(value)

    time.sleep(1)

    cancel_x = 450
    cancel_y = 285
    pyautogui.click(cancel_x, cancel_y)

    cancel_x = 829.245
    cancel_y = 110
    pyautogui.click(cancel_x, cancel_y)

    time.sleep(1)

    cancel_x = 829.245
    cancel_y = 110
    pyautogui.click(cancel_x, cancel_y)

    time.sleep(3)


print("HERE'S THE END\n\n\n\n\n\n")
