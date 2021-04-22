v = int(input("Qual o valor a ser sacado? "))
total = v
ced = 50
total_ced = 0
while True:
	if v >= ced:
		v -= ced
		total_ced += 1
	else:
		print(f"total de {total_ced} cédulas de R${ced}")
		if ced == 50:
			ced = 20
		elif ced == 20:
			ced = 10
		elif ced == 10:
			ced = 1
		total_ced = 0
		if v == 0:
			break
