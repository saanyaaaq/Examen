def citirea_tast():
    matricea=[]
    n=int(input("Dati numarul de directii: "))
    cote=n*[None]
    cale=n*[None]
    for i in range(n):
        cote[i]=[int(x) for x in input("Dati directiile: ").split()]
        cale[i]=[0]*n
    x0=int(input("Dati x0 initial: "))
    y0=int(input("Dati y0 initial: "))
    return n,cote,cale,x0,y0
def afisarea(n,cote,cale,x0,y0):
    print(f"Aveti {n} directii!")
    print(f"x,y=({x0},{y0})")
    for i in range(n):
        print(*cote[i])
def citirea_fis():
    with open("minge.txt",'r')as f:
        linii=f.readlines()
        n=int(linii[0])
        cote=n*[None]
        cale=n*[None]
        for i in range(n):
            cote[i]=[int(x) for x in linii[i+1].split()]
            cale[i]=[0]*n
        x0=int(linii[4])
        y0=int(linii[5])
    return n,cote,cale,x0,y0
def scierea_fis(n,cote,x0,y0):
    with open("out",'w')as f:
        f.write(f"{n}\n{x0} {y0}\n")
        for i in range(n):
            f.write(f"{cote[i]}\n")


