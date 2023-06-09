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

class TaskList:
    def __init__(self):
        self.tasks = PriorityQueue()

    def add_task(self, name: str, priority: int):
        task = Task(name, priority)
        self.tasks.put(task)

    def execute_task(self):
        if not self.tasks.empty():
            task = self.tasks.get()
            print(f"Выполняется задача {task.name} с приоритетом {task.priority}")
        else:
            print("Список задач пуст")

    def change_priority(self, task_name: str, new_priority: int):
        tasks_list = list(self.tasks.queue)
        for i in range(len(tasks_list)):
            if tasks_list[i].name == task_name:
                tasks_list[i].priority = new_priority
                self.tasks = PriorityQueue()
                for task in tasks_list:
                    self.tasks.put(task)
                print(f"Приоритет задачи {task_name} изменен на {new_priority}")
                return
        print(f"Задача {task_name} не найдена в списке")
def execute_application():
    pass
if __name__ == "__main__":
    execute_application()