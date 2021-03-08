print('Загадайте число')
num = 'да'
l = 4
while num == 'да':
    l -= 1
    num = input(f'Количество цифр вашего числа меньше {l}? : ')  ## да или нет
num_2 = 'да'
dig = ''
while l > 0:
    number = 10
    while num_2 == 'да':
        number -= 1
        num_2 = input(f'Ваша {l}-e цифра меньше {number}? :')  # да или нет
    l -= 1
    dig = str(number) + dig
    num_2 = 'да'
print(dig)
