def recursion(func):
    """
    递归修饰器
    :param func: 含两个参数的函数
    :return: 可以输入多个参数的同意义函数
    """
    if func.__code__.co_argcount != 2:
        raise TypeError(
            f"recursion takes a function argument with 2 arguments "
            f"but get a function argument with {func.__code__.co_argcount} arguments")

    def f(*args):
        length = len(args)
        if length > 2:
            return f(func(args[0], args[1]), *args[2:])
        if length == 2:
            return func(args[0], args[1])

    return f


if __name__ == "__main__":
    @recursion
    def add(a, b):
        return a + b


    @recursion
    def sub(a, b):
        return a - b


    print(add(1, 2, 3, 4, 5))
    print(sub(50, 1, 2, 3, 4, 5))
