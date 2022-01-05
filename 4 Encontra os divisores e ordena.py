# Crie um programa que peça ao usuário um número e, em seguida, imprima uma lista de todos os divisores
# desse número. (Se você não sabe o que é um divisor, é um número que se divide igualmente em outro número.
#     Por exemplo, 13 é um divisor de 26 porque 26/13 não tem resto.)

numero = int(input('Digite um numero:'))

rangelista = list(range(1, numero + 1))

divisorlista = []

for nsequencial in rangelista:
    if numero % nsequencial == 0:
        divisorlista.append(nsequencial)

print(divisorlista)