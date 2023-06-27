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

class TransportFactory(ABC):
    @abstractmethod
    def create_transport(self):
        pass


class ElectricScooterFactory(TransportFactory):
    def create_transport(self):
        return ElectricScooter()


class BicycleFactory(TransportFactory):
    def create_transport(self):
        return Bicycle()


class CarFactory(TransportFactory):
    def create_transport(self):
        return Car()

def execute_application():
    # Создаем объект фабрики
    electric_scooter_factory = ElectricScooterFactory()
    bicycle_factory = BicycleFactory()
    car_factory = CarFactory()

    # Создаем объекты транспортных средств с помощью соответствующих фабрик
    electric_scooter = electric_scooter_factory.create_transport()
    bicycle = bicycle_factory.create_transport()
    car = car_factory.create_transport()

    # Используем методы объектов для получения информации о скорости и вместимости
    print(f"Скорость электросамоката: {electric_scooter.get_speed()} км/ч")
    print(f"Вместимость электросамоката: {electric_scooter.get_capacity()} единиц продукции")

    print(f"Скорость велосипеда: {bicycle.get_speed()} км/ч")
    print(f"Вместимость велосипеда: {bicycle.get_capacity()} единиц продукции")

    print(f"Скорость автомобиля: {car.get_speed()} км/ч")
    print(f"Вместимость автомобиля: {car.get_capacity()} единиц продукции")

if __name__ == "__main__":
    execute_application()