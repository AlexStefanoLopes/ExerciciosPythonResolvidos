# Crie um programa que irá jogar o jogo “vacas e touros” com o usuário. O jogo
# funciona assim: Gere aleatoriamente um número de 4 dígitos. Peça ao usuário para adivinhar
# um número de 4 dígitos. Para cada dígito que o usuário
# adivinhou corretamente no lugar correto, eles têm uma "vaca"
# Para cada dígito que o usuário adivinhou corretamente no lugar errado é um "touro". Cada vez que o
# usuário adivinhar, diga quantas “vacas” e “touros” ele tem. Assim que o usuário adivinhar o número
# correto, o jogo termina. Acompanhe o número de suposições que o usuário faz durante o jogo e informe
# ao usuário no final.
# -1-4  para 2 bulls.. tem q tentar advinhar os outros
import random
def compare_numbers(number, user_guess):
    cowbull = [0,0] #cows, then bulls
    for i in range(len(number)):
        if number[i] == user_guess[i]:
            cowbull[1]+=1
        else:
            cowbull[0]+=1
    return cowbull

if __name__== "__main__":
    playing = True #gotta play the game
    number = str(random.randint(0,9999)) #random 4 digit number
    guesses = 0

    print("Let's play a game of Cowbull!") #explanation
    print("I will generate a number, and you have to guess the numbers one digit at a time.")
    print("For every number in the wrong place, you get a cow. For every one in the right place, you get a bull.")
    print("The game ends when you get 4 bulls!")
    print("Type exit at any prompt to exit.")

    while playing:
        user_guess = input("Give me your best guess!")
        if user_guess == "exit":
            break
        cowbullcount = compare_numbers(number,user_guess)
        guesses+=1

        print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

        if cowbullcount[1]==4:
            playing = False
            print("You win the game after " + str(guesses) + "! The number was "+str(number))
            break #redundant exit
        else:
            print("Your guess isn't quite right, try again.")