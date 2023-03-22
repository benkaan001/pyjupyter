def do_twice(func):
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice


# add updated version
def do_twice_updated(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice