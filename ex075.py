v1 = int(input("Digite o primeiro número: "))
v2 = int(input("Digite o segundo número: "))
v3 = int(input("Digite o terceiro número: "))
v4 = int(input("Digite o quarto número: "))

tupla = (v1, v2, v3, v4)
print(f"Você digitou os valores {tupla}")
print(f"O valor 9 apareceu {tupla.count(9)} vezes")
if 3 in tupla:
    print(f"O valor 3 apareceu na {tupla.index(3)}º posição")
else:
    print("O valor 3 não foi digitado em nenhuma posição")

print(f"Os valores pares digitados foram ", end="")
for item in tupla:
    if item % 2 == 0:
        print(item, end=" ")
   


# Fazendo o ultimo tópico com lista
# par = []
# for item in tupla:
#     if item % 2 == 0:
#         par.append(item)