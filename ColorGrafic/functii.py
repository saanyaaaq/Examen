def citirea_tast():
    graf=dict()
    n=int(input("Introdu numarul de noduri: "))
    for y in range(n):
        linie=input("Introdu nodurile ( A:B,C )")
        nod_crt,urm=linie.strip().split(":")
        lst_urm=[t.strip() for t in urm.split(',') if t !='']
        includeNod(nod_crt,lst_urm,graf)
    return n,graf
def afisarea(n,graf):
    print(f"Aveti {n} noduri")
    print(graf)
def citirea_fis():
    graf=dict()
    with open("file.txt",'r')as f:
        linii=f.readlines()
        n=int(linii[0])
        for i in linii[1:]:
            nod_crt,urm=i.strip().split(":")
            lst_urm=[t.strip() for t in urm.split(",")if t !='']
            includeNod(nod_crt, lst_urm, graf)
    return n,graf
def includeNod(nod,lst_urm,graf):
    if nod in graf:
        graf[nod]+=lst_urm
    else:
        graf[nod]=lst_urm