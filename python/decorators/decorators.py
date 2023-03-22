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

import functools


# add debug wrapper
def debug(func):
    """ Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr =[repr(arg) for arg in args ] # create a list of positional args with tehir string representation using repr()
        kwargs_repr = [f"{k}={v!r}" for k,v in kwargs.items()] # do the same for kwargs
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")
        return value
    return wrapper_debug