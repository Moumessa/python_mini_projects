
def my_func(f):
    """_summary_

    Args:
        f (_type_): _description_
    """
    def wrapper():
        print('1')
        f()
        print(2)

    return wrapper

def func_2():
    print('Inside func 2')

def func_3():
    print('Inside func 3')

x = my_func(func_2)
print(x)
x()

y = my_func(func_3)
print(y)
y()