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
class Strategy(ABC):
    @abstractmethod
    def calculate_route(self, start_point, end_point):
        pass


class StrategyDecorator(Strategy):
    def __init__(self, strategy):
        self._strategy = strategy

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
        self.strategy = strategy


def execute_application():
    walking_strategy = WalkingStrategy()
    driving_strategy = DrivingStrategy()
    public_transport_strategy = PublicTransportStrategy()

    decorated_driving_strategy = RouteLogger(driving_strategy)

    navigator = Navigator(decorated_driving_strategy)
    start_point = (55.753960, 37.620393)  # координаты Красной площади в Москве
    end_point = (55.715230, 37.552450)  # координаты парка Горького в Москве

    route = navigator.build_route(start_point, end_point)
    print(route)  # выводим массив точек маршрута


if __name__ == "__main__":
    execute_application()