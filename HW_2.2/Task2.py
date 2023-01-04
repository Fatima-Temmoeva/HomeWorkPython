# Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно.

# Входные данные
# В единственной строке входного файла INPUT.TXT записано единственное целое число N, не превышающее по абсолютной величине 10^4.

# Выходные данные
# В единственную строку выходного файла OUTPUT.TXT нужно вывести одно целое число — сумму чисел, расположенных между 1 и N включительно.

print('Введи целое число N, чтобы посчитать сумма от 1 до N')
n = input()
data = open(r'C:\Users\fatim\Desktop\PY_HW\HW_2.2\input.txt', 'w')
data.write(f'{n}\n')
data.close()

symm = 0
number = 1
data = open(r'C:\Users\fatim\Desktop\PY_HW\HW_2.2\input.txt', 'r')
var = int(data.read())
while number <= var:
    symm = symm + number
    number +=1

data = open(r'C:\Users\fatim\Desktop\PY_HW\HW_2.2\output.txt', 'w')
data.write(f'{symm}\n')
data.close()