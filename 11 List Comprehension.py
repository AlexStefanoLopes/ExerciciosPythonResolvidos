# e escreva um programa que retorne uma lista que contenha apenas os elementos que são comuns entre as listas
# (sem duplicatas). Certifique-se de que seu programa funcione em duas listas de tamanhos diferentes.
# Escreva usando pelo menos uma lista de compreensão. (Dica: lembre-se das compreensões de lista do Exercício 7).

import random
a = random.sample(range(1, 30), 12)
b = random.sample(range(1, 30), 16)
result = [i for i in a if i in b]
result.sort()
print(result, '\n')
#
import random
a = random.sample(range(1,30), 12)
b = random.sample(range(1,30), 16)
result = [i for i in set(a) if i in b]
result.sort()
print(result, '\n')

import random
a = random.sample(range(1,30), 12)
b = random.sample(range(1,30), 16)
result_overlap = [i for i in set(a) if i in b]
result = []
for element in result_overlap:
  if element not in result:
    result.append(element)
    result.sort()
    print(result, '\n')
#
import random
a = random.sample(range(1,30), 12)
b = random.sample(range(1,30), 16)
result_overlaps = [i for i in set(a) if i in b]
result = [i for i in result_overlaps if result_overlaps.count(i) == 1]
result.sort()
print(result, '\n')

# Python nos permite criar sets de várias formas. Uma das mais formas mais frequentemente usadas é criar um set
# a partir de uma lista de elementos.
#
# # Exemplo de criação de sets.
# numeros = [1, 2, 2, 3, 3, 3]
# numeros_distintos = set(numeros)
# print("Números: ", numeros)
# print("Números distintos: ", numeros_distintos)
# Números: [1, 2, 2, 3, 3, 3]
# Números distintos: {1, 2, 3}
# Outra forma de criarmos sets em Python é criar um conjunto vazio e inserir elementos nele à medida que desejarmos.
# Vejamos um exemplo.
#
# # Exemplo de criação de sets.
# numeros = [1, 2, 2, 3, 3, 3]
# numeros_distintos = set()
# for num in numeros:
#     numeros_distintos.add(num)
# print("Números: ", numeros)
# print("Números distintos: ", numeros_distintos)