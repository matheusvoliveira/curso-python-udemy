def hello(name):
    print('The hello() function has been executed')
    def greet():
        print('greet() func')

    def welcome():
        print('welcome() func')

    if name == 'José':
        print(greet())
    else:
        print(welcome())
    print('this is the end of hello() func')

hello('José')


def new_decorator(original_func):
    def wrap_func():
        print('Some extra code, before the original function')
        original_func()
        print('Some extra code, after the original function')
    return wrap_func

new_decorator('cavapo)


def func_needs_decorator():
    print('I want to be decorated')


decorated_func = new_decorator(func_needs_decorator)

func_needs_decorator()

