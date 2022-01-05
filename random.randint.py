# Printar um numero aleatório entre o intervalor colocado

import random

menor = int(input('Digite o menor valor:'))
maior = int(input('Digite o maior valor:'))
print(random.randint(menor, maior))
