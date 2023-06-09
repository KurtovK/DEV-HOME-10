"""
Реализуйте архитектуру приложения, используя паттерн
«Абстрактная фабрика»
Допустим, вы решили создать программу по производству и продаже
автомобилей. Автомобили будем создавать сами. Лучшим решением будет
скупить заводы известных компаний Ford и Toyota, и продолжить выпускать
автомобили под их собственными марками, а прибыль класть себе в
карман. Будем делать автомобили с 2 типами кузова – седан и купе. Например,
японцы будут делать ToyotaSedan и ToyotaCoupe, американцы — FordSedan и
FordCoupe». Таким образом, в вашем абстрактном классе CarsFactory будут 2
метода: createSedan() и createCoupe(). Реализуйте программу и протестируйте
фабрику на примерах создания конкретных автомобилей.
"""
from abc import ABC, abstractmethod

class CarsFactory(ABC):
    @abstractmethod
    def create_sedan(self):
        pass

    @abstractmethod
    def create_coupe(self):
        pass


class FordSedan:
    def __init__(self):
        self.name = "Ford Sedan"


class FordCoupe:
    def __init__(self):
        self.name = "Ford Coupe"


class FordFactory(CarsFactory):
    def create_sedan(self):
        return FordSedan()

    def create_coupe(self):
        return FordCoupe()


class ToyotaSedan:
    def __init__(self):
        self.name = "Toyota Sedan"


class ToyotaCoupe:
    def __init__(self):
        self.name = "Toyota Coupe"


class ToyotaFactory(CarsFactory):
    def create_sedan(self):
        return ToyotaSedan()

    def create_coupe(self):
        return ToyotaCoupe()
def execute_application():
    cars_factory = FordFactory()
    sedan = cars_factory.create_sedan()
    coupe = cars_factory.create_coupe()

    print(sedan.name)
    print(coupe.name)


    cars_factory = ToyotaFactory()
    sedan = cars_factory.create_sedan()
    coupe = cars_factory.create_coupe()

    print(sedan.name)
    print(coupe.name)
if __name__ == "__main__":
    execute_application()