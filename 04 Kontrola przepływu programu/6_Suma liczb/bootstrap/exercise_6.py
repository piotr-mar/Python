n = int(input("Podaj n: "))
suma_liczb = 0
for i in range(0, n + 1):
    suma_liczb += i
print(suma_liczb)

suma_liczb_sum = sum(range(n + 1))
print(suma_liczb_sum)
