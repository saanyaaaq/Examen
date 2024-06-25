import functii
def menu():
        print("1. Citire tastatura")
        print("2. Citire fisier")
        print("3. Afisare matrice")
        print("4. Scriere fisier")
        print("5. Rezolvare")
menu()
while True:
        opt = int(input("Alege: "))
        match opt:
            case 1:
                n,start, stop, matrice, drumuri = functii.citire_tastatura()
            case 2:
                n, start, stop, matrice, drumuri = functii.citire_fisier()
            case 3:
                functii.afisare(n, matrice)
            case 4:
                functii.scriere_fisier(n, start, stop, drumuri)