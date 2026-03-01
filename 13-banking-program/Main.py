# Banking program

def show_balance(balance):
    print(f"your total balance is ${balance:.2f}")

def deposit():
    amount = float(input("enter the amount u like to deposit : "))
    if amount < 0:
        print("invalid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("enter the amount you want to withdraw : "))
    if amount < 0:
        print("amount should be greater than 0")
        return 0
    elif amount > balance:
        print("insufficent funds")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("1.show balance")
        print("2.deposit")
        print("3.withdraw")
        print("4.exit")

        choice = input("enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)

        elif choice == '2':
            balance += deposit()

        elif choice == '3':
            balance -= withdraw(balance)

        elif choice == '4':
            is_running = False

        else:
            print("not valid")

    print("thank you have a nice day")

if __name__ == '__main__':
    main()