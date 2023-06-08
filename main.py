#Задание 1.
#Создайте класс очереди с приоритетами для работы с объектами
#определенного класса (реализуйте на своё усмотрение). Требуется создать
#реализации для операций над элементами очереди:
#is_empty — проверка очереди на пустоту.
#insert_with_priority—добавление элемента c приоритетом в очередь.
#pull_highest_priority_element—удаление элемента c высшим приоритетом из очереди.
#peek—возврат самого большого по приоритету элемента. Обращаем
#ваше внимание,что элемент не удаляется из очереди.
#show—отображение всех элементов очереди на экран. При показе
#элемента также необходимо отображать приоритет.
#При старте приложения нужно отобразить меню с помощью, которого
#пользователь может выбрать необходимую операцию.
class PriorityNode:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.head = None
#проверка очереди на пустоту
    def is_empty(self):
        return self.head is None
#добавление элемента c приоритетом в очередь
    def insert_with_priority(self, data, priority):
        new_node = PriorityNode(data, priority)
        if self.is_empty() or priority > self.head.priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None and priority <= current_node.next.priority:
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
#удаление элемента c высшим приоритетом из очереди
    def pull_highest_priority_element(self):
        if self.is_empty():
            print("Очередь пуста")
            return None
        data = self.head.data
        self.head = self.head.next
        return data
#возврат самого большого по приоритету элемента
    def peek(self):
        if self.is_empty():
            print("Очередь пуста")
            return None
        return self.head.data
# отображение всех элементов очереди на экран
    def show(self):
        if self.is_empty():
            print("Очередь пуста")
        else:
            current_node = self.head
            while current_node is not None:
                print(f"{current_node.data} (приоритет: {current_node.priority})")
                current_node = current_node.next

def execute_application():
    queue = PriorityQueue()

    while True:
        print("1. Добавить элемент с приоритетом")
        print("2. Удалить элемент с наибольшим приоритетом")
        print("3. Просмотреть элемент с наибольшим приоритетом")
        print("4. Проверить, пуста ли очередь")
        print("5. Показать все элементы очереди")
        print("6. Выход")
        choice = input("Выберите операцию: ")
        if choice == "1":
            data = input("Введите элемент: ")
            priority = int(input("Введите приоритет: "))
            queue.insert_with_priority(data, priority)
        elif choice == "2":
            data = queue.pull_highest_priority_element()
            if data is not None:
                print(f"Удален элемент {data}")
        elif choice == "3":
            data = queue.peek()
            if data is not None:
                print(f"Элемент с наибольшим приоритетом: {data}")
        elif choice == "4":
            if queue.is_empty():
                print("Очередь пуста")
            else:
                print("Очередь не пуста")
        elif choice == "5":
            queue.show()
        elif choice == "6":
            break
        else:
            print("Неверный выбор операции")

if __name__ == "__main__":
    execute_application()
