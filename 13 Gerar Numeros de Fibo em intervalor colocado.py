# Escreva um programa que pergunte ao usuário quantos números de Fibonacci gerar e os gere. Aproveite esta
# oportunidade para pensar sobre como você pode usar as funções. Certifique-se de pedir ao usuário para inserir o
# número de números na sequência a gerar. (Dica: a sequência de Fibonacci é uma sequência de números onde o próximo
# número na sequência é a soma dos dois números anteriores na sequência.
# A sequência se parece com isto: 1, 1, 2, 3, 5, 8, 13, ...)

def gen_fib():
    count = int(input("How many fibonacci numbers would you like to generate? "))
    i = 1
    if count == 0:
        fib = []
    elif count == 1:
        fib = [1]
    elif count == 2:
        fib = [1, 1]
    elif count > 2:
        fib = [1, 1]
        while i < (count - 1):
            fib.append(fib[i] + fib[i - 1])
            i += 1
    return fib

# Outra forma
def fibonacci():
    num = int(input("How many numbers that generates?:"))
    i = 1
    if num == 0:
        fib = []
    elif num == 1:
        fib = [1]
    elif num == 2:
        fib = [1,1]
    elif num > 2:
        fib = [1,1]
        while i < (num - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1
    return fib
print(fibonacci())
