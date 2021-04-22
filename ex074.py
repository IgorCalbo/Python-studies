from random import randint

# maior, menor = 0, 0

numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print(numeros)
print(f"O maior número gerado foi {max(numeros)}")
print(f"O menor númeo gerado foi {min(numeros)}")
