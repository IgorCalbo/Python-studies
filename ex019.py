# Sorteando  um item na lista
from random import choice
a = input("Primeiro aluno: ")
b = input("Segundo aluno: ")
c = input("Terceiro aluno: ")
d = input("Quarto aluno: ")
print(f"O aluno escolhido foi {choice([a, b, c, d])}")