

# def outer_function(msg):
#     def inner_function():
#         print(msg)
#     return inner_function

# hi_func = outer_function('Hi')
# bye_func = outer_function('Bye')

# hi_func()
# bye_func()


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f'Wrapper executed this before {original_function.__name__}')
        return original_function(*args, **kwargs)
    return wrapper_function


class decorator_class(object):

    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f'call method executed this before {self.original_function.__name__}')
        return self.original_function(*args, **kwargs)


# Some Practical Examples

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename=f'{orig_func.__name__}.log', level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            f'Ran with args {args}, and kwargs {kwargs}'
        )
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f'{orig_func.__name__} ran in {t2} sec')
        return result

    return wrapper

# @decorator_class
# def display():
#     print('display function ran')

# import time

@my_timer
def display_info(name, age):
    # time.sleep(1)
    print(f'display_info ran with arguments ({name}, {age})')


# decorated_display = decorator_function(display)

# display()
display_info('harsh', 20)