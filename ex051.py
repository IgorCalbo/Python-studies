#  Progressão Aritmética
a1 = int(input("Primeiro termo: "))
r = int(input("Razão: "))
a10 = a1 + (10-1) * r
for c in range(a1,a10+r,r):
    print(c, end=" -> ")
print("fim")