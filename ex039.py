# Alistamento Militar
ano = int(input("Ano de nascimento: "))
idade = 2020 - ano
print(f"Quem nasceu em {ano} tem {idade} anos em 2020.")
if idade < 18:
    print(f"Ainda faltam {18-idade} anos para o seu alistamento \nSeu alistamento será em {2020+(18-idade)}")
elif idade == 18:
    print("Você tem que se alistar IMEDIATAMENTE!")
elif idade > 18:
    print(f"Você já deveria ter se alistado há {idade-18} anos. \nSeu alistamento foi em {2020-(idade-18)}")