class ATM:
    def __init__(self):
        self.accounts = {}  

    def create_account(self, account_number, pin):
        if account_number in self.accounts:
            return False 
        self.accounts[account_number] = {"pin": pin, "balance": 0, "transactions": []}
        return True

    def authenticate(self, account_number, pin):
        account = self.accounts.get(account_number)
        if account and account["pin"] == pin:
            return True
        return False

    def deposit(self, account_number, amount):
        if amount <= 0:
            return False
        self.accounts[account_number]["balance"] += amount
        self.accounts[account_number]["transactions"].append(f"Deposited: ${amount}")
        return True

    def withdraw(self, account_number, amount):
        if 0 < amount <= self.accounts[account_number]["balance"]:
            self.accounts[account_number]["balance"] -= amount
            self.accounts[account_number]["transactions"].append(f"Withdrew: ${amount}")
            return True
        return False

    def check_balance(self, account_number):
        return self.accounts[account_number]["balance"]

    def transaction_history(self, account_number):
        return self.accounts[account_number]["transactions"]

    def run(self):
        while True:
            print("\nWelcome to the ATM")
            print("1. Create Account")
            print("2. Login")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                account_number = input("Enter a new account number: ")
                pin = input("Set a 4-digit PIN: ")
                if self.create_account(account_number, pin):
                    print("Account created successfully!")
                else:
                    print("Account already exists!")

            elif choice == "2":
                account_number = input("Enter your account number: ")
                pin = input("Enter your PIN: ")
                if self.authenticate(account_number, pin):
                    print("Login successful!")
                    self.account_menu(account_number)
                else:
                    print("Invalid account number or PIN.")

            elif choice == "3":
                print("Thank you for using the ATM. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

    def account_menu(self, account_number):
        while True:
            print("\nAccount Menu")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transaction History")
            print("5. Logout")
            choice = input("Choose an option: ")

            if choice == "1":
                balance = self.check_balance(account_number)
                print(f"Your balance is: ${balance}")

            elif choice == "2":
                amount = float(input("Enter the amount to deposit: "))
                if self.deposit(account_number, amount):
                    print("Deposit successful!")
                else:
                    print("Invalid amount.")

            elif choice == "3":
                amount = float(input("Enter the amount to withdraw: "))
                if self.withdraw(account_number, amount):
                    print("Withdrawal successful!")
                else:
                    print("Insufficient balance or invalid amount.")

            elif choice == "4":
                transactions = self.transaction_history(account_number)
                print("Transaction History:")
                if transactions:
                    for transaction in transactions:
                        print(transaction)
                else:
                    print("No transactions yet.")

            elif choice == "5":
                print("Logging out...")
                break

            else:
                print("Invalid choice. Please try again.")



if __name__ == "__main__":
    atm = ATM()
    atm.run()
