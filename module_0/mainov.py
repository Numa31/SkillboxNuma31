import random
min = 1
max = 100
user = None
print('Загадайте число')
while user != '=':
    number_1 = random.randint(min,max)
    print('Это число - ', number_1)
    user = input('Напишите мне угадал ли число, либо дайте подсказку знаками =, +, -. ')
    if user == '=':
       print('Ура я угадал! Вы загадали число:', number_1)
    elif user == '-':
       max = number_1 -1
       print('Попробую поменьше!')
    elif user == '+':
       print('Попробую больше!')
       min = number_1 + 1


       # а я все летала

