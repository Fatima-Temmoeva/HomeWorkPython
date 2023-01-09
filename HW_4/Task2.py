# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

print('Введи натуральное число N')
n = int(input())
d = 2
mnozh = []
while d ** 2 <= n:
    if n % d == 0:
        mnozh.append(d)
        n //= d 
    else:
        d += 1
mnozh.append(n)
print('Простые множители числа N =', mnozh)
