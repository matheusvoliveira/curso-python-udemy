import random
class Password:
    def __init__(self):
        self.caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.0123456789"

    def randomy(self):
        list = []
        q = int(input('How many character would you like: '))
        for x in range(q):
            password = random.choice(self.caracteres)
            list.append(password)
        full_password = ''.join(list)
        return full_password

    def multiple_password(self):
        quantity = int(input('Quantity: '))
        all_passwords = []
        for x in range(quantity):
            all_passwords.append(self.randomy())
        for password in all_passwords:
            print(password)

    def __str__(self):
        return f'PASSWORDS: \n{self.multiple_password()}'

test = Password()
test.multiple_password()