import functii
def menu():
    print("C.Citirea tastatura:")
    print("A.Afisarea:")
    print("F.Citirea fisier:")
menu()
while True:
    opt=input("Alege optiunea: ")
    match opt:
        case "C":
            n,graf=functii.citirea_tast()
        case "A":
            functii.afisarea(n,graf)
        case "F":
            n,graf=functii.citirea_fis()