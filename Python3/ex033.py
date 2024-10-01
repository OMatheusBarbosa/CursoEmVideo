arrNum = []

for i in range(3):
    arrNum.append(int(input('Informe o {}º número: ' .format(i + 1))))

arrNum.sort()

print('O maior valor é {}' .format(arrNum[0]))
print('O menor valor é {}' .format(arrNum[2]))
