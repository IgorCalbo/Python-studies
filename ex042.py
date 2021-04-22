# Analisando Triângulos v2.0
a = float(input("Primeiro segmento: "))
b = float(input("Segundo segmento: "))
c = float(input("Terceiro segmento: "))
if (b-c) < a < b+c and (a-c) < b < a+c and (a-b) < c < a+b:
    if a == b and a == c:
        print("Os segmentos acima formam um triângulo EQUILÁTERO")
    elif a == b and a != c or a == c and a!= b or b == c and b != a:
        print("Os segmentos acima formam um triângulo ISÓSCELES")
    elif a != b and a != c and b != c:
        print("Os segmentos acima formam um triângulo ESCALENO")
else:
    print("Os segmentos acima NÂO podem formar um triângulo!")
