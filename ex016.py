# Quebrando um número
from math import trunc
num = float(input("Digite um valor: "))
print(f"O valor digitado foi {num} e a sua porção inteira é {trunc(num)}")

# sem usar a biblioteca math
num = float(input("Digite um valor: "))
print(f"O valor digitado foi {num} e a sua porção inteira é {int(num)}")