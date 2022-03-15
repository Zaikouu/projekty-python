import sys as system
import math
# Zadanie 1
# sporty = ['szachy','skoki','nozna']
# sporty.reverse
# print(sporty)
# sporty.append('siatkowka')
# sporty.append('reczna')
# print(sporty)

# Zadanie 2
# skroty = {'itd':'I tak dalej', 'itp':'I tym podobne', 'np':'na przyklad', 'pt':'pod tytulem'}
# print(skroty)

# Zadanie 3
# Gry = {'LoL':'League of Legends', 'Apex':'Apex Legends', 'TFT':'Teamfight Tactics', 'GTA':'Grand Theft Auto', 'DMC':'Devil May Cry'}
# print(len(Gry))

# Zadanie 4
# ilosc_a = input("Wpisz jakies zdanie: ")
# print(ilosc_a.count('a'))

# Zad 5. Napisz skrypt gdzie pobierzesz trzy liczby całkowite, gdzie wykonasz obliczenia: a^b + c.
# Użyj instrukcji readline() i write()).
# system.stdout.write("wpisz dowolne liczby calkowite: ")
# a = int(system.stdin.readline())
# b = int(system.stdin.readline())
# c = int(system.stdin.readline())
# wynik = (pow(a,b)+c)
# system.stdout.write(str(wynik))

# Zad 6. Wczytaj trzy liczby całkowite a,b,c i sprawdź, która z nich jest największa. W zależności od
# wyniku wyświetl odpowiedni komunikat. Użyj zagnieżdżeń.
# a = int(input("Wpisz 3 liczby calkowite: "))
# b = int(input())
# c = int(input())
# maks = a
# if (a<b):
#     maks = b
#     if(b<c):
#         maks = c
# print("Najwieksza liczba to %(z1)d"%{'z1':maks})

# Zad 7. Napisz skrypt, gdzie stworzysz listę składającą się z liczb typu int i float. Następnie za pomocą
# użycia pętli for podnieś każdą liczbę do kwadratu.
# lista = [10,4.5,1.1,4]
# b = 0
# for a in lista:
#     lista[b] = pow(a,2)
#     b+=1
# print(lista)

# Zad 8. Napisz skrypt, który za pomocą pętli while pobiera 10 liczb, następnie dodaje do listy tylko
# parzyste liczby.
# a = []
# a1 = []
# b = 0
# c = 0
# d = 0
# while b < 10:
#     a[c] = int(input())
#     b+=1
#     c+=1
#     if(a[c]%2==0):
#         a1[d] = a[c]
#         d += 0