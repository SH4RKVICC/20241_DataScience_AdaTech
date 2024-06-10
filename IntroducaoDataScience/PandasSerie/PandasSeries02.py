import pandas as pd

# Criando Notas;
notas = {'Vic': 4.7, 'Loren': 10.0, 'Gabriel': 2.8, 'Nat': 8.2, 'Vitor': 3.3}

# Criando Serie;
nota_serie = pd.Series(notas)

# Chamando Nota por Aluno;
print(nota_serie['Loren'])

# Calculando Média das Notas;
print(nota_serie.median())

# Pedindo Descrição;
print(nota_serie.describe())