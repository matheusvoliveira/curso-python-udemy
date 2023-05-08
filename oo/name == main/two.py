import one

print('top level in two.py'.upper())

one.func()

if __name__ == '__main__':
    print('two.py is being run directly!'.upper())
else:
    print('two.py has been imported! '.upper())