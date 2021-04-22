# Maior e menor da sequência
lista = []
for i in range(1,6):
    peso = float(input(f"Peso da {i} pessoa: "))
    lista.append(peso)
print(f"O maior peso foi {max(lista)}Kg")
print(f"O menor peso foi {min(lista)}Kg")