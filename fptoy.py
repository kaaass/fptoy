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


# Church zero
zero = currying(lambda s, z: z)


def church(n: int):
    """
    Convert integer to church number
    :param n:
    :return:
    """
    if n < 1:
        return zero
    return currying(lambda s, z: s(church(n - 1)(s)(z)))


def dechurch(c) -> int:
    """
    Convert church number to integer
    :param c:
    :return:
    """
    return c(lambda x: x + 1, 0)


"""
Church operation plus
"""
plus = currying(lambda a, b, s, z: a(s)(b(s)(z)))

"""
Church operation multiply
"""
multiply = currying(lambda a, b, s, z: a(b(s))(z))

"""
ω combinator
"""
omega = lambda x: x(x)

"""
Ω combinator
"""
Omega = lambda x: omega(omega(x))

"""
Y combinator
"""
Y = lambda f: (lambda x: f(x(x)))((lambda x: f(lambda *args: x(x)(*args))))

if __name__ == '__main__':
    num_plus = currying(lambda x, y: x + y)
    print(num_plus)
    print(num_plus(3))
    print(num_plus(3)(4))

    three = church(3)
    five = church(5)
    print(three)
    print(dechurch(five))
    print(dechurch(plus(three, five)))
    print(dechurch(multiply(three, five)))

    fibonacii = Y(lambda f: lambda n: 1 if n <= 1 else f(n - 1) + f(n - 2))
    print(fibonacii(12))
