import pandas as pd
import seaborn as sns # Para visualização de dados
import matplotlib.pyplot as plt

sns.get_dataset_names() # Retorna uma lista de conjuntos de dados disponíveis

iris = sns.load_dataset('iris') # Carrega o conjunto de dados iris

sns.pairplot(iris) # Cria um gráfico de dispersão para cada par de atributos e histogramas

sns.pairplot(iris, hue='species') # Cria um gráfico de dispersão para cada par de atributos e histogramas, separados por espécie