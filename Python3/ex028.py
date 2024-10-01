import random

intRndPC = random.randint(0, 5)
intRndUser = int(input('Adivinhe o número sorteado pelo computador entre 0 e 5: '))

if(intRndPC == intRndUser):
    print('Você acertou!!!')
else:
    print('Você errou!!! O numero sorteado foi {}' .format(intRndPC))
