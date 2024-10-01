fltLargura = float(input('Largura da parede: '))
fltAltura = float(input('Altura da parede: '))

fltArea = fltLargura * fltAltura

print('Voce irá precisar de {:.1f}L de tinta para pintar uma parade com {:.2f}m2' .format(fltArea / 2, fltArea))
