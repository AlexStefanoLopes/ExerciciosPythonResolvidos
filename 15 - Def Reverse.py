# Escreva um programa (usando funções!) Que peça ao usuário uma longa string contendo várias
# palavras. Imprime de volta para o usuário a mesma string, exceto com as palavras na ordem
# inversa. Por exemplo, digamos que eu digite a string:
#  My name is Michele
# Then I would see the string:
#
#   Michele is name My
# shown back to me.
# Exemplo - >>> a = '1234' >>> a [:: - 1] '4321' Em seguida, você converte para int e depois de volta para
# string (embora não tenha certeza de por que você faz isso), isso apenas lhe devolve a string.

a = '1234'
print(a[::3],'\n')

a = '1234'
print(a[::-1],'\n')

a = '1234'
print(a[3:0:-1],'\n')

txt1 = ['Alex', 'Stefano', 'Lopes'][::-1]
print(txt1)
#
def inverter():
    txt2 = ['Alex', 'Stefano', 'Lopes']
    return txt2[::-1]

def reverse_v1(x):
    y = x.split()
    result = []
    for word in y:
        result.insert(0, word)
    return "".join(result)

# # method 2
def reverse_v2(x):
    y = x.split()
    return " ".join(y[::-1])

# #
# # method 3
def reverse_v3(x):
    y = x.split()
    return " ".join(reversed(y))

# # method 4
def reverse_v4(x):
    y = x.split()
    y.reverse()
    return " ".join(y)

# test code
test1 = input("Enter a sentence: ")
print(reverse_v1(test1))
print(reverse_v2(test1))
print(reverse_v3(test1))
print(reverse_v4(test1))