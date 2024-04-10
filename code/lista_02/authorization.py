import hashlib


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = self._encrypt_password(password)
        self.is_logged = False

    def _encrypt_password(self, password):
        hash_str = (self.username + password).encode('utf8')
        return hashlib.sha256(hash_str).hexdigest()

    def check_password(self, password):
        return self.password == self._encrypt_password(password)


u = User('krystian', '12345678')



class PermissionError(Exception): pass


class AuthenticException(Exception): pass


class IncorrectPassword(AuthenticException): pass


class IncorrectUsername(AuthenticException): pass


class NotLoggedError(AuthenticException): pass


class PasswordTooShort(AuthenticException): pass


class UsernameAlreadyExists(AuthenticException): pass


class NotPermittedError(AuthenticException): pass


class Authenticator:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        try:
            self.users[username]
        except KeyError:
            try:
                password[7]
                self.users[username] = User(username, password)
            except IndexError:
                raise PasswordTooShort('Hasło jest za krótkie!')
        else:
            raise UsernameAlreadyExists('Taki użytkownik już istnieje!')

    def login(self, username, password):
        try:
            user = self.users[username]
        except KeyError:
            raise IncorrectUsername(f'Nie ma konta o nazwie użytkownika: {username}')
        else:
            if not user.check_password(password):
                raise IncorrectPassword('Błędne hasło!')
            else:
                user.is_logged = True
                return True

    def is_logged_in(self, username):
        try:
            user = self.users[username]
        except KeyError:
            return False
        else:
            return user.is_logged


class Authorizer:
    def __init__(self, authenticator):
        self.permissions = {}
        self.authenticator = authenticator

    def add_permission(self, perm):
        try:
            self.permissions[perm]
        except KeyError:
            self.permissions[perm] = set()
        else:
            raise PermissionError('Takie uprawnienie już istnieje')

    def permit_user(self, username, perm):
        try:
            self.authenticator.users[username]
        except KeyError:
            raise IncorrectUsername(f'{username} - nie ma takiego użytkownika')
        else:
            try:
                set_users = self.permissions[perm]
            except KeyError:
                raise PermissionError('Takie uprawnienie nie istnieje')
            else:
                set_users.add(username)

    def check_permission(self, username, perm):
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedError(f'Użytkownik {username} nie jest zalogowany!')

        try:
            set_users = self.permissions[perm]
        except KeyError:
            raise PermissionError('Takie uprawnienie nie istnieje')
        else:
            if username not in set_users:
                raise NotPermittedError(f'Użytkownik {username} nie ma takiego uprawnienia')


authenticator = Authenticator()
authorizer = Authorizer(authenticator)
