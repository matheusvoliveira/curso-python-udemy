from math import sqrt
# try:
#     for i in ['a','b','c']:
#         print(i**2)
# except TypeError:
#     print(f'you cant use {type(i)} to make this calculation')


# try:
#     x = 5
#     y = 0
#
#     z = x / y
#
# except ZeroDivisionError:
#     print(f'you cant divide {x} by 0')
#
# finally:
#     print('all done!')

def ask():
    true_false = True
    while true_false:
        try:
            num = int(input("Insert an int: "))
        except:
            print('try again!')
        else:
            true_false = False
            print(sqrt(num))

ask()