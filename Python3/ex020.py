import random

arrAlunos = []
intAlunos = int(input('Informe a quantidade de alunos: '))

for i in range(intAlunos):
    arrAlunos.append(input('Qual o nome do {}º aluno? ' .format(i + 1)))

random.shuffle(arrAlunos)

print('A ordem de apresentação será:')

for i in range(intAlunos):
    print('{}º - {}' .format(i + 1, arrAlunos[i]))
