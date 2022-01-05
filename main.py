import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "Seu Account"
# Your Auth Token from twilio.com/console
auth_token  = "Seu Token"
client = Client(account_sid, auth_token)

# Passo a passo de solução

# Abrir oos 6 arquivos em excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendedor'].values[0]
        qntvenda = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendas'].values[0]
        print(f'No mês: {mes}, Alguem bateu a META! Vendedor: {vendedor}, Vendas: {qntvenda}')
        message = client.messages.create(
            to="Numero para quem enviar",
            from_="Numero de quem vai enviar",
            body=f'No mês: {mes}, Alguem bateu a META! Vendedor: {vendedor}, Vendas: {qntvenda}')

        print(message.sid)


# Para cade arquivo:

# Verificar se algum valor na coluna vendas daquele arquivo é maior que 55 mil

# se for maior que 55 mil, enviar sms com nome, mes, vendas do vendedor

# Nao for maior que 55mil nao fazer nada