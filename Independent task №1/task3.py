import math
x = float(input("Введіть x: "))
if x >= 0:
    f = 0.5 - abs(x) ** 0.25
else:
 denominator=abs(x + 1)
 if denominator != 0:
  f=(math.sin(x ** 2)**2) / abs(x + 1)
 else:
     print("Ділити на нуль не можна")
     exit()

print(f"f(x) = {f:.2f}")