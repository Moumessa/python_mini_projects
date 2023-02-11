def my_func(f):
    """_summary_

    Args:
        f (_type_): _description_
    """
    def wrapper(*args, **kwargs):
        print('1')
        r = f(*args, **kwargs)
        print(2)

        return r

    return wrapper

@my_func
def func_2(x,y):
    print('Inside func 2 :', x, y)
    return x

@my_func
def func_3():
    print('Inside func 3')

# func_2 = my_func(func_2)
a = func_2(3,6)
print('returned value of func_2 =', a)

# func_3 = my_func(func_3)
# func_3()