# lisp + 运算符递归
def add(*args):
    length = len(args)
    if length > 2:
        return add(add(args[0], args[1]), *args[2:])
    if length == 2:
        return args[0] + args[1]
    if length == 1:
        return args[0]
    return add


if __name__ == "__main__":
    print(add(1, 2, 3, 4, 5))
