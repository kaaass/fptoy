from functools import partial


def currying(f):
    """
    Currize a normal function
    :param f:
    :return:
    """
    if isinstance(f, partial):
        # noinspection PyUnresolvedReferences
        arg_count = f.func.__code__.co_argcount
    else:
        arg_count = f.__code__.co_argcount

    def wrapper_func(x):
        func = partial(f, x)
        if len(func.args) == arg_count:
            return func()
        else:
            return currying(func)

    return wrapper_func


if __name__ == '__main__':
    plus = currying(lambda x, y: x + y)
    print(plus)
    print(plus(3))
    print(plus(3)(4))
