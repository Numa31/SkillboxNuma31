import random
min = 1
max = 100
user = None
print('Загадайте число')
i = 1
while user != '=':
    number = random.randint(min,max) #рандомное число из диапазона
    print('Это число - ', number)
    user = input('Напишите мне угадал ли число, либо дайте подсказку знаками =, +, -. ')
    if user == '=':
       print('Ура я угадал! Вы загадали число:', number, 'Количество попыток ',i)
    elif user == '-':
       max = number -1
       print('Попробую поменьше!')
       i = i + 1
    elif user == '+':
       print('Попробую больше!')
       min = number + 1
       i = i + 1
    else:
       print('Потрачено...')


