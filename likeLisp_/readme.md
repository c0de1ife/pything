# python 再现 lisp 递归  

## 引言
总所周知，`lisp` 中的函数或运算符有递归性，如 `+` 运算符：  
```lisp
(+ 1 2 3 4 5)  ; 输出15
```

`python` 中能否实现类似写法呢？试写如下

## 函数改写
```python
def add(*args):
    length = len(args)
    if length > 2:
        return add(add(args[0], args[1]), *args[2:])
    if length == 2:
        return args[0] + args[1]
    if length == 1:
        return args[0]
    return add

print(add(1, 2, 3, 4, 5))  # 输出15
```
当然可以使用 `for` 循环，只是为了体现递归，故实现如上  
仔细想想，这样的确可以实现，但是每个需要递归的函数都需要重写。有没有更方便的方法呢，我们可以用包装函数（`python`中叫修饰器）来实现

## 包装函数
```python
def recursion(func):
    def f(*args):
        length = len(args)
        if length > 2:
            return f(func(args[0], args[1]), *args[2:])
        if length == 2:
            return func(args[0], args[1])

    return f
```
这样我们就可以传入现成的双参数函数，生成一个可以接受多个参数的相同意义的函数，如 `add` 运算
```python
def add(a, b):
        return a + b

recursion_add = recursion(add)
print(recursion_add(1, 2, 3, 4, 5))  # 输出15
```
再如 `sub`
```python
def sub(a, b):
        return a - b

recursion_sub = recursion(sub)
print(recursion_sub(50, 1, 2, 3, 4, 5))  # 输出35
```
扩展起来方便多了吧:)

## python 修饰器
`python` 中有修饰器的概念，可以更方便地实现这个功能（相当于语法糖），具体见于 [likelisp2.py](./likeLisp2.py)