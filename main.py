#Imports the bedwars module from the Library folder
from Library.bedwars import *
run = True

#Makes infinte loop because "run" is equal to True
while run:
    #Takes inputs 1, 2, and 3 to find out which output you want
    choice = int(input("Type '1' if you want to check for number of coins\nType '2' if you want to check for wins\nType '3' if you want to check the losses\n"))
    if choice == 1:
        user = input("Please write the username:\n")
        print(coin(user))

    elif choice == 2:
        user = input("Please write the username:\n")
        print(wins(user))

    elif choice == 3:
        user = input("Please write the username:\n")
        print(losses(user))
    else:
        print("Invalid Input\n")