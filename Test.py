from random import *
print("Выберете камень, ножницы или бумагу.")
print()
a=0
while (a==0):
    player = int(input("1 - Камень, 2 - Ножницы, 3 - Бумага"))
    if (player==1 or player==2 or player==3):
        a=1

if player==1:
    print("Вы выбрали камень.")
elif player==2:
    print("Вы выбрали ножницы.")
elif player==3:
    print("Вы выбрали бумагу.")

bot=randint(1,3)

if bot==1:
    print("Компьютер выбрали камень.")
elif bot==2:
    print("Компьютер ножницы.")
elif bot==3:
    print("Компьютер бумагу.")

win=1
win=2
win=0

if player==1 and bot==2:
    win=1

if win==0:
    print("Ничья.")
if win==1:
    print("Вы выиграли.")
if win==2:
    print("Выиграл компьютер.")

a=0
while(a==0):