# Jogo da Adivinhação v2.0
from random import randint
p = 0
acertou = False
computador = randint(0,10)
print("Acabei de pensar em um número entre 0 e 10, consegue adivinhar qual foi? ")
while acertou != True:
    jogador = int(input("Qual o seu palpite: "))
    p += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print("Menos... Tente mais uma vez")
        elif jogador < computador:
            print("Mais... Tente mais uma vez")    
print(f"Acertou com {p} tentativas. Parabéns!")
