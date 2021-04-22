# Comparando números
num1 = int(input("Primeiro número inteiro: "))
num2 = int(input("Segundo número inteiro: "))
if num1 > num2:
    print("O primeiro valor é maior")
elif num1 < num2:
    print("O segundo valor é maior")
elif num1 == num2:
    print("Não existe valor maior, os dois são iguais")
else:
    print("Valor inválido")