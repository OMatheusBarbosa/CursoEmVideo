fltSalario = float(input('Informe o salário (R$): '))

if(fltSalario > 1250):
    fltSalario = fltSalario * 1.1

else:
    fltSalario = fltSalario * 1.15

print('O novo salário será de R${:.2f}' .format(fltSalario))
