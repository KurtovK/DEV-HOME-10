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
    def is_empty(self):
        return self.head is None
def execute_application():
    pass
if __name__ == "__main__":
    executer_application()
