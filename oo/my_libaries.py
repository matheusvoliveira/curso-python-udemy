import os
import shutil
import send2trash


f = open('pratice.txt', 'w+')
f.write('This is a test string')
f.close()
#cria um arquivo escreve ou manda algo pra dentro dele e depois fecha


os.getcwd()
print(os.listdir())
# lista todos os arquivos no seu repositorio atual

# shutil.move('pratice.txt', 'C:\\Users\\Matheus')
#manda um arquivo de um lugar para outro dentro do pc

send2trash.send2trash('C:\\Users\\Matheus\\pratice.txt')
#manda o arquivo pra lixeira


os.walk()
#cria pastas e encontra pasta/arquivos/subpastas em um projeto