# Aumentos múltiplos
sal = float(input("Qual é o salário do funcionário? R$"))
if sal <= 1250:
    print(f"Quem ganhava R${sal} passa a ganhar R${sal+((15*sal)/100):.2f} com o aumento de 15%")
else:
    print(f"Quem ganhava R${sal} passa a ganhar R${sal+((10*sal)/100):.2f} com aumento de 10%")