import math
x = int(input("Введіть останню цифру у списку групи (x): "))
t = 1
numerator = 9 * math.pi * t + 10 * math.cos(x)
denominator = math.sqrt(t) - abs(math.sin(t))
z = (numerator / denominator) * math.exp(x)
print(f"Z = {z:.2f}")