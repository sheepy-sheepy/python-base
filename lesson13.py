import time


def decorator_timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Конец исполнения: {end - start}")
        return result

    return wrapper


@decorator_timer
def load_file(seconds):
    print("Загружаю какой-то файл")
    time.sleep(seconds)


load_file(0.5)
load_file(1)


@decorator_timer
def multiply(a, b):
    print("Результат умножения")
    time.sleep(1)
    return a * b


print(multiply(3, 8))
