import functii
from functii import *
# Graf orientat
def menu():
        print("1. Citire tastatura")
        print("2. Citire fisier")
        print("3. Afisare date")
        print("4. Scrierea in fisier")
        print("5. Rezolvare")

menu()
while True:
        opt = int(input("Alege: "))
        match(opt):
            case 1:
                graf = citire_tastatura()
            case 2:
                numeFis = input("Introdu nume fisier = ")
                graf=citirea_fisier(numeFis)
            case 3:
                functii.afisare(graf)


