print('Введите число для перевода в двоичную систему', )
n = int(input())
s = ''
while n != 0:
    s = str(n % 2) + s
    n = n // 2
print('Ваше число в двоичной системе счисления =>', s)