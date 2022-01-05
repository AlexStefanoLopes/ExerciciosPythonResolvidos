# a = int(input("Digite a:"))
# b = int(input("Digite b:"))
# c = int(input("Digite c:"))
# # Outra maneira
# # a=20
# # b=5
# # c=9
#
# def max_of_three(a, b, c):
#     max_3 = 0
#     if a > b:
#         # max_3=a
#         if a > c:
#             max_3 = a
#         else:
#             max_3 = c
#     else:
#         if b > c:
#             max_3 = b
#         else:
#             max_3 = c
#     return max_3
# print(max_of_three(a, b, c))
#
# # Outra maneira
# Outra solução é um pouco menos prolixa, pegando 3 números como entrada, transformando-os em uma lista,
# classificando-os e, em seguida, lendo o elemento maior. Esta última solução usa uma série mais compacta de
# comparações de instrução if para cobrir todos os casos de 3 elementos.
# !/usr/bin/env python
import sys

if len(sys.argv) < 4:
    print('Usage <value1> <value2> <value3>')
    sys.exit(1)

arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = sys.argv[3]

def maxfunction(a, b, c):
    if (a > b) and (a > c):
        print
        'Max value is :', a
    elif (b > a) and (b > c):
        print
        'Max value is :', b
    elif (c > a) and (c > b):
        print
        'Max value is :', c

maxfunction(arg1, arg2, arg3)