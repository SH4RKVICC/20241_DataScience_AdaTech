import pandas as pd

# Criando Lista;
lista = [12, 23, 34, 45, 56, 67]

# Transformando em uma série no Pandas;
serie_pandas = pd.Series(lista)

# Mostrando o resultado;
print(serie_pandas)

# Mostrando posição do elemento;
print(serie_pandas[2])