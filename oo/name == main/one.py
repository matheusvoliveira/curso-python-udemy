def func():
    print('func() in one.py'.upper())

print('top level in one.py'.upper())

if __name__ == '__main__': #se __name__ == '__main__' significa que o arquivo ta rodando em primeiro plano e não foi importado
    print('one.py is being run directly!'.upper())
else:
    print('one.py has been impported!'.upper())

