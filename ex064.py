# Tratando vários valores v1.0
n = 7
c, soma = 0, 0
while n != 999:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    c += 1
    soma += n
print(f"{c} números foram digitados, e a soma deles é {soma}")