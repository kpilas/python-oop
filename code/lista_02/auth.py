from authorization import authorizer
import authorization as auth
import time

authorizer.authenticator.add_user('Krystian', '12345678')
authorizer.authenticator.add_user('Anna', '1231255125')

authorizer.add_permission('testowanie')
authorizer.add_permission('modyfikacja')

authorizer.permit_user('Krystian', 'testowanie')
authorizer.permit_user('Anna', 'testowanie')
authorizer.permit_user('Anna', 'modyfikacja')


class Editor:
    def __init__(self):
        self.username = None
        self.options = {
            "a": self.login,
            "b": self.test,
            "c": self.change,
            "d": self.quit
        }

    def _is_permitted(self, username, perm):
        try:
            authorizer.check_permission(username, perm)
        except auth.NotLoggedError as err:
            print(err)
        except auth.PermissionError as err:
            print(err)
        except auth.NotPermittedError as err:
            print(err)
        else:
            return True

        return False

    def quit(self):
        quit()

    def test(self):
        if self._is_permitted(self.username, 'testowanie'):
            print('Testowanie...')
            time.sleep(5)

    def change(self):
        if self._is_permitted(self.username, 'modyfikacja'):
            print('Modyfikacja...')
            time.sleep(5)

    def login(self):
        try:
            username = input("Podaj nazwę użytkownika: ")
            authorizer.authenticator.login(username, input("Podaj hasło: "))
            self.username = username
        except auth.IncorrectUsername as err:
            print(err)
        except auth.IncorrectPassword as err:
            print(err)

    def run(self):
        while True:
            print('Wybierz opcję:')
            print('a - logowanie')
            print('b - wyświetlanie')
            print('c - modyfikacja')
            print('d - zakończ')

            try:
                op = input('Twój wybór: ')
                action = self.options[op]
            except KeyError:
                print('Błędna opcja')
            else:
                action()


Editor().run()
