#6 задание
num = input('Введите число: ')
l = 0
for i in num:
    l+=int(i)
print(l)
#7 задание
num = input('Введите число: ')
l = 1
for i in num:
    l*=int(i)
print(l)
#8 задание
num = input('Введите число: ')
l = 0
for i in num:
    if i=='5':
        l+=1
if l>0:
    print('Цифра 5 есть в числе')
else:
    print('Цифры 5 нет в числе')
#9 задание
num = input('Введите число: ')
l = 0
for i in num:
    if int(i)>l:
        l=int(i)
print(l)
#10 задание
num = input('Введите число: ')
l = 0
for i in num:
    if i=='5':
        l+=1
print(l)