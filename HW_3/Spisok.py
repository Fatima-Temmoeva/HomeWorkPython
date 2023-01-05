def input_list(n):
    print('Введите список чисел')
    a = []
    for i in range(int(n)):
         a.append(input())
    print('Вы ввели список')
    return a

def summ_odd_elem(a):
     summ = 0
     for item in range(len(a)):
          if item % 2 != 0:
               print('На нечетной позиции стоит элемент')
               print(a[item])
               summ = summ + int(a[item])
     print('Сумма элементов на нечетных позициях равна summ = ')
     return summ

def product_of_a_pair_of_numbers(a):
     sum = []
     dlina = int(0)
     if len(a) % 2 == 0:
          dlina = int(len(a) // 2)
     else:
          dlina = int(len(a) // 2 + 1)
     for i in range(dlina):
          sum.append(int(a[i]) * int(a[len(a)-i-1]))
     print(f'{sum}')
     return sum
