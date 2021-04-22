# Grupo da Maioridade
menor = 0
maior = 0
for pessoas in range(1,8):
    ano = int(input("Digite o ano de nascimento: "))
    idade = 2020-ano
    if idade >= 18:
        maior +=1
    else:
        menor +=1
print(f"{menor} pessoas ainda não atingiram a maioridade e {maior} já são maiores de idade.")