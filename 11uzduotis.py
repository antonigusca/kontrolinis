# Utwórz klasę Pythona o nazwie BankAccount z saldem atrybutów prywatnych.
# Wdrażaj metody wpłat i wypłat, aby zmodyfikować saldo.
# Upewnij się, że dostęp do salda nie jest możliwy bezpośrednio spoza zajęć.
# Utwórz instancję klasy BankAccount, wpłać część pieniędzy, wypłać część pieniędzy i wydrukuj pozostałe saldo.

class BankAccount:
    def __init__(self, acc_nr, balance):
        self.acc_nr = acc_nr
        self.balance = balance

    def show_balance(self, balance):
        print("Balance: ", balance)


    def __add_money(self, balance):
        money = input("Kiek nori pridet pinigu? ")
        balance +=money
        print(balance)
    def __withdraw_money(self, balance):
        money = input("Kiek nori paimt pinigu? ")
        balance += money
        print(balance)
