# Radar eletrônico
v = float(input("Qual é a velocidade atual do carro: "))
m = (v-80)*7
if v > 80:
    print(f"Você excedeu o limite permitido de 80km/h \nVocê deve pagar uma multa de R${m:.2f}!")
else:
    print("Tenha um bom dia! Dirija com segurança!")