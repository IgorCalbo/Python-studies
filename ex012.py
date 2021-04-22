# Calculando descontos
p = float(input("Qual é o preço do produto? R$"))
d = (5*p)/100
print(f"O produto custava R${p}, na promoção com desconto de 5% vai custar R${p-d:.2f}")