from abc import ABC, abstractmethod
#Задание 1.
#Стратегия – это поведенческий паттерн проектирования, который
#определяет семейство схожих алгоритмов и помещает каждый из них в
#собственный класс, после чего алгоритмы можно взаимозаменять прямо во время исполнения программы.
#Вы решили написать приложение-навигатор для путешественников.
#Оно должно показывать красивую и удобную карту, позволяющую с лёгкостью ориентироваться в незнакомом городе.
#Одной из самых востребованных функций являлся поиск и
#прокладывание маршрутов. Пребывая в неизвестном ему городе, пользователь
#должен иметь возможность указать начальную точку и пункт назначения, а
#навигатор – проложит оптимальный путь.
#В этом примере каждый алгоритм поиска пути переедет в свой
#собственный класс. В этих классах будет определён лишь один метод,
#принимающий в параметрах координаты начала и конца пути, а
#возвращающий массив точек маршрута. Реализуйте класс навигатора,
#который по переданной ему стратегии выполняет построение маршрута.
from abc import ABC, abstractmethod
class Point:
    def __init__(self, point_x: int, point_y: int):
        self.__point_x = point_x
        self.__point_y = point_y

    def __str__(self):
        return f"{self.__point_x}, {self.__point_y}"


class Strategy(ABC):
    @abstractmethod
    def calculate_route(self, start_point, end_point):
        pass


class WalkingStrategy(Strategy):
    def calculate_route(self, start_point, end_point):
        # алгоритм поиска маршрута для пешехода
        pass


class DrivingStrategy(Strategy):
    def calculate_route(self, start_point, end_point):
        # алгоритм поиска маршрута для автомобилиста
        pass


class PublicTransportStrategy(Strategy):
    def calculate_route(self, start_point, end_point):
        # алгоритм поиска маршрута для использования общественного транспорта
        pass


class CyclingStrategy(Strategy):
    def calculate_route(self, start_point, end_point):
        # алгоритм поиска маршрута для велосипедистов
        pass


class MyCustomStrategy(Strategy):
    def calculate_route(self, start_point, end_point):
        # алгоритм поиска маршрута с учетом каких-то особых требований
        pass


class StrategyDecorator(Strategy):
    def __init__(self, strategy):
        self._strategy = strategy

    @abstractmethod
    def calculate_route(self, start_point, end_point):
        pass


class RouteLogger(StrategyDecorator):
    def __init__(self, strategy):
        super().__init__(strategy)

    def calculate_route(self, start_point, end_point):
        route = self._strategy.calculate_route(start_point, end_point)
        print(f"Маршрут построен: {route}")
        return route


class Navigator:
    def __init__(self, strategy):
        self.strategy = strategy

    def build_route(self, start_point, end_point):
        route = self.strategy.calculate_route(start_point, end_point)
        return route

    def set_strategy(self, strategy):
        if not isinstance(strategy, Strategy):
            raise TypeError("Стратегия должна быть объектом класса, наследующегося от Strategy.")
        self.strategy = strategy


class BaseStrategy(ABC):
    @abstractmethod
    def build_route(self, start_point: Point, finish_point: Point):
        raise NotImplementedError


class CarStrategy(BaseStrategy):
    def build_route(self, start_point: Point, finish_point: Point):
        return f"Маршрут построен из точки {start_point} в точку {finish_point}. Вид транспорта: автомобиль."


class PublicTransportStrategy2(BaseStrategy):
    def build_route(self, start_point: Point, finish_point: Point):
        return f"Маршрут построен из точки {start_point} в точку {finish_point}. Вид транспорта: городской транспорт."


class WalkingStrategy2(BaseStrategy):
    def build_route(self, start_point: Point, finish_point: Point):
        return f"Маршрут построен из точки {start_point} в точку {finish_point}. Вид транспорта: пешком."


class Navigator2:
    __strategy = BaseStrategy

    def set_strategy(self, strategy: BaseStrategy):
        self.__strategy = strategy

    def build_route(self, start_point: Point, finish_point: Point):
        return self.__strategy.build_route(start_point, finish_point)


def execute_application():
    walking_strategy = WalkingStrategy()
    driving_strategy = DrivingStrategy()
    public_transport_strategy = PublicTransportStrategy()
    cycling_strategy = CyclingStrategy()
    my_custom_strategy = MyCustomStrategy()

    decorated_driving_strategy = RouteLogger(driving_strategy)

    navigator = Navigator(decorated_driving_strategy)
    start_point = (55.753960, 37.620393)  # координаты Красной площади в Москве
    end_point = (55.715230, 37.552450)  # координаты парка Горького в Москве

    # Стратегия по умолчанию - RouteLogger
    route = navigator.build_route(start_point, end_point)
    print(route)  # выводим массив точек маршрута
    
    # Переключаем стратегию на WalkingStrategy
    navigator.set_strategy(walking_strategy)
    route = navigator.build_route(start_point, end_point)
    print(route)
    
    # Переключаем стратегию на MyCustomStrategy
    navigator.set_strategy(my_custom_strategy)
    route = navigator.build_route(start_point, end_point)
    print(route)
    
    # Пример использования второго набора классов
    navigator2 = Navigator2()
    start_point = Point(0, 0)
    finish_point = Point(10, 10)
    
    navigator2.set_strategy(CarStrategy())
    print(navigator2.build_route(start_point, finish_point))
    
    navigator2.set_strategy(WalkingStrategy2())
    print(navigator2.build_route(start_point, finish_point))
    
    navigator2.set_strategy(PublicTransportStrategy2())
    print(navigator2.build_route(start_point, finish_point))
if __name__ == "__main__":
    execute_application()
