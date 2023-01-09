# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: 
        # На столе лежит 2021 конфета. 
        # Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
        # Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
            # a) Добавьте игру против бота
            # b) Подумайте как наделить бота ""интеллектом""
from random import randint


def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

def botMove(isFirst, userMove):
    flag = randint(0, 1)

    if flag:
        if isFirst:
            return 29 - userMove
        else:
            x = 28 - userMove

        if x == 0:
            return 28
        
        return x
    else:
        return randint(1, 28)    
                

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = int(input("Введите количество конфет на столе: "))
flag = randint(0, 1)  
print(flag)
if flag:
    print(f"Первый ходит {player1}")
    botIsFirst = False
else:
    print(f"Первый ходит {player2}")
    botIsFirst = True

isBot = True

counter1 = 0
counter2 = 0
userMove = 1

while value > 28:
    if flag:
        k = input_dat(player1)
        userMove = k
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        if isBot:
            k = botMove(botIsFirst, userMove)        
        else:    
            k = input_dat(player2)

        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")