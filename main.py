from abc import ABC, abstractmethod
# Задание 1.
# Паттерн «Адаптер».
# Представьте, что у нас есть какая-то карта памяти. В чем состоит
# проблема? В том, что она не умеет взаимодействовать с компьютером. У них
# нет общего интерфейса. У компьютера есть разъем USB, но карту памяти в него
# не вставить. Карту невозможно вставить в компьютер, из-за чего мы не сможем
# сохранить наши фотографии, видео и другие данные. Кард ридер является
# адаптером, решающим данную проблему.
# Создайте абстрактный класс USB c методом connect_with_usb_cable()
# Создайте класс MemoryCard с методами insert() и copy_data()
# Реализуйте класс CardReader – наследник класса USB, который будет
# принимать в конструкторе объект класса MemoryCard и переопределять метод
# класса USB. В этом методе необходимо вызывать методы класса MemoryCard.
class USB(ABC):
    @abstractmethod
    def connect_with_usb_cable(self):
        pass
class MemoryCard:
    def __init__(self, data):
        self.data = data

    def insert(self):
        print("Карта памяти вставлена.")

    def copy_data(self):
        print(f"Данные ({self.data}) скопировано с карты памяти.")


class CardReader(USB):
    def __init__(self, memory_card):
        self.memory_card = memory_card

    def connect_with_usb_cable(self):
        self.memory_card.insert()
        self.memory_card.copy_data()
def execute_application():
    memory_card = MemoryCard("Мои фотографии")
    card_reader = CardReader(memory_card)
    card_reader.connect_with_usb_cable()


if __name__ == "__main__":
    execute_application()