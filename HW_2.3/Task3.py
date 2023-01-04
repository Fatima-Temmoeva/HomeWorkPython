# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

# Входные данные
# Входной файл INPUT.TXT содержит целое число N (1 < N ≤ 106).

# Выходные данные
# В выходной файл OUTPUT.TXT выведите ответ на задачу.

print('Введи целое число N, наименьший делитель которого необходимо найти')
n = input()
data = open(r'C:\Users\fatim\Desktop\PY_HW\HW_2.3\input.txt', 'w')
data.write(f'{n}\n')
data.close()

i = 1
with open(r'C:\Users\fatim\Desktop\PY_HW\HW_2.3\input.txt') as file:
    number = int(file.read())
    for i in range (2, int(number ** 0.5) + 1):
        if number % i == 0:
            data = open(r'C:\Users\fatim\Desktop\PY_HW\HW_2.3\output.txt', 'w')
            data.write(f'{i}\n')
            data.close()
            break
        else:
            data = open(r'C:\Users\fatim\Desktop\PY_HW\HW_2.3\output.txt', 'w')
            data.write(f'{number}\n')
            data.close()
            