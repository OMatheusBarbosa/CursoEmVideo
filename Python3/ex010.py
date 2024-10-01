import requests
from datetime import date

fltReais = float(input('Informe quanto dinheiro possui (R$):'))

jsCotacao = requests.get("https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{}'&$top=1&$format=json" .format(date.today().strftime('%m-%d-%Y'))).json()

fltCotDolar = float(jsCotacao['value'][0]['cotacaoCompra'])

print('Com R${:.2f}, conseguirá comprar US${:.2f}' .format(fltReais, fltReais / fltCotDolar))
