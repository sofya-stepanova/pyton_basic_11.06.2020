seconds = input('введите секунды: ')
hours = int(seconds) // 3600
minutes = (int(seconds) % 3600) // 60
sec = minutes % 60
print(f'{hours}:{minutes}:{sec}')
