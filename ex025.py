# Procurando uma string dentro de outra
nome = input("Qual é seu nome completo: ").strip()
print(f"Seu nome tem Silva? {'silva' in nome.lower().split()}")