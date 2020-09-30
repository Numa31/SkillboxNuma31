left = -1
right = 101
while True:
    number = (left+right)//2 #Определяем середину диапазона
    is_right = input('Ваше число: {}? (да,+,-)'.format(number))
    if is_right.lower() == 'да':# Ответ в нижнем регистре
        print ('Угадал!')
        break# Завершение цикла
    elif is_right=='+':
        left = number + 1
    elif is_right=='-':
        right = number - 1
    else:
        print ('Потрачено...')