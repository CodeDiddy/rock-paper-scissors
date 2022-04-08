import random

choices = ['Rock', 'Paper', 'Scissors']
check = ("0","1","2")

def players_choice(choice = None):
    while choice not in check:
        choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
        if choice not in check:
            print("that is not a valid option")
        else:
            return choices[int(choice)]

def cpu_choice():
    return random.choice(choices)

def start_game():
    player = players_choice()
    print("You chose:", player)
    cpu = cpu_choice()
    print("Computer chose:", cpu)
    result(player, cpu)


def result(player, cpu):
    if player == 'Rock' and cpu == 'Paper':
        print("CPU wins")
    elif player == 'Rock' and cpu == 'Scissors':
        print("You win")
    elif player == 'Paper' and cpu == 'Rock':
        print("You win")
    elif player == 'Paper' and cpu == 'Scissors':
        print("CPU wins")
    elif player == 'Scissors' and cpu == 'Rock':
        print("CPU wins")
    elif player == 'Scissors' and cpu == 'Paper':
        print("You win")
    else:
        print("It's a draw, try again!")
        start_game() 
        
start_game()

