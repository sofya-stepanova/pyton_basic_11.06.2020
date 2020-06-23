def info():
    name = input('имя: ')
    surname = input('фамилия: ')
    year = input('год рождения: ')
    city = input('город проживания: ')
    email = input('электронная почта: ')
    tel = input('телефон: ')
    result = (f"{name}, {surname}, {year}, {city}, {email}, {tel}")
    return result

