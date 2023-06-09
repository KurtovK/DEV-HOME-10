import tkinter
from queue import PriorityQueu
#Задание 1.
#Создайте приложение используя очереди с приоритетом.
#Представим что нужно спроектировать список задач. У каждой задачи
#есть приоритет, это значит, что вначале должны быть самые приоритетные
#задачи. Сами задачи можно обрабатывать только по одной, мы не можем взять задачу с центра списка.
#При старте приложения отображается меню:
#a. Добавить новую задачу
#b. Выполнить текущую задачу
#c. Изменить приоритет задачи
class Task:
    def __init__(self, name: str, priority: int):
        self.name = name
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

def execute_application():
    pass
if __name__ == "__main__":
    execute_application()