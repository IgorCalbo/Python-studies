# Primeira e última ocorrência de uma string
frase = input("Digite uma frase: ").strip().lower()
print(f"A letra A aparece {frase.count('a')} vezes na frase.")
print(f"A primeira letra A aparece na posição {frase.find('a')+1}")
print(f"A última letra A aparece na posição {frase.rfind('a')+1}")