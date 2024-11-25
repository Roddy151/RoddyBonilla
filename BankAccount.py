class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

    def desposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Se han depositado {amount} en su cuenta y su nuevo balance es de {self.balance}")
        else:
            print("No se puede depositar, cuenta inactiva")
    
    def withdraw(self, amount):
        if self.is_active:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Se ha rertirado {amount}. Su saldo actual es de {self.balance}")
            else:
                print(f"Su saldo es menor a su saldo actual. Saldo actual {self.balance}")
        else:
            print("No se puede retirar dinero. Su cuenta está desactivada")

    def deactive_account(self):
        self.is_active=False
        print("La cuenta ha sido desactivada")
    def active_account(self):
        self.is_active=True
        print("La cuenta ha sido activada")

account1 = BankAccount("Anissa", 20000)
account2 = BankAccount("Anlly", 100000)

#Llamar a los metodos:
account1.desposit(25000)
account2.withdraw(25000)
account1.deactive_account()
account1.withdraw(10000)
account2.desposit(10000)
account1.active_account()
account1.desposit(50000)