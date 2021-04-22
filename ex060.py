# Cálculo do Fatorial
num = int(input("Digite um número para calcular seu fatorial: "))
fatorial = 1
if num < 0:
    print("Não existe fatorial para números negativos")
elif num == 0:
    print("O fatorial de 0 é 1")
else:
    for i in range(1, num+1):
        fatorial = fatorial*i
print(f"O fatorial do número {num} é {fatorial}")