# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на |K| элементов вправо, если K – положительное и влево, если отрицательное.

# Входные данные
# Первая строка входного файла INPUT.TXT содержит натуральное число N, 
# во второй строке записаны N целых чисел Ai, а в последней – целое число K. (1 ≤ N ≤ 105, |K| ≤ 105, |Ai| ≤ 100).

# Выходные данные
# В выходной файл OUTPUT.TXT выведите полученную последовательность.

print('Введи число 1 <= N <= 105')
n = input()
if int(n) > int(105):
    print('Некорректное значение. N должно быть <= 105')
    exit()
data = open(r'C:\Users\fatim\Desktop\PY_HW\HW_3\Task6\input.txt', 'w')
data.write(f'{n}\n')
data.close()

print('Введи N целых чисел Ai (|Ai| ≤ 100)')
a = []
for i in range(int(n)):
    a.append(int(input()))
    if a[i] > int(100):
        print('Некорректное значение. |Ai| ≤ 100 ')
        exit()
data = open(r'C:\Users\fatim\Desktop\PY_HW\HW_3\Task6\input.txt', 'a')
data.write(f'{a}')
data.close()

print('Введи целое число K циклический сдвиг - вправо, если K – положительное и влево, если отрицательное')
k = input()
if int(k) > int(105):
    print('Некорректное значение. K должно быть <= 105')
    exit()
data = open(r'C:\Users\fatim\Desktop\PY_HW\HW_3\Task6\input.txt', 'a')
data.write(f'\n{k}\n')
data.close()

k = int(k)
n = int(n)
#c = 0
if int(k) > int(0):
    for i in range(k):
        temp = a[i]
        a[i] = a[n - k + i]
        a[n - k + i] = temp
    print(a)

elif int(k) < int(0):
    print(a)
    for z in range(abs(k)):
        for i in range(n-1):
            temp = a[i-1]
            a[i-1] = a[i]
            a[i] = temp
    #print(a)
data = open(r'C:\Users\fatim\Desktop\PY_HW\HW_3\Task6\output.txt', 'w')
data.write(f'{a}\n')
data.close()