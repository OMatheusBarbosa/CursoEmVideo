arrLados = []

for i in range(3):
    arrLados.append(float(input('Informe o tamanho do {}º lado: ' .format(i + 1))))

arrLados.sort()

if(arrLados[0] + arrLados[1] > arrLados[2]):
    print('Os lados acima podem formar um triângulo')

else:
    print('Os lados acima não podem formar um triângulo')
