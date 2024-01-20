import math

pizza1_srednica = 42
pizza1_cena = 36

pizza2_srednica = 56
pizza2_cena = 42.5

pole1 = (pizza1_srednica / 2) ** 2 * math.pi
pole2 = (pizza2_srednica / 2) ** 2 * math.pi

pizza1 = pole1 / pizza1_cena
pizza2 = pole1 / pizza2_cena

print("Stosunki wielkości pizzy do ceny")
print(f"pizza1: {pole1 / pizza1_cena}")
print(f"pizza2: {pole2 / pizza2_cena}")