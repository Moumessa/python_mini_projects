import datetime

#=========== EXAMPLE N 1=================
#This is a basic example of a decorator

def my_func(f):
    """A basic example of a decorator 

    Args:
        f (function): the decorated function
    """
    def wrapper(*args, **kwargs):
        print('1')
        r = f(*args, **kwargs)
        print("2")

        return r

    return wrapper

@my_func
def func_2(x,y):
    print('Inside func 2 :', x, y)
    return x

@my_func
def func_3():
    print('Inside func 3')

a = func_2(3,6)
print('returned value of func_2 =', a)

#=========== EXAMPLE N 2=================
# The second example help track when a decorated function is called and with which arguments
# It saves that to a file called 'decorators_history_track.txt'
#

def log(f):
    """A decorator which can track when a decorated function is called and with which arguments
        It saves that to a file called 'decorators_history_track.txt'

    Args:
        f (function): the decoarated function
    """
    def wrapper(*args, **kwargs):
        # Track args and date of call, and save them to file
        with open("decorators_history_track.txt", "a") as ff:
            print("saving to file...")
            ff.write("\n Called the function with args : ("+" ".join([str(arg) for arg in args])+") at :"+ str(datetime.datetime.now()))
        
        # Call the decorated function and Get the result to a variabe called r
        r = f(*args, **kwargs)
        # return the result
        return r
    return wrapper

@log
def func(x,y):
    print("x+y=", x+y)

func(3,5)

#====== Example 4 ==========