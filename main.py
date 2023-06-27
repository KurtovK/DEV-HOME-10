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
def execute_application():
    pass
if __name__ == "__main__":
    execute_application()