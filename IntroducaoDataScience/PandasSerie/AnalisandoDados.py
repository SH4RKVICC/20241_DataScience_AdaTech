import pandas as pd

taxis = pd.read_csv('taxis.csv')

# Mostrando DataFrame de Elementos;
taxis.head()

taxis['dropoff_borough'].value_counts()

# Vizinhanças com casas mais caras dão melhores gorgetas?
taxis.groupby(['dropoff_borough'])['tip'].agg('mean', 'median') # Descobrindo Média e Mediana também!
