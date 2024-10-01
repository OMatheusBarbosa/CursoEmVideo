intDias = int(input('Informe a quantidade de dias alugados: '))
fltDistancia = float(input('Informe a distancia percorrida (Km): '))

fltVlr = (intDias * 60) + (fltDistancia * 0.15)

print('O total a pagar é R${:.2f}' .format(fltVlr))
