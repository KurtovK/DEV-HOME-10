import time
import datetime
import pytz

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Необходимое время: {end_time - start_time:.5f} секунд.")
        return result

    return wrapper


@timer
def get_primes(n):
    primes = []
    numbers = [True] * (n + 1)
    for i in range(2, n + 1):
        if numbers[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                numbers[j] = False
    return primes


@timer
def get_primes_range(start, end):
    primes = []
    numbers = [True] * (end + 1)
    for i in range(2, end + 1):
        if numbers[i]:
            if i >= start:
                primes.append(i)
            for j in range(i * i, end + 1, i):
                numbers[j] = False
    return primes


def time_decorator(func):
    def wrapper(*args, **kwargs):
        print("*" * 27)
        print(f"*** {func()} ***")
        return func(*args, **kwargs)

    return wrapper


@time_decorator
def get_current_time():
    tz = pytz.timezone('Europe/Moscow')
    now = datetime.datetime.now(tz)
    return now.strftime("%I:%M %p")


def execute_application():
    print(get_primes(1000))
    print(get_primes_range(50, 200))

    current_time = get_current_time()
    print("Текущее время:", current_time)


if __name__ == "__main__":
    execute_application()
