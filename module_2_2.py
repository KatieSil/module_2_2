first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first == second == third:
    print('Количество одинаковых чисел: 3')
elif first == second or second == third or third == first:
    print('Количество одинаковых чисел: 2')
else:
    print('Количество одинаковых чисел: 0')
