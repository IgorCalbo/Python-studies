# Validação de Dados
sexo = input("Informe seu sexo: ").strip().upper()[0]
while sexo not in "MF":
    sexo = input("Dados Inválidos. Por favor, informe seu sexo: ").strip().upper()[0]
print(f"Sexo {sexo} registrado com sucesso")
