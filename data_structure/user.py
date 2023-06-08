class User:
    def __init__(self, login: str, password: str):
        self.__login = login
        self.__password = password

    def __str__(self):
        return f" Логин: {self.__login}; Пароль: {self.__password}"