lista = []
for i in range(0,5):
    n = int(input("Digite um número: "))
    if i == 0 or n > lista[-1]:
        lista.append(n)
        print("Adicionado ao final da lista")
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f"Adicionando na posição {pos} da lista")
                break
            pos += 1
print(lista)