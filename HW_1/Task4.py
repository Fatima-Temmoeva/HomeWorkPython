# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

print("Введи координаты точки А")
XA = int(input())
YA = int(input())
print("Введи координаты точки В")
XB = int(input())
YB = int(input())
print("Координаты точки A =" , "(", f'{XA}', ";" , f'{YA}', ")")
print("Координаты точки B =" , "(", f'{XB}', ";" , f'{YB}', ")")
print('Расстояние между точками равно = ', ((XB - XA)**(2) + (YB - YA)**(2))**(1 / 2))