import logging 
logging.basicConfig(filename='Logs.log', level=logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info(f'Running "{func.__name__}" with arguments :{args}')
        print(func(*args))
    return log_func

def add(x, y):
    return x+y

def sub(x, y):
    return x-y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(6, 14)
sub_logger(19, 5)

add_logger(45, 23)
sub_logger(56, 44)