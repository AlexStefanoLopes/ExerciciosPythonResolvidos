# Gere um número aleatório entre 1 e 9 (incluindo 1 e 9). Peça ao usuário para adivinhar
# o número e, em seguida, diga se ele adivinhou muito baixo, muito alto ou exatamente certo.
# (_Dica: lembre-se de usar as lições de entrada do usuário desde o primeiro exercício

import random
i = random.randint(0, 9)
numero = int(input('Adivinhe o numero:'))
total_de_tentativas = 10
for rodada in range(0, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
while numero != i:
    if numero > i:
        print('Numero maior')
        break
    else:
        print('Numero menor')
        break
else:
    print('Parabéns, vc acertou')
print('O numero segredo é:', i)

while numero != i:
    if numero !=i:
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('O jogo acabou')

 # Outra forma
import random
rd = random.randint(1, 9)
guess = 0
c = 0
while guess != rd and guess != "exit":
    guess = input("Enter a guess between 1 to 9")

    if guess == "exit":
        break

    guess = int(guess)
    c += 1

    if guess < rd:
        print("Too low")
    elif guess > rd:
        print("Too high")
    else:
        print("Right!")
        print("You took only", c, "tries!")
input()

# Outra forma
import random

# Awroken

MINIMUM = 1
MAXIMUM = 9
NUMBER = random.randint(MINIMUM, MAXIMUM)
GUESS = None
ANOTHER = None
TRY = 0
RUNNING = True

print("Alright...")

while RUNNING:
    GUESS = input("What is your lucky number? ")
    if int(GUESS) < NUMBER:
        print("Wrong, too low.")
    elif int(GUESS) > NUMBER:
        print ("Wrong, too high.")
    elif GUESS.lower() == "exit":
        print("Better luck next time.")
    elif int(GUESS) == NUMBER:
        print ("Yes, that's the one, %s." % str(NUMBER))
        if TRY < 2:
            print("Impressive, only %s tries." % str(TRY))
        elif TRY > 2 and TRY < 10:
            print("Pretty good, %s tries." % str(TRY))
        else:
            print("Bad, %s tries." % str(TRY))
        RUNNING = False
    TRY += 1