class Account:
    def __init__(self, name, balance):
        if balance < 0:
            raise ValueError('Saldo początkowe nie może być ujemne')
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError('Nie można wpłacić ujemnej kwoty.')
        self.balance += amount
        print(f'Wpłacono {amount}')

    def take(self, amount):
        if self.balance - amount < 0:
            raise ValueError('Brak środków na koncie.')
        self.balance -= amount

    def __str__(self):
        return f'Nazwa konta: {self.name}\nstan konta: {self.balance}'


my_account = None

while True:
    print('1 - załóż konto')
    print('2 - pokaż stan konta')
    print('3 - wpłać gotówkę')
    print('4 - wypłać gotówkę')
    print('5 - zakończ')
    try:
        op = int(input("Twój wybór: "))
        if op == 1:
            my_account = Account(input('Nazwa konta:'), float(input('Podaj saldo początkowe: ')))
        elif op == 2:
            if my_account:
                print(my_account)
            else:
                raise NameError('Nie ma takiego konta.')
        elif op == 3:
            if my_account:
                my_account.deposit(float(input('Podaj kwotę do wpłaty: ')))
            else:
                raise NameError('Nie ma takiego konta.')
        elif op == 4:
            if my_account:
                my_account.take(float(input('Podaj kwotę do wypłacenia: ')))
            else:
                raise NameError('Nie ma takiego konta.')
        elif op == 5:
            raise SystemExit
        else:
            print('Błędna opcja.')

    except ValueError as err:
        print(err)
    except NameError as err:
        print(err)
            
