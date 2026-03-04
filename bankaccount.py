balance = 0.0

def show_balance():
    print("Current Balance:", balance)

def deposit(amount):
    global balance
    balance += amount
    print("Amount Deposited Successfully")

def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print("Withdrawal Successful")
    else:
        print("Insufficient Balance")

while True:
    print("\n1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    choice = int(input("Enter choice: "))

    if choice == 4:
        break
    elif choice == 1:
        show_balance()
    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        deposit(amount)
    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        withdraw(amount)
    else:
        print("Invalid choice")