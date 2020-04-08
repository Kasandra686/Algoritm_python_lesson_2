# В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10
# попыток. После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то,
# что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.

from random import randint

a = randint(0, 100)
b = 0
while b < 10:
    x = int(input('Введите число '))
    if x == a:
        print('Вы угадали')
        break
    else:
        b += 1
        if x < a:
            print('Слишком маленькое число')
        else:
            print('Слишком большое число')
print(f'Загадано число {a}')
