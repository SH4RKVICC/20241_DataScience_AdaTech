import numpy as np

# Receba 10 valores, tranforme-os em array e realize operações (min, média, max, desvio padrao).

lista = [] # Criando lista vazia;

for i in range(10): # Criando fio de repetição de apelido i para receber valores;
    valor = float(input(f"Digite o {i+1}º valor: "))
    lista.append(valor)

array_valores = np.array(lista) # Transformando lista em array;

min = array_valores.min()
max = array_valores.max()
dp = array_valores.std()
m = array_valores.mean()
pm = array_valores.argmin()
up = array_valores.argmax()

print(f'Resultados!\nMinimo: {min}.\nMáximo: {max}.\nMédia: {m}.\nDesvio Padrão: {dp}.\nPosição Menor: {pm}.\nPosição Maior: {up}.')