import random

lista2 = []
def alunos(aluno1, aluno2, aluno3, aluno4):
    lista = [aluno1, aluno2, aluno3, aluno4]
    count = 0
    while len(lista) < 2:
        r = random.choice(lista)
        lista2.append(r)
        if alunos in lista2:
            lista2.pop(-1)
    print(lista2)





alunos('Matheus', 'Marcos', 'Lucas', 'João')