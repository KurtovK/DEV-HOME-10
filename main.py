from data_structure.queue import UsersQueue
from user import User
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

def execute_application():
    while True:
        try:
            queue_lenght = int(input("Введите количество мест в очереди: "))
            user_queue = UsersQueue(queue_lenght)
            break
        except ValueError:
            print("Недопустимым количество мест,число должно быть целым!")

    while True:
        show_menu()
        main_action = input(" >>> ")
        if main_action == "1":
            user = User(
                input("Введите логин пользователя: "),
                input("Введите пароль пользователя: ")
            )
            user_queue.enqueue(user)
            print(f"Пользователь {user} в очередь")
        elif main_action == "2":
            try:
                temp_user = user_queue.dequeue()
                print(f"Пользователь {temp_user} вышел из очереди")
            except IndexError as e:
                print(e)
        elif main_action == "3":
            print(f"В очереди {len(user_queue)} пользователей")
        elif main_action == "4":
            if user_queue.is_empty():
                print("Очередь пуста")
            else:
                print("В очереди есть пользователи")
        elif main_action == "5":
            if user_queue.is_empty():
                print("Очередь пуста")
            else:
                print("в очереди находятся следующие пользователи:")
                user_queue.info()
        elif main_action == "0":
            print("Завершение работы программы.")
            break
        else:
            print("Выбрано недопустимое действие! Повторите ввод.")


if __name__ == '__main__':
    execute_application()