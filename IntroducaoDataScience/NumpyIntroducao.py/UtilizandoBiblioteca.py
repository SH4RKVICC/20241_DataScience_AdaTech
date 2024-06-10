import numpy as np

## Notas de Alunos;
lista_de_notas = [9.8, 5.6, 7.8, 9.1, 6.5] # Emitindo lista;

notas = np.array(lista_de_notas) #Transformando em Array

print(f"Máximo: {notas.max()}.\nMinimo: {notas.min()}.\nDesvio Padrão: {notas.std()}.\nMédia: {notas.mean()}.\nPosição Menor: {notas.argmin()}")