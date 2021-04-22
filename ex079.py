lista = []
while True:
    n = int(input("Digite um número: "))
    if n in lista:
        print("Já existe esse valor dentro da lista, digite outro")
    else:
        lista.append(n)
        print("Valor adicionado com sucesso!")
    escolha = input("Deseja continuar[s/n]: ").lower()
    if escolha == "n":
        break
print(f"Você digitou os valores {sorted(lista)}")