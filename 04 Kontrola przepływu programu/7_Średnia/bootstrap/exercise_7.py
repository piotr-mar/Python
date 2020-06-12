n = int(input("Podaj ile liczb wprawadzisz: "))
numbers = []
for i in range(n):
    numbers.append(int(input("podaj liczbę: ")))
suma_liczb = sum(numbers)
srednia_liczb = suma_liczb / n
if srednia_liczb > suma_liczb:
    print(f"Wprowadzone liczby: {numbers}\nSuma: {suma_liczb}\nŚrednia: {srednia_liczb}\nŚrednia jest większa")
elif srednia_liczb < suma_liczb:
    print(f"Wprowadzone liczby: {numbers}\nSuma: {suma_liczb}\nŚrednia: {srednia_liczb}\nSuma jest większa")
else:
    print(f"Wprowadzone liczby: {numbers}\nSuma: {suma_liczb}\nŚrednia: {srednia_liczb}\nSą takie same")
