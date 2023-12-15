import pandas as pd
from twilio.rest import Client
account_sid = "******.." # coloque a sid da sua conta twillio aqui
auth_token  = "******" #coloque seu token de autorização twillio aqui
client = Client(account_sid, auth_token)

# 3 coisas que para se instalar
# Pandas
# OpenPyxl
# Twilio
# O Pandas e o OpenPyxl é a para realizar a integração entre Python e Excel.
# O twilio é a integração do Python com SMS.

# Passo a Passo de solução
# Abrir os 6 arquivos em Excel
# Para cada arquivo:
# Verificar se algum valor na coluna vendas naquele arquivo é maior que 55.000
# Se for maior que 55.000 --> Envia um SMS com o Nome, Mês e as Vendas do vendedor
# Caso não seja maior que 55.000, não fazer nada.

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000  , 'Vendas'].values[0]
        print(f'No mês {mes} o vendedor {vendedor} realizou a meta no valor de {vendas} em vendas, confira!')
        message = client.messages.create(
    to= "+5535987****", # coloque seu numero aqui
    from_= "+12018****",# coloque o numero gerado pelo Twillio aqui
    body= f'No mês {mes} o vendedor {vendedor} realizou a meta no valor de {vendas} em vendas, confira!')
print(message.sid)
