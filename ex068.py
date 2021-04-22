import random
n, pc, s, v = 0, 0, 0, 0
while True:
	n = int(input("Digite um número: "))
	pc = random.randint(0, 50)
	escolha = input("Você escolhe par ou impar? ").strip().lower()
	if escolha == "par":
		epc = "impar"
	elif escolha == "impar":
		epc = "par"
	else:
		print("Escolha inválida")
		break
	s = n + pc
	if s % 2 == 0 and escolha =="par":
		print(f"Você jogou {n} e o computador jogou {pc}, deu par. Você venceu!")
	else:
		print(f"Você jogou {n} e o computador jogou {pc}, deu ímpar. Você perdeu!")
		break
	v += 1
print(f"Seu total de vitórias foi de {v}")