# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

stroka = input('Введи строку для сжатия:  ')
print('Исходная строка: ', stroka)

def encode(stroka):
    encoding = ''
    i = 0
    while i < len(stroka):
        count = 1
        while i + 1 < len(stroka) and stroka[i] == stroka[i + 1]:
            count += 1
            i += 1
        encoding += str(count) + stroka[i]
        i = i + 1
    return encoding

print('Сжатая строка: ', encode(stroka))

   