import pandas as pd

# Crie um dicionario com autores, preços, e titulos
d = { "Autores" : ['Rick Riordan', 'J. R. R Tolkien', 'Rick Riordan', 'Machado de Assis'],
     'Títulos' : ['A Batalha do Labirinto', 'A Sociedade do Anel', 'O Filho de Netuno', 'Memórias Postumas de Brás Cubas'],
     'Preços': [42.8, 35.7, 39.6, 40.5]}

# DataFrame;
df = pd.DataFrame(d)

# Mostrar Lista de Autores;
df['Autores']

# Mostrar Elemento da Posição 2;
df['Autores'][2]

# Ver Média dos Preços;
df['Preços'].mean()

# Buscar Elementos que Correspondem ao nome do autor;
mask = (df['Autores'] == 'Rick Riordan')

# Mostrar Resultado;
df[mask]

# Adicionando Novo Elemento;
df.append({'Autores': 'Rick Riordan', 'Título': 'A Piramide Vermelha', 'Preço': 40.2}, ignore_index = True)

# Chamar Elemento Especifico;
df.loc[mask]

# Mudando valor de uma coluna;
change = df['Preços'] == 40.2
df.loc[change, 'Preço'] == 40.4 