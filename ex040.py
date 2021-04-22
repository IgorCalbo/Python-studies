# Aquele clássico da Média
n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
media = (n1 + n2)/2
if media < 5:
    print(f"A média do aluno é {media}, aluno REPROVADO!")
elif media >= 5 and media <= 6.9:
    print(f"A média do aluno é {media}, aluno em RECUPERAÇÂO!")
else:
    print(f"A média do aluno é {media}, aluno APROVADO!")
