import math

fltCO = float(input('Comprimento do cateto oposto: '))
fltCA = float(input('Comprimento do cateto adjacente: '))

fltHip = math.hypot(fltCO, fltCA)

print('A hipotenusa do triângulo é {:.2f}' .format(fltHip))
