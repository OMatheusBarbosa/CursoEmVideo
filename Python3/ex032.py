intAno = int(input('Informe um ano: '))

bolBissexto = False

if(intAno % 400 == 0):
    bolBissexto = True

elif(intAno % 100 == 0):
    bolBissexto = False

elif(intAno % 4 == 0):
    bolBissexto = True

if(bolBissexto):
    print('O ano {} é bissexto' .format(intAno))

else:
    print('O ano {} não é bissexto' .format(intAno))
