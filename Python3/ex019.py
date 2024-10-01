import random

arrAlunos = []
intAlunos = int(input('Informe a quantidade de alunos: '))

for i in range(intAlunos):
    arrAlunos.append(input('Qual o nome do {}º aluno? ' .format(i + 1)))

print('O {} foi sorteado! Parabéns!' .format(random.choice(arrAlunos)))
