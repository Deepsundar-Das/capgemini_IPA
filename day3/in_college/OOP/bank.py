class Bank:
    bank_name='SBI'
    loc='Haldia'
    ifsc='SBI00123433'
    reserved_money=8374892374
    def __init__(self, name, age, phone, pan, balance):
        self.name = name
        self.age = age
        self.phone = phone
        self.pan = pan
        self.balance = balance

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    def change_phone(self, new_phone : str) -> None:
        self.phone = new_phone

    def check_balance(self) -> int:
        return self.balance

    def withdraw_money(self, money:int) -> None:
        if money < 0:
            print("please give a valid amount")
        elif  self.balance < money :
            print("insufficient bank balance")
        else:
            print("transaction successful")
            self.balance = self.balance - money

c1 = Bank("deep",22, 9878997897, 'PANIN8778787', 1000)
c2 = Bank("arka",22, 9878787687, 'PANB98776567', 2000)
c3 = Bank("subhadip",23, 5464566576, 'PANI546545', 3000)

print(c1.name)
print(c2.bank_name)
print(c3.balance)
c1.withdraw_money(200)
print(c1.check_balance())
Bank.change_bank_name('furfuri-nagar state bank')
print(c1.bank_name)