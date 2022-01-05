# This one is 3x3 (like in tic tac toe).
# Obviously, they come in many other sizes
# (8x8 for chess, 19x19 for Go, and many more).

a = '---'.join('    ')
b = '   '.join('||||')
print('\n'.join((a, b, a, b, a, b, a)))
#
# def drawboard(kamal):
#     kamal = int(kamal)
#     i = 0
#     ho = "--- "
#     ve = "|   "
#     ho = ho * kamal
#     ve = ve * (kamal + 1)
#     while i < kamal + 1:
#         print
#         ho
#         if not (i == kamal):
#             print
#             ve
#         i += 1
