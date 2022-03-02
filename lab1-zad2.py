print("Wprowadz dwie liczby aby przeprowadzic dzialanie")
a = float(input("Wprowadz pierwsza liczbe: "))
b = float(input("Wprowadz druga liczbe: "))
print("Wybierz dzialanie ktore ma byc wykonane\n1.Dodawanie\n2.Odejmowanie\n3.Mnozenie\n4.Dzielenie\n5.Dzielenie Calkowite\n6.Potegowanie")
c = int(input("Numer dzialania: "))
if c == 1:
    print(a + b)
if c == 2:
    print(a - b)
if c == 3:
    print(a * b)
if c == 4:
    print(a / b)
if c == 5:
    print(a // b)
if c == 6:
    print(a ** b)
