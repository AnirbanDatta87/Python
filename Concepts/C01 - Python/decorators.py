import time


def my_logger(original_func):
    import logging
    logging.basicConfig(
        filename=f'{original_func.__name__}.log', level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(f'Ran with args: {args} and kwargs: {kwargs}')
        return original_func(*args, **kwargs)

    return wrapper


def my_timer(original_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = original_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f'{original_func.__name__} ran in: {t2 :.4f} seconds.')
        return result

    return wrapper()

@my_timer
def display_info(name, age):
    time.sleep(1)
    print(f'display_info ran with arguments {name} and {age}.')


display_info('Anirban', 33)
