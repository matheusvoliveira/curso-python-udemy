try:
# try é o codigo que voce vai rodar, um codigo comum
    resulta = 10 + '10'
except:

# oque ira ser executado caso try esteja errado
    print('erro')
    resulta = 10
finally:
#sempre ira ser executado
    print(resulta)

