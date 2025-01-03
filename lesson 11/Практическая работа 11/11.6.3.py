import math

while True:
    file_size = int(input('Укажите размер файла для скачивания: '))
    speed = int(input('Какова скорость вашего соединения: '))
    if file_size < 1 or speed < 1:
        print('че клоун?')
    else:
        sec = math.ceil(file_size / speed)
        downloaded = 0
        for second in range(1, sec+1):
            if downloaded < file_size - speed:
                downloaded += speed
                procent = math.ceil(downloaded / file_size * 100)
                print('Прошло', second, 'сек. Скачано', downloaded, 'из', file_size, 'Мб (',procent,'%)')
            else:
                print('Прошло', second, 'сек. Скачано', file_size, 'из', file_size, 'Мб ( 100% )')

