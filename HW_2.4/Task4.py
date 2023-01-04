# Петя впервые пришел на урок физкультуры в новой школе. 
# Перед началом урока ученики выстраиваются по росту, в порядке невозрастания. 
# Напишите программу, которая определит на какое место в шеренге Пете нужно встать, 
# чтобы не нарушить традицию, если заранее известен рост каждого ученика и эти данные уже расположены по невозрастанию (то есть каждое следующее число не больше предыдущего). Если в классе есть несколько учеников с таким же ростом, как у Пети, то программа должна расположить его после них.

# Входные данные
# Первая строка входного файла INPUT.TXT содержит натуральное число N (N ≤ 100) – количество учеников (не считая Петю). 
# Во второй строке записаны N натуральных чисел Ai (Ai ≤ 200) – рост учеников в сантиметрах в порядке невозрастания. 
# Третья строка содержит единственное натуральное число X (X ≤ 200) – рост Пети.

# Выходные данные
# В выходной файл OUTPUT.TXT выведите единственное целое число – номер Пети в шеренге учеников.


print('Введи число N < 100 (Количество учеников, не считая Петю)')
n = input()
if int(n) >= int(100):
    print('Некорректное значение. Количество учеников в классе должно быть < 100')
    exit()
data = open(r'C:\Users\fatim\Desktop\PY_HW\HW_2.4\input.txt', 'w')
data.write(f'{n}\n')
data.close()

print('Введи рост учеников (A < 200)')
a = []
for i in range(int(n)):
    a.append(int(input()))
    # if a[i] >= int(200):
    #     print('Некорректное значение. Рост должен быть меньше 200')
    #     break

a_sort = sorted(a, reverse=True)
   
print(a_sort)
data = open(r'C:\Users\fatim\Desktop\PY_HW\HW_2.4\input.txt', 'a')
data.write(f'{a_sort}')

data.close()

print('Введи рост Пети')
x = input()
if int(x) >= int(200):
    print('Некорректное значение. Рост должен быть меньше 200')
data = open(r'C:\Users\fatim\Desktop\PY_HW\HW_2.4\input.txt', 'a')
data.write('\n')
data.write(f'{x}')
data.close()

k = 0
for i in range(len(a_sort) - 1):
    if int(x) > a_sort[i]:
        k = i
print(k + 1)
data = open(r'C:\Users\fatim\Desktop\PY_HW\HW_2.4\output.txt', 'w')
data.write(f'{k + 1}\n')
data.close()
                