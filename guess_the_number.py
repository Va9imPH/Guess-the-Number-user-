import random
import sys

while True:
    user_data = int(input('Загадайте число от 1 до 10: '))
    computer_data = random.randint(1, 10)
    if computer_data == user_data:
        print('Компьютер угадал')
    elif user_data > 10:
        print('Ошибка! Введите число меньше 10')
    elif user_data < 1:
        print('Ошибка! Напишите число больше 0')
    else:
        print('Компьютер не угадал и выбрал:', computer_data)

    stop = input('Хотите продлжить? да/нет: ').lower()

    if stop == 'нет':
        print('Вы вышли из игры')
        sys.exit()