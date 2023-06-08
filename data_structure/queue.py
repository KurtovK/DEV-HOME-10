from data_structure.linkedList import LinkedList


class Queue:
    def __init__(self):
        self.__data = LinkedList()

    def enqueue(self, item):
        """ Добавление нового элемента item в очередь """
        self.__data.add_last(item)

    def dequeue(self):
        """ удаление и возврат очередного элемента в порядке «первым вошел, первым вышел» (FIFO) """
        return self.__data.remove_first()

    def peek(self):
        """ возврат(без удаления) очередного элемента в очереди в порядке FIFO """
        item = self.__data.remove_first()
        self.__data.add_first(item)
        return item

    def __len__(self):
        """ возврат количества элементов в очереди """
        return len(self.__data)

    def is_empty(self):
        """ ПРоверка очереди на пустоту """
        return len(self.__data) == 0