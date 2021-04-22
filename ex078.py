# Utilizando uma lista predefinida 
lista = [7, 4, 11, 9, 2]
maior = lista[1]
menor = lista[1]
for posicao, item in enumerate(lista):
    if item > maior:
        maior = item
        maiorPos = posicao
    if item < menor:
        menor = item
        menorPos = posicao
print(f"O maior número é {maior} e está na posição {maiorPos}")
print(f"O menor número é {menor} e está na posição {menorPos}")

# Utilizando uma lista  a partir do input do usuário
lista = []
for cont in range(0,5):
    lista.append(int(input("Digite um número: ")))
maior = lista[1]
menor = lista[1]
for posicao, item in enumerate(lista):
    if item > maior:
        maior = item
        maiorPos = posicao
    if item < menor:
        menor = item
        menorPos = posicao
print(f"O maior número é {maior} e está na posição {maiorPos}")
print(f"O menor número é {menor} e está na posição {menorPos}")
