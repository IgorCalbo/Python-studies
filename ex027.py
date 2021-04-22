# Primeiro e último nome de uma pessoa
n = input("Digite seu nome completo: ").strip()
nome = n.split()
print(f"O seu primeiro nome é {nome[0]}")
print(f"O seu ultimo nome é {nome[len(nome)-1]}")