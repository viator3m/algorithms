import time


def how_long(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(f'Время выполнения {func.__name__}: {time.time() - start_time}')
        return result
    return wrapper
