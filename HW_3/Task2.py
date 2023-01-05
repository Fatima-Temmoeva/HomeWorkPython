# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
print('Введи число элементов списка')
n = input()
import Spisok
a = Spisok.input_list(n)
print(a)
Spisok.product_of_a_pair_of_numbers(a)
