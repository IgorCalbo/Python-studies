# Separando dígitos de um número
nome = input("Digite seu nome completo: ")
print(f"O nome com todas letras maiúsculas: {nome.upper()}")
print(f"O nome com todas letras minúsculas: {nome.lower()}")
print(f"O nome tem {len(nome)- nome.count(' ')} letras")
print(f"O primeiro nome tem {len(nome.split()[0])} letras")