""""
Реализуйте архитектуру приложения, используя паттерн «Строитель».
Чтобы построить стандартный дом, нужно поставить 4 стены,
установить двери, вставить пару окон и постелить крышу. Но что, если вы
хотите дом побольше, посветлее, с бассейном, садом и прочим добром?
Паттерн предлагает разбить процесс конструирования объекта на
отдельные шаги (например, построить стены, вставить двери и т.д.) Чтобы
создать объект, вам нужно поочерёдно вызывать методы строителя. Причём
не нужно запускать все шаги, а только те, что нужны для производства
объекта определённой конфигурации.
"""
class House:
    def __init__(self):
        self.parts = []

    def add_part(self, part):
        self.parts.append(part)

    def list_parts(self):
        print(f"Дом состоит из: {', '.join(self.parts)}")

class HouseBuilder:
    def __init__(self):
        self.house = House()

    def build_walls(self):
        self.house.add_part("стены")

    def build_doors(self):
        self.house.add_part("двери")

    def build_windows(self):
        self.house.add_part("окна")

    def build_roof(self):
        self.house.add_part("крыша")

    def get_house(self):
        return self.house

class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct_house(self):
        self.builder.build_walls()
        self.builder.install_doors()
        self.builder.insert_windows()
        self.builder.lay_roof()
def execute_application():
    builder = HouseBuilder()
    director = Director(builder)

    # Строим дом
    director.construct_house()
    house = builder.get_house()

    # Выводим на экран список частей дома
    house.list_parts()
if __name__ == "__main__":
    execute_application()