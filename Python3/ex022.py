strNome = input('Digite seu nome completo: ').strip()

arrNome = strNome.split(' ')
strPriNome = arrNome[0]

print('Seu nome em maiúsculo: {}' .format(strNome.upper()))
print('Seu nome em minúsculo: {}' .format(strNome.lower()))
print('Seu nome ao todo tem {} letras' .format(len(strNome) - strNome.count(' ')))
print('Seu primeiro nome tem {} letras' .format(len(strPriNome)))
