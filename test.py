from Library.bedwars import *
run = True

while run:
    choice = int(input("Write '1' if you want to check for number of coins\nWrite '2' if you want ot check for wins\nWrite '3' if you want to check the losses\n"))
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
        run = False