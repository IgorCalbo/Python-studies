# GAME: Pedra Papel e Tesoura
from random import randint
itens = ("PEDRA", "PAPEL", "TESOURA")
pc = randint(0,2)
print("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
jogada = int(input("Qual é a sua jogada: "))
print("-=" * 11)
print(f"Computador jogou {itens[pc]}")
print(f"Jogador jogou {itens[jogada]}")
print("-=" * 11)
if pc == 0: # computador jogou PEDRA
    if jogada == 0:
        print("EMPATE")
    elif jogada == 1:
        print("JOGADOR VENCE")
    elif jogada == 2:
        print("COMPUTADOR VENCE")
    else:
        print("Jogada inválida")
elif pc == 1: # computador jogou PAPEL
    if jogada == 0:
        print("COMPUTADOR VENCE")
    elif jogada == 1:
        print("EMPATE")
    elif jogada == 2:
        print("JOGADOR VENCE")
    else:
        print("Jogada inválida")
elif pc == 2: # computador jogou TESOURA 
    if jogada == 0:
        print("JOGADOR VENCE")
    elif jogada == 1:
        print("COMPUTADOR VENCE")
    elif jogada == 2:
        print("EMPATE")
    else:
        print("Jogada inválida")   