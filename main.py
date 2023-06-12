import time
#Задание 1.
#Создайте функцию, возвращающую список со всеми простыми числами
#от 0 до 1000. Используя механизм декораторов посчитайте сколько секунд,
#потребовалось для вычисления всех простых чисел. Отобразите на экран
#количество секунд и простые числа
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Необходимое время: {end_time - start_time:.5f} секунд")
        return result
    return wrapper

@timer
def get_primes(n):
    primes = []
    numbers = [True] * (n+1)   # инициализируем список чисел
    for i in range(2, n+1):
        if numbers[i]:
            primes.append(i)
            for j in range(i*i, n+1, i):   # вычеркиваем кратные
                numbers[j] = False
    return primes
#Задание 2.
#Добавьте к первому заданию возможность передавать границы
#диапазона для поиска всех простых чисел
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Необходимое время: {end_time - start_time:.5f} секунд")
        return result
    return wrapper

@timer
def get_primes(start, end):
    primes = []
    numbers = [True] * (end+1)   # инициализируем список чисел
    for i in range(2, end+1):
        if numbers[i]:
            if i >= start:
                primes.append(i)
            for j in range(i*i, end+1, i):   # вычеркиваем кратные
                numbers[j] = False
    return primes
def execute_application():
    print(get_primes(1000))


if __name__ == "__main__":
    execute_application()