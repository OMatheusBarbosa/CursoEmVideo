strFrase = input('Digite uma frase: ').strip().upper()

print('A letra "A" aparece {} vezes' .format(strFrase.count('A')))
print('A letra "A" aparece pela primeira vez na {}ª posição' .format(strFrase.find('A') + 1))
print('A letra "A" aparece pela última vez na {}ª posição' .format(strFrase.rfind('A') + 1))
