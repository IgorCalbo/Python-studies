# Classificando Atletas
ano = int(input("Ano de nascimento do atleta: "))
idade = 2020-ano
if idade <= 9:
    print(f"O atleta tem {idade} anos. \nCategoria MIRIM")
elif idade > 9 and idade <= 14:
    print(f"O atleta tem {idade} anos. \nCategoria INFANTIL")
elif idade > 14 and idade <= 19:
    print(f"O atleta tem {idade} anos. \nCategoria JUNIOR")
elif idade > 19 and idade <= 20:
    print(f"O atleta tem {idade} anos. \nCategoria SÊNIOR")
else:
    print(f"O atleta tem {idade} anos. \nCategoria MASTER")