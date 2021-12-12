import random

alun01 = str(input('Diga o nome do primeiro aluno: '))
alun02 = str(input('Diga o nome do segundo aluno: '))
alun03 = str(input('Diga o nome do terceiro aluno:'))
alun04 = str(input('Diga o nome do quarto aluno: '))
alun05 = str(input('Diga o nome do quinto aluno: '))

lista = [alun01, alun02, alun03, alun04, alun05]
escolhido = random.choice(lista)

print('O aluno escolhido foi {} '.format(escolhido))
