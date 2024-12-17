class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self._password = password

    def set_password(self, new_password):
        self._password = new_password
        return 'Новый пароль: {}'.format(self._password)    
    
    def check_password(self, password):
        if password == self._password:
            return True
        return False
    
    def get_pass(self):
        return self._password

obj = UserAccount('Bin', 'Bin@gmail.com', 8642)
print(obj.set_password(123))
obj = UserAccount('Bin', 'Bin@gmail.com', 8642)
print(obj.check_password(123))

#прикол с приватным атрибутом
print(obj.email) #публичный работает
print(obj.get_pass()) #приватный через метод работает
print(obj._password) #просто приватный неочень
