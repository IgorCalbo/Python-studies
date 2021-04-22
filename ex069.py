maioridade, homem, mulher = 0, 0, 0
while True:
	idade = int(input("Informe a idade: "))
	sexo = input("Informe o sexo[m/f]: ").strip().lower()
	esc = input("Quer continuar[s/n]? ").strip().lower()
	if idade >= 18:
		maioridade += 1
	if sexo == "m":
		homem += 1
	if sexo == "f" and idade < 20:
		mulher += 1
	if esc == "n":
		break
print(f"{maioridade} pessoas com mais de 18 anos cadastrados \n{homem} homens cadastrados \n{mulher} mulheres com menos de 20 anos cadastrados")