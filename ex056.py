# Analisador completo
medIdade = 0.0
maiorIdadeHomem = 0
nomeVelho = ''
mulher = 0
for i in range(1,5):
    print(f"----- {i}º PESSOA -----")
    nome = input("Nome: ").strip()
    idade = int(input("Idade: "))
    sexo = input("Sexo[F/M]: ").strip().upper()
    if i == 1 and sexo == "M":
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo == "M" and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    medIdade += idade / 4
    if sexo == "F" and idade < 20:
        mulher += 1
print(f"A média de idade do grupo é {medIdade} anos") 
print(f"O homem mais velho tem {maiorIdadeHomem} anos e seu nome é {nomeVelho}")
print(f"Ao todo são {mulher} mulheres com menos de 20 anos")
