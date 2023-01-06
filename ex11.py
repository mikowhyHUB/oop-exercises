import time


time.sleep(2)


def timer(func):
    def wrapper(sec):
        start = time.time()
        func(sec)
        stop = time.time()
        print(f'execution time {stop - start:.4f}')
    return wrapper


def fake_sleep(sec):
    print(f'Executing {fake_sleep.__name__}...')
    time.sleep(sec)


timer(fake_sleep)(3)
