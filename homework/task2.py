import os

file_path = os.path.join(os.path.dirname(__file__), 'task2.txt')

with open (file_path, encoding='UTF-8') as file:
    text = file.read()
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    print(text.count(' '))



print(sum(1 for line in open('task2.txt', 'r' )))

