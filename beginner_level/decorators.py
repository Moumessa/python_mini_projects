
def my_func(string):
    def wrapper():
        print('1')
        print(string)
        print(2)

    return wrapper

x = my_func('Yes')

print(x)