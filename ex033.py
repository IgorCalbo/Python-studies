# Maior e menor valores
a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))
# Menor valor
menor = a
if b < a and b < c:
    menor = b
elif c < a and c < b:
    menor = c
# Maior valor
maior = a
if b > a and b > c:
    maior = b
elif c > a and c > b:
    maior = c
print(f"O menor número digitado foi {menor} e o maior número digitado foi {maior}")