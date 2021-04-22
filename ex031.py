# Custo da Viagem
dist = int(input("Qual a distância da viagem: "))
if dist <= 200:
    preco = 0.50
    print(f"O preço de uma viagem de {dist:.1f}km é R${dist*preco:.2f}.")
else:
    preco = 0.45
    print(f"O preço de uma viagem de {dist:.1f}km é R${dist*preco:.2f}.")