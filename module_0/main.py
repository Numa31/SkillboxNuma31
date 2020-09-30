left = -1
right = 101
while True:
    number = (left+right)//2 #Определяем середину диапазона
    isright = input('Ваше число: {}? (да,+,-)'.format(number))
    if isright.lower() == 'да':
        print ('Есть!')
        break
    elif isright=='+':
        left = number + 1
    elif isright=='-':
        right = number - 1
    else:
        print ('Потрачено')
