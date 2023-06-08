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

def execute_application():
    pass
if __name__ == "__main__":
    executer_application()
