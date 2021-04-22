# Sorteando uma ordem na lista
from random import shuffle
a = input("Primeiro aluno: ")
b = input("Segundo aluno: ")
c = input("Terceiro aluno: ")
d = input("Quarto aluno: ")
ordem = [a, b, c, d]
shuffle(ordem)
print(f"A ordem de apresentação será {ordem}")

