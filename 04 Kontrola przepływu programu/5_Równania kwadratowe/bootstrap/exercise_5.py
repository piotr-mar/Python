print("Równanie w postaci a*x**2 + b*x + c == 0")
a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))
delta = b ** 2 - 4 * a * c
if delta > 0:
    x_1 = (-b - delta ** 0.5) / (2 * a)
    x_2 = (-b + delta ** 0.5) / (2 * a)
    print(f"Pierwiastki rownania kwadratowego:\nx_1 = {x_1}\nx_2 = {x_2}")
elif delta == 0:
    x_1 = -b / (2 * a)
    print(f"Pierwiastki rownania kwadratowego:\nx_1 = x_2 = {x_1}")
else:
    print("Delta mniejsza od 0 - jest rozwiązanie ale to jeszcze nie twój poziom:)")
