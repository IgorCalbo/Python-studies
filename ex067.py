n, c, d = 0, 0, 0
while True:
	n = int(input("Digite um número para ver sua tabuada: "))
	if n < 0:
		break
	for c in range(0,10,1):
		c += 1
		print(f"{n} x {c} = {n*c}")
	d += 1
print(f"Laço interrompido, total de {d} números digitados")