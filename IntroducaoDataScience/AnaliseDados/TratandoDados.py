import pandas as pd
#!pip install openpyxl

# Criando conexão com o arquivo xsls;
df = pd.read_excel('São_paulo,xsls')

auxiliar = df.loc[100031]

#Criando Função limpa_preco;
def limpa_preco(linha):
    linha['price'] = linha['price'].replace('R$', '')
    linha['price'] = linha['price'].replace('\n', '')
    linha['price'] = linha['price'].replace('/Mês ', '')
    linha['price'] = linha['price'].replace('           ', '.')
    return linha

df.apply(lambda x: limpa_preco(x), axis=1) # axis=1 = eixo 1, vulgo linhas!

def ajusta_alugueis(linha):
    linha['price'] = linha['price'].replace('.', '')
    preco = int(linha['price'])
    if(int(linha['price'])) < 10000:
        preco = int(linha['price']) * 200
    linha['price'] = preco
    return linha

ajusta_alugueis(auxiliar)

df.apply(lambda x: ajusta_alugueis(x), axis=1)


auxiliar = df.loc[100031]