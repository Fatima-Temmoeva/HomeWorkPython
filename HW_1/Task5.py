#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print("Введи значение Х")
x = input()
print("Введи значение Y")
y = input()
print("Введи значение Z")
z = input()

if (not (x and y and z)) == ((not x) or (not y) or (not z)):
    print("True")
else:
    print("False")    
