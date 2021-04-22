# Jogo da Adivinhação v.1.0
from random import randint
pc = randint(0,5)
num = int(input("Em que número eu pensei: "))
if num == pc:
    print("PARABENS! Você conseguiu me vencer!")
else:
    print(f"Você errou, eu pensei no número {pc}")