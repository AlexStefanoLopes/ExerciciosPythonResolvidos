# Escreva um programa que pegue uma lista de números (por exemplo, a = [5, 10, 15, 20, 25]) e faça uma nova lista apenas
# do primeiro e do último elemento da lista fornecida. Para praticar, escreva este código dentro de uma função.

a = [5, 10, 15, 20, 25]

def primult(a):
    return [a[0], a[-1]]

Novalista = primult(a)
print(Novalista)

lista = [1,6,7]
lista = primult(lista)
print(lista)