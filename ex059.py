# Criando um Menu de Opções
sair = False
opcao = 0
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
while opcao != 5:
    print("[1]Somar \n[2]Multiplicar \n[3]Maior \n[4]Novos números \n[5]Sair")
    opcao = int(input("Qual sua opção: "))
    if opcao == 1:
        print(f"A soma dos números {n1} e {n2} é {n1+n2}")
    elif opcao == 2:
        print(f"A multiplicacao dos números {n1} e {n2} é {n1*n2}")
    elif opcao == 3:
        Maior = n1
        if n2 > n1:
            Maior = n2
            print(f"O maior número é {n2}")
        else:
            print(f"O maior número é {n1}")
    elif opcao == 4:
        n1 = int(input("Digite um novo número: "))
        n2 = int(input("Digite um novo segundo número: "))
    elif opcao == 5:
        print("Programa encerrado!")
    else:
        print("Opcão inválida. Tente novamemente")