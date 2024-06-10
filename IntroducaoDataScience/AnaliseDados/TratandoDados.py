# Importando a biblioteca pandas para manipulação de dados
import pandas as pd

# Importando o pacote openpyxl para permitir a leitura de arquivos Excel
#!pip install openpyxl

# Criando conexão com o arquivo Excel
df = pd.read_excel('São_paulo,xsls')

# Selecionando uma linha específica do DataFrame (linha com índice 100031)
auxiliar = df.loc[100031]

# Criando a função limpa_preco para limpar e formatar os valores na coluna 'price'
def limpa_preco(linha):
    linha['price'] = linha['price'].replace('R$', '')  # Remove o símbolo de Real
    linha['price'] = linha['price'].replace('\n', '')  # Remove quebras de linha
    linha['price'] = linha['price'].replace('/Mês ', '')  # Remove a indicação de preço mensal
    linha['price'] = linha['price'].replace('           ', '.')  # Substitui múltiplos espaços por um ponto
    linha['price'] = linha['price'].replace('/Ano ', '')  # Realizando desafio!
    return linha

# Aplicando a função limpa_preco em cada linha do DataFrame
df.apply(lambda x: limpa_preco(x), axis=1)  # axis=1 indica que a aplicação é feita por linha

# Criando a função ajusta_alugueis para ajustar os valores de aluguel na coluna 'price'
def ajusta_alugueis(linha):
    linha['price'] = linha['price'].replace('.', '')  # Remove pontos dos valores
    preco = int(linha['price'])  # Converte o valor para inteiro
    if '/Ano' in linha['price']:
        preco = preco / 12
    elif preco < 10000:  # Se o valor for menor que 10.000
        preco = preco * 200  # Multiplica o valor por 200
    linha['price'] = preco  # Atualiza o valor na coluna 'price'
    return linha

# Aplicando a função ajusta_alugueis na linha auxiliar
ajusta_alugueis(auxiliar)

# Aplicando a função ajusta_alugueis em cada linha do DataFrame
df.apply(lambda x: ajusta_alugueis(x), axis=1)

# Selecionando novamente a linha específica do DataFrame para verificar as alterações
auxiliar = df.loc[100031]
