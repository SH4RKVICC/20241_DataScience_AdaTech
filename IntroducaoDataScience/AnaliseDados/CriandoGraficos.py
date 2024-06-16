import pandas as pd
import matplotlib.pyplot as plt

# Carregar arquivo CSV;
df = pd.read_csv('netflix.csv')

# Remover a primeira coluna;
df = df.drop(df.columns[0], axis=1)

# Preparar os dados para o gráfico;
eixo_x = df['MAIN_GENRE'].value_counts().keys()
eixo_y = df['MAIN_GENRE'].value_counts().values

# Criar o gráfico de barras;
plt.bar(eixo_x, eixo_y)

# Customizar o gráfico;
plt.title('Filmes por Gênero')
plt.ylabel('Quantidade de Filmes')
plt.xticks(rotation=45)

# Mostrar gráfico;
plt.show()
