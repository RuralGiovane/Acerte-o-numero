import os
os.system("cls")

import random
numero = random.randint(1,10)
resposta_correta = int(numero)
quantidade_de_chutes = 0
while True:
    chute = int(input("Digite um numero de 1 a 10, tente acertar qual numero foi selecionado: "))
    quantidade_de_chutes += 1
    if chute < resposta_correta:
        print("Você errou, o número é maior")
    elif chute > resposta_correta:
        print("Você errou, o número é menor")
    else:   
        chute == resposta_correta
        print("Parabens, você acertou o numero. O numero era:", numero)
        print(f"Você acertou o número em {quantidade_de_chutes} tentativas :)")
        break   