fltVelocidade = float(input('Qual a velocidade do veículo (Km/h)? '))

if(fltVelocidade > 80):
    print('Você excedeu o limite de velocidade de 80Km/h')
    print('Uma multa foi gerada no valor de R${:.2f}' .format((fltVelocidade - 80) * 7))

else:
    print('Tenha um bom dia! Dirija com segurança!')
