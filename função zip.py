lista1 = [1, 2, 3, 4, 5,5]
lista2 = ['abacete', 'oi', 'elefante','1','2','3']
lista3 = ['R$ 2,00', 'R$ 3,00', 'I','O','O','O','F']

for numero, nome, valor in zip(lista1, lista2, lista3):
    print(numero, nome, valor)