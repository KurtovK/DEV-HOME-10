
#Задание 1.
#Реализуйте класс очереди для работы с пользователями (каждому
#пользователю соответствует пара логин и пароль) на основе связного списка.
#Очередь должна иметь фиксированный размер (ограничение на количество
#элементов, которое можно задать при создании очереди).
#Реализуйте набор операций для работы с очередью:
# Добавление пользователя в очередь;
# Удаление и возврат пользователя из очереди;
# Подсчет количества пользователей в очереди;
# Проверку пустая ли очередь;
# Вывод всех пользователей из очереди на экран.
#При старте приложения нужно отобразить меню с помощью, которого
#пользователь может выбрать необходимую операцию.

class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, item):
        """Добавление нового элемента item в очередь"""
        self.data.append(item)

    def dequeue(self):
        """Удаление и возврат очередного элемента в порядке FIFO"""
        return self.data.pop(0)

    def peek(self):
        """Возврат (без удаления) очередного элемента в порядке FIFO"""
        return self.data[0]

    def __len__(self):
        """Возврат количества элементов в очереди"""
        return len(self.data)

    def is_empty(self):
        """Проверка очереди на пустоту"""
        return len(self.data) == 0

    def __iter__(self):
        """Возврат итератора по элементам очереди"""
        return iter(self.data)


class UsersQueue:
    def __init__(self, queue_length: int):
        self.queue = Queue()
        self.__max_length = queue_length

    def enqueue(self, user):
        """Добавление пользователя в очередь"""
        if len(self.queue) < self.__max_length:
            self.queue.enqueue(user)
        else:
            print(f"Очередь заполнена! Невозможно добавить пользователя {user}.")

    def dequeue(self):
        """Удаление и возврат пользователя из очереди"""
        if not self.queue.is_empty():
            return self.queue.dequeue()
        else:
            raise IndexError("Очередь пользователей пуста!")

    def count(self):
        """Подсчет количества пользователей в очереди"""
        return len(self.queue)

    def is_empty(self):
        """Проверка пустая ли очередь"""
        return self.queue.is_empty()

    def info(self):
        """Вывод всех пользователей из очереди на экран"""
        for user in self.queue:
            print(user)


class User:
    def __init__(self, login: str, password: str):
        self.login = login
        self.__password = password

    def __str__(self):
        return f"Логин: {self.login}; Пароль: {self.__password}"


def show_menu():
    menu = """
Выберите действие:
1 - Добавить пользователя в очередь
2 - Удалить и вернуть первого пользователя из очереди
3 - Количество пользователей в очереди
4 - Проверить пуста ли очередь
5 - Вывести всех пользователей из очереди на экран
0 - Закрыть программу
"""
    print(menu)


def execute_application():
    while True:
        try:
            queue_length = int(input("Введите максимальную длину очереди: "))
            user_queue = UsersQueue(queue_length)
            break
        except ValueError:
            print("Недопустимое количество мест, число должно быть целым!")

    while True:
        show_menu()
        main_action = input(">>> ")
        if main_action == "1":
            user = User(
                input("Введите логин пользователя: "),
                input("Введите пароль пользователя: ")
            )
            user_queue.enqueue(user)
            print(f"Пользователь {user} добавлен в очередь")
        elif main_action == "2":
            try:
                temp_user = user_queue.dequeue()
                print(f"Пользователь {temp_user} вышел из очереди")
            except IndexError as e:
                print(e)
        elif main_action == "3":
            print(f"В очереди {user_queue.count()} пользователей")
        elif main_action == "4":
            if user_queue.is_empty():
                print("Очередь пуста")
            else:
                print("В очереди есть пользователи")
        elif main_action == "5":
            if user_queue.is_empty():
                print("Очередь пуста")
            else:
                print("В очереди находятся следующие пользователи:")
                user_queue.info()
        elif main_action == "0":
            print("Завершение работы программы.")
            break
        else:
            print("Выбрано недопустимое действие")
if __name__ == "__main__":
    execute_application()
