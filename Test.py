from random import *
a=0
while a!="x":
        try:
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
            if player==1 and bot==2 or player==2 and bot==3 or player==3 and bot==1:
                win=1
            if player==1 and bot==3 or player==2 and bot==1 or player==3 and bot==2:
                win=2
            if player==3 and bot==3 or player==2 and bot==2 or player==1 and bot==1:
                win=0
            if win==0:
                print("Ничья.")
            elif win==1:
                print("Вы победили!")
            elif win==2:
                print("Победил компьютер.")
        except:
            ValueError