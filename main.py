"""
Реализуйте архитектуру приложения, используя паттерн «Фабричный
метод».
Представьте, что вы создали программу управления доставкой еды. В
программе в качестве единственного средства доставки используется электросамокат.
Ваши курьеры на электро-самокатах развозят еду из пункта А в
пункт Б. Все просто.
Программа набирает популярность и ваш бизнес растет. Парк самокатов
ограничен и вы решаете подключить к вашей системе доставки велосипеды и
автомобили. Вам важно знать когда будет доставлена еда и сколько единиц
продуктов может забрать курьер. У транспортных средств разная скорость и
вместимость.
"""
from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def get_speed(self):
        pass

    @abstractmethod
    def get_capacity(self):
        pass

class ElectricScooter(Transport):
    def get_speed(self):
        return 20

    def get_capacity(self):
        return 1

class Bicycle(Transport):
    def get_speed(self):
        return 15

    def get_capacity(self):
        return 2

class Car(Transport):
    def get_speed(self):
        return 60

    def get_capacity(self):
        return 10

class TransportFactory:
    @staticmethod
    def create_transport(transport_type):
        if transport_type == "electric_scooter":
            return ElectricScooter()
        elif transport_type == "bicycle":
            return Bicycle()
        elif transport_type == "car":
            return Car()
        else:
            raise ValueError("Недопустимый тип транспорта")

def execute_application():
    # Создаем объект фабрики
    factory = TransportFactory()

    # Создаем объекты транспортных средств
    electric_scooter = factory.create_transport("electric_scooter")
    bicycle = factory.create_transport("bicycle")
    car = factory.create_transport("car")

    # Используем методы объектов для получения информации о скорости и вместимости
    print(f"Скорость электросамоката: {electric_scooter.get_speed()} км/ч")
    print(f"Вместимость электросамоката: {electric_scooter.get_capacity()} единиц продукции")

    print(f"Скорость велосипеда: {bicycle.get_speed()} км/ч")
    print(f"Вместимость велосипеда: {bicycle.get_capacity()} единиц продукции")

    print(f"Скорость автомобиля: {car.get_speed()} км/ч")
    print(f"Вместимость автомобиля: {car.get_capacity()} единиц продукции")
if __name__ == "__main__":
    execute_application()