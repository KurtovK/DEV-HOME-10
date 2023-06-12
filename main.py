from abc import ABC, abstractmethod


# Задание 1.
# Паттерн «Заместитель».
# Представьте себе дверь, которую можно открыть лишь картой доступа
# либо нажатием кнопки. Главная функциональность двери — это ее открытие,
# а заместитель, который добавлен поверх (кнопка, карт-ридер), отвечает за
# безопасность и расширяет функциональность.
# Создайте абстрактный класс Door с методами open() и close().
# Реализуйте наследника этого класса LaboratoryDoor, который реализует
# методы этого класса.
# Также у нас будет существовать заместитель Security, обеспечивающий
# защиту любых дверей.
# Реализуйте класс заместитель SecurityDoor, который в конструкторе
# принимает объект класса Door. Класс заместителя должен реализовывать те
# же методы, что и наследники класса Door. В методе open() необходимо
# выполнить аутентификацию. Аутентификацию реализовать отдельным
# методом, который принимает пароль и определяет, подходит он к двери или
# нет. Таким образом к оригинальной двери мы накладываем логику проверки
# доступа.
class Door(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass

class LaboratoryDoor(Door):
    def open(self):
        print("Двери лаборатории открыты")

    def close(self):
        print("Двери лаборатории закрыты")


class Security:
    def authenticate(self, password):
         if password == "123":
            return True
        else:
            return False


class SecurityDoor(Door):
    def __init__(self, door: Door, security: Security):
        self.door = door
        self.security = security

    def open(self):
        password = input("Введите пароль:")

        if self.security.authenticate(password):
            print("Пароль верный. Дверь открыта.")
            self.door.open()
        else:
            print("Пароль не верный. Доступ запрещен.")

    def close(self):
        self.door.close()


lab_door = LaboratoryDoor()

def execute_application():
    pass


if __name__ == "__main__":
    execute_application()