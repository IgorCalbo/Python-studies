# Analisando Triângulo v1.0
a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))
if (b-c) < a < b+c and (a-c) < b < a+c and (a-b) < c < a+b:
    print("Os segmentos acima PODEM formar um triângulo!")
else:
    print("Os segmentos acima NÂO podem formar um triângulo!")
