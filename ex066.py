n, s, c = 0, 0, 0
while n != 999:
	n = int(input("Digite um número: "))
	if n == 999:
		break
	s += n
	c += 1
print(f"{c} números foram digitados e a soma entre eles é {s}")