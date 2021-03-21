name = str(input("Enter Your Name: "))
print(f"{name} you are stuck at work")
while True:
    print(" You are still working and suddenly you you saw a ghost, Now you have two options")
    print("1.Run. 2.Jump from the window")
    answer = input("Choose 1 or 2: ")
    if answer == '1':
        print("You did it")
    elif answer == '2':
        print("You are not that smart")
    else:
        print("Please Check your input")
    if input('Another question? (Y / N ) -> ').lower() != 'y':
        break
