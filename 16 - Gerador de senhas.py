# # generate a password with length "passlen" with no duplicate characters in the password
#
# import random
#
# s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
# passlen = 20
# p =  "-".join(random.sample(s,passlen))
# print(p)

import string
import random

def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))

print(pw_gen(int(input('How many characters in your password?'))))
# OBS: Ou seja, size = 8 neste caso, significa que terei 8 de string.ascii_letters, 8 de string.digits, etc...de forma
# aleatória
# Já o in range(size) é para o tamanho total do pw que quero