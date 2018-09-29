from inspect import isfunction


def currying(f):
    """
    Currize a normal function
    :param f:
    :return:
    """
    if isfunction(f):
        f = (f, f.__code__.co_argcount, ())

    def wrapper_func(*args):
        args = f[2] + tuple(args)
        if len(args) >= f[1]:
            return f[0](*args)
        else:
            return currying((f[0], f[1], args))

    return wrapper_func


if __name__ == '__main__':
    plus = currying(lambda x, y: x + y)
    print(plus)
    print(plus(3))
    print(plus(3)(4))
