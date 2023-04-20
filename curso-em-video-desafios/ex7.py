def aluno(first_grade, second_grade, test):
    average_grade = (first_grade + second_grade + test) / 3
    print('A média entre {}, {}, e {} é {:.2f}'.format(first_grade, second_grade, test, average_grade))

aluno(8, 9.5, 7)
#test1