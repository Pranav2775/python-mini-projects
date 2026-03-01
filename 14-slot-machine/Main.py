# python slot machine
import sys
sys.stdout.reconfigure(encoding='utf-8')
import random

def spin_row():
    
    symbol = ['🍒', '🍋' ,'🍉' ,'🔔', '⭐']

    return [random.choice(symbol) for _ in range(3)]

def print_row(row):
    print("**************")
    print(" | ".join(row))
    print("**************")

def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🍉":
            return bet * 10
        elif row[0] == "🔔":
            return bet * 20
        elif row[0] == "⭐":
            return bet * 100
    else:
        return 0
    
def main():
    balance = 100

    print("******************************")
    print("welcome to python slot machine")
    print("symbols  :  🍒 🍋 🍉 🔔 ⭐ ")
    print("******************************")
    print()

    while balance > 0:
        print(f"current balance : ${balance}")

        bet = input("place your bet : $")

        if not bet.isdigit():
            print("invalid bet")
            continue

        bet = int(bet)

        if bet > balance:
            print("insufficent balance")
            continue

        if bet <= 0:
            print("bet should be greater than 0")
            continue
    
        balance -= bet

        row = spin_row()
        print("spinning................\n")
        print_row(row)

        payout = get_payout(row,bet)

        if payout > 0:
            print(f"you won : ${payout}")
        else:
            print("you lost this round")

        balance += payout

        play_again = input("Do you like to play again (Y/N) : ").upper()

        if play_again != "Y":
            break

    print(f"Game Over ! your final balance is : ${balance}")

if __name__ == '__main__':
    main()
