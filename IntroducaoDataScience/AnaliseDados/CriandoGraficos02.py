import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo CSV
df = pd.read_csv('netflix.csv')

# Remover a primeira coluna
df = df.drop(df.columns[0], axis=1)

# Preparar os dados para o gráfico
eixo_x = df['RELEASE_YEAR'].value_counts().sort_index().keys()
eixo_y = df['RELEASE_YEAR'].value_counts().sort_index().values

# Criar o gráfico de linha
plt.plot(eixo_x, eixo_y)

# Customizar o gráfico
plt.title('Melhores Filmes Por Ano de Lançamento')
plt.xlabel('Ano de Lançamento')
plt.ylabel('Quantidade de Filmes')

# Mostrar o gráfico
plt.show()
