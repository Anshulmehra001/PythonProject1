# keep adding a stream of number inputted y the user. The adding stops as soon as user presses q key on the keyboard

sum = 0
while(True):
    userInput = input("Enter the item price or quit: \n ")
    if (userInput!='q'):
        sum = sum + int(userInput)
        print(f"Order total so far: {sum}")
    else:
        print("thanks for using")
        print(f"your bill is {sum}. thanks for visiting")
        break