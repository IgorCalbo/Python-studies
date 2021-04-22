# Maior e Menor valores
media, soma, cont = 0, 0, 0
while True:
    n = int(input("Digite um número: "))
    resposta = input("Quer continuar[sim/nao]? ").strip().lower()
    if resposta == "sim":
        soma += n
    else:
        break
    maior = 0
    if n >= maior:
        maior = n
    menor = 1000
    if n <= menor:
        menor = n
    cont += 1
print(f"A média entre todos os valores é {soma/cont}, o maior valor digitado foi {maior} e o menor foi {menor}")