#1
m = input('Введите число: ')
for i in range(1, int(m)+1):
    print(i)
#2
m1 = int(input('Введите первое число: '))
m2 = int(input('Введите второе число: '))
if m1 == m2:
    print('Числа равны.')
else:
    print('Больше число: ', max(m1, m2))