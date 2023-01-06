n = int(input('Задайте число для составления списка чисел Фибоначчи: \n'))
def fibo(ind):
    if ind == 0:
       return 0
    elif ind == 1:
        return 1
    return fibo(ind - 1) + fibo(ind - 2)
f = [fibo(x) for x in range(n + 1)]
print('Числа Фибоначчи = \n',f)

b = -n
def nefibo(i):
    if i == -1:
       return 1
    elif i == -2:
        return -1
    return nefibo(i + 2) - nefibo(i + 1)
k = [nefibo(z) for z in range(b, 0)]
print('Числа негафибоначчи = \n ', k)

fib = k + f
print('Последовательность чисел Фибоначчи, в том числе для отрицательных индексов = \n', fib)
