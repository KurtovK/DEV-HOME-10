from data_structure.deque import Deque
from collections import deque

# Задание 1.
# Реализуйте структуру данных «Двусторонняя очередь» на основе
# связного списка (LinkedList)
# На ветке dev/class-10.2 в файле deque.py находится шаблон структуры.
# Протестируйте полученную структуру. Сравните работу своей
# структуры с встроенным классом deque модуля collections.
def execute_application():
    deq = Deque()
    deq.add_first(1)
    deq.add_first(2)
    deq.add_first(3)
    deq.add_first(4)
    print(deq)
    deq = deque()
    deq.appendleft("1")
    deq.appendleft("2")
    deq.appendleft("3")
    deq.appendleft("4")
    print(deq)
    deq = Deque()
    deq.add_last(1)
    deq.add_last(2)
    deq.add_last(3)
    deq.add_last(4)
    print(deq)
    deq = deque()
    deq.append(1)
    deq.append(2)
    deq.append(3)
    deq.append(4)
    print(deq)


if __name__ == '__main__':
    execute_application()