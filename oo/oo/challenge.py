class Account:
    def __init__(self, owner, balance):
        self._owner = owner
        self._balance = balance

    def deposit(self, add_money):
        self._balance = self._balance + add_money
        print(self._balance)


    def withdraw(self, withdraw_money):
        if withdraw_money > self._balance:
            print(f'The value of ${withdraw_money} is higher than the value in your account!')
        else:
            self._balance = self._balance - withdraw_money
            print(self._balance)

    def __str__(self):
        return f'{self._owner} has $ {self._balance} in his/her account'

a = Account('João', 100)
a.deposit(200)
a.withdraw(100)
print(a)



