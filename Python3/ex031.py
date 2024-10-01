fltDistancia = float(input('Informe a distância da viagem (Km): '))

if(fltDistancia > 200):
    fltCusto = fltDistancia * 0.45

else:
    fltCusto = fltDistancia * 0.5

print('O preço da passagem será de R${:.2f}' .format(fltCusto))
