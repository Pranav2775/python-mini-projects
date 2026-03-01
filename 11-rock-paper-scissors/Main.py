import random

options = ("rock","paper","scissor")

running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("enter your choice (rock, paper , scissors) : ")

    print(f"player : {player}")
    print(f"computer : {computer}")

    if player == computer:
        print("its a tie")
    elif player == "rock" and computer == "scissor":
        print("You Win")
    elif player == "scissor" and computer == "paper":
        print("You Win")
    elif player == "paper" and computer == "rock":
        print("You Win")
    else:
        print("You Lose")

    play_again = input("play again (y/n) ? : ").lower()
    if not play_again == "y":
        running = False

print("thanks for playing")