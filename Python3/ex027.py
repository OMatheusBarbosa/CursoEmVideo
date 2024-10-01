strNome = input('Digite seu nome: ').strip()

arrNome = strNome.split(' ')

print('Seu primeiro nome é: {}' .format(arrNome[0]))
print('Seu último nome é:   {}' .format(arrNome[len(arrNome) - 1]))
