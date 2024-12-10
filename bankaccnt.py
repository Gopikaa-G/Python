class BankAccount:
    def __init__(self,acc_no,name,acc_type,balance):
        self.account_number=acc_no
        self.name=name
        self.account_type=acc_type
        self.balance=balance
    def deposit(self,amount):
        if amount <=0:
            print("Deposite amount must be positive")
        else:
            self.balance+=amount
            print(f"Deposited:{amount}")
            print(f"Updated balance:{self.balance}")
    def withdraw(self,amount):
        if amount<=0:
            print("Withdrawal amount must be positive")
        elif self.balance<amount:
            print("Insufficent balance")
        else:
            self.balance-=amount
            print(f"Withdraw:{amount}")
            print(f"Updated balance:{self.balance}")
    def display(self):
        print("\nAccount details:")
        print(f"Account number:{self.account_number}")
        print(f"Account holder:{self.name}")
        print(f"Account type:{self.account_type}")
        print(f"Account balance:{self.balance}")
acc_no=int(input("Enter account number:"))
name=input("Enter account holder name:")
acc_type=input("Enter account type(savings/current):")
balance=int(input("Enter initial balance:"))
account=BankAccount(acc_no,name, acc_type, balance)
account.display()
deposit_amount=int(input("\nEnter the amount to deposit:"))
account.deposit(deposit_amount)
withdraw_amount=int(input("\nEnter the amount to withdraw:"))
account.withdraw(withdraw_amount)