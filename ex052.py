# Números primos
d = 0
num = int(input("Digite um número: "))
for c in range(1,num+1):
    if num % c == 0:
        d += 1
if num > 1 and d == 2:
    print(f"O número {num} foi divisível {d} vezes, por isso é primo")
else:
    print(f"O número {num} foi divisivel {d} vezes, por isso NÂO é primo")