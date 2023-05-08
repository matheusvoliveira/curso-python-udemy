try:
# try é o codigo que voce vai rodar, um codigo comum
    resulta = 10 + '10'
except:

# oque ira ser executado caso try esteja errado
# você pode especificar o erro que voce quer quer por exemplo
# except typeError, except: IndententionError
    print('erro')
    resulta = 10
finally:
#sempre ira ser executado
    print(resulta)

def ask_for_int():

    while True:
        try:
            result = int(input('Please provide a number: '))
        except:
            print(f' is not a number')
        else:
            print('Yes, thank you')
            break
        finally:
            print('Im going to ask you again')

ask_for_int()