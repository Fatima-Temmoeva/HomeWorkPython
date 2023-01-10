c = input()
a = 'аеёиоуыэюя'
def rifma(c):
    st = c.lower().split()
    f = lambda x: sum(1 for i in x if i in a)
    tmp = f(st[0])
    if all([f(i) == tmp for i in st]):
        return 'Рифма есть. Парам пам-пам'
    return 'Рифмы нет ...(. Пам парам'
print(rifma(c))