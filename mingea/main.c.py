import functii
def menu():
    print("C.Citirea la tastatura:")
    print("A.Afisarea:")
    print("F.Citirea fisier:")
    print("S.Scrierea fisier:")
menu()

while True:
    opt=input("Alege optinea: ")
    match opt:
        case "A":
            functii.afisarea(n,cote,cale,x0,y0)
        case "F":
            n,cote,cale,x0,y0=functii.citirea_fis()
        case "C":
            n,cote,cale,x0,y0=functii.citirea_tast()
        case "S":
            functii.scierea_fis(n,cote,x0,y0)