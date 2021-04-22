# Seno, Cosseno e Tangente
from math import radians, cos, sin, tan
a = float(input("Digite o ângulo que você deseja: "))
print(f"O ângulo de {a:.1f} tem o SENO de {sin(radians(a)):.2f}")
print(f"O ângulo de {a:.1f} tem o COSSENO de {cos(radians(a)):.2f}")
print(f"O ângulo de {a:.1f} tem a TANGENTE de {tan(radians(a)):.2f}")