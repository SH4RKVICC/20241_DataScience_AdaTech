import numpy as np

# Lendo Notas;
notas = np.array([7.3, 4.2, 9.5, 8.0, 6.4])

# Criando Mascara Para Aprovado e em Recuperação;
a = (notas >= 5)
r = (notas < 5)

# Adicionando Rótulos;
rotulos = np.empty(notas.shape, dtype=object)
rotulos[a] = 'Aprovado!'
rotulos[r] = 'Em Recuperação!'

# Mostrando Resultados;
print(rotulos)
