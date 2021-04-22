contador, total, produtoCaro, produtoBarato, nomeBarato = 0, 0, 0, 0, ''
while True:
	produto = input("Informe o nome do produto: ")
	preco = float(input("Informe o preço do produto: "))
	contador += 1
	total += preco
	if preco > 1000:
		produtoCaro += 1
	if contador == 1:
		produtoBarato = preco
	else:
		if preco < produtoBarato:
			produtoBarato = preco
			nomeBarato = produto
	escolha = input("Quer continuar[s/n]? ").lower()
	if escolha != "s":
		break
print(f"Total gasto na compra R${total} \n{produtoCaro} produtos custam mais de R$1000 \n{nomeBarato} é o produto mais barato, custando R${produtoBarato}")
