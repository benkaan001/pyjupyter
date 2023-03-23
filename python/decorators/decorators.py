import functools

# add do twice
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


# add debug wrapper
def debug(func):
    """
    A decorator function that wraps around the given function and
    prints debug information before and after its execution.

    Usage:
    ------
    @debug
    def my_func(*args, **kwargs):
        # function body

    Parameters:
    -----------
    func : function
        The function to be decorated.

    Returns:
    --------
    wrapper_debug : function
        A new function that wraps around the given function and
        prints debug information before and after its execution.
    """
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


# add count calls

def count_calls(func):
    """
    A wrapper function that counts the number of times the decorated function is called.

    Args:
        func: A function to decorate.

    Returns:
        A decorated version of the input function that prints the number of times it has been called.

    Example usage:
    ```
    @count_calls
    def say_hello(name):
        print(f"Hello, {name}!")

    say_hello("Alice")  # prints "Call 1 of 'say_hello'"
    say_hello("Bob")    # prints "Call 2 of 'say_hello'"
    say_hello("Charlie")# prints "Call 3 of 'say_hello'"
    ```
    """
    @functools.wraps(func)
    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.num_calls += 1
        print(f"Call {wrapper_count_calls.num_calls} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper_count_calls.num_calls = 0
    return wrapper_count_calls