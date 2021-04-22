# Gerenciador de Pagamentos
p = float(input("Preço das compras: R$"))
print("""FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão)""")
op = int(input("Qual é a opção: "))
if op == 1:
    pf = p - (10*p)/100
    print(f"Sua compra de R${p:.2f} vai ficar R${pf:.2f} no final.")
elif op == 2:
    pf = p - (5*p)/100
    print(f"Sua compra de R${p:.2f} vai ficar R${pf:.2f} no final.")
elif op == 3:
    print(f"Pagando em 2x no cartão o preço é o mesmo.")
elif op == 4:
    pf = p + (20*p)/100
    print(f"Sua compra de R${p:.2f} vai ficar R${pf:.2f} no final.")
else:
    print("Opção inválida.")
