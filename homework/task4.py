import os

file_path = os.path.join(os.path.dirname(__file__), 'task4.txt')

with open (file_path, encoding='UTF-8') as file:
    text = file.read()
    text = text.replace("One", "один").replace("Two", "два").replace("Three", "три").replace("Four", "четыре")

with open (file_path, 'a', encoding='UTF-8') as file:
    file.write(f'\n{text}')