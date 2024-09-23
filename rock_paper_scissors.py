import random

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. "))
options = ["Rock", "Paper", "Scissors"]
computer_selection = random.randint(0, 2)

print(f"You chose: {options[user_input]}")
print(f"Computer chose: {options[computer_selection]}")

if computer_selection == 0:
    if user_input == 0:
        print('Tie')
    elif user_input == 1:
        print("You win!")
    else:
        print("You lost :(")
    
elif computer_selection == 1:
    if user_input == 0:
        print('You lost :(')
    elif user_input == 1:
        print("Tie")
    else:
        print("You win!")
    
else:
    if user_input == 0:
        print('You win!')
    elif user_input == 1:
        print("You lost :(")
    else:
        print("Tie")
    