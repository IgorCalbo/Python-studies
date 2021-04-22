# Número por extenso
listaNum = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
for count in enumerate(listaNum):
    numero = int(input("Digite um número entre 0 e 20: "))
    while numero < 0 or numero > 20:
        numero = int(input("Tente novamente. Digite um número entre 0 e 20: "))
    break
print(f"Você digitou o número {listaNum[numero]}")