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