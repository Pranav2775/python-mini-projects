import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python Number guessing game")
print(f"select a number between {lowest_num} and {highest_num}")

while is_running:
    
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("out of range")
            print(f"select a number between {lowest_num} and {highest_num}")

        elif guess < answer:
            print("too low")
        elif guess > answer:
            print("too high")
        else:
            print(f"correct , the answer was {answer}")
            print(f"the no of guesses are {guesses}")
            is_running = False
    else:
        print("invalid guess")
        print(f"please select a number between {lowest_num} and {highest_num}")
