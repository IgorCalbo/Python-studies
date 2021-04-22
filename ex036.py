# Aprovando Empréstimo
casa = float(input("Valor da casa: "))
sal = float(input("Salário do comprador: "))
anos = int(input("Anos de financiamento: "))
prestacao = casa/(anos*12)
if prestacao <= (30*sal)/100:
    print(f"Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação será de R${prestacao:.2f} \nEmpréstimo pode ser CONCEDIDO!")
else:
    print(f"Para pagar uma casa de R${casa:.2f} em {anos} anos a prestação será de R${prestacao:.2f} \nEmpréstimo NEGADO!")