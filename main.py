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
class MainWindow:
    MW_GEOMETRY = "400x400"

    def __init__(self):
        self.task_list = TaskList()

    def init(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Список дел")

        self.main_window.columnconfigure(index=0, weight=45)
        self.main_window.columnconfigure(index=1, weight=45)

        self.main_window.rowconfigure(index=0)

        self.actual_task = tkinter.StringVar()
        if not self.task_list.tasks.empty():
            self.actual_task.set(self.task_list.tasks.queue[0].name)

        self.task_label = tkinter.Label(self.main_window, textvariable=self.actual_task, font=("Arial", 16),
                                        width=40, height=10, borderwidth=3, relief="ridge")
        self.task_label.grid(row=0, columnspan=2, sticky="wens", pady=4, padx=4)

        self.change_btn = tkinter.Button(self.main_window, text="Изменить", font=("Arial", 16), command=self.change_priority)
        self.change_btn.grid(row=1, column=0, sticky="we", pady=8, padx=4)

        self.do_it_btn = tkinter.Button(self.main_window, text="Выполнить", font=("Arial", 16), command=self.execute_task)
        self.do_it_btn.grid(row=1, column=1, sticky="we", pady=8, padx=4)

        self.add_btn = tkinter.Button(self.main_window, text="Добавить", font=("Arial", 16), width=22, command=self.add_task)
        self.add_btn.grid(row=2, columnspan=2, pady=4, padx=4)

        self.empty_label = tkinter.Label(self.main_window, height=10)
        self.empty_label.grid(row=4, columnspan=2)
        self.quit_btn = tkinter.Button(self.main_window, text="Выход", font=("Arial", 16), width=22, command=self.main_window.quit)
        self.quit_btn.grid(row=5, columnspan=2)



def execute_application():
    pass
if __name__ == "__main__":
    execute_application()