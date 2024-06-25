
sum=0
bancnote=[]
d={}
nr_200=1
nr_100=1
nr_50=1
nr_20=1
nr_10=1
nr_5=1
nr_1=1
out=0
bancnote_necesare=0
def citirea_tast():
    global nr_200,nr_100,nr_50,nr_20,nr_10,nr_5,nr_1,bancnote,d
    nr_200=int(input("Introdu bancnota de 200: "))
    nr_100=int(input("Introdu bancnota de 100: "))
    nr_50=int(input("Introdu bancnota de 50: "))
    nr_20=int(input("Introdu bancnota de 20: "))
    nr_10=int(input("Introdu bancnota de 10: "))
    nr_5=int(input("Introdu bancnota de 5: "))
    nr_1=int(input("Introdu bancnota de 1: "))
    bancnote = [200, 100, 50, 20, 10, 5, 1]
    d = {200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 1: 0}
def citirea_fisier():
    global bancnote,d,nr_200,nr_100,nr_50,nr_20,nr_10,nr_5,nr_1
    with open("banc.txt",'r')as f:
        linii=f.readlines()
        nr_200=int(linii[0])
        nr_100=int(linii[1])
        nr_50=int(linii[2])
        nr_20=int(linii[3])
        nr_10=int(linii[4])
        nr_5=int(linii[5])
        nr_1=int(linii[6])
        bancnote = [200, 100, 50, 20, 10, 5, 1]
        d = {200: 0, 100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 1: 0}
    print("Ati citit cu succes!!!")
def rezovolvarea_pr():
    global bancnote,d
    bancnote.sort(reverse=True)
    sum=int(input("Ce suma doriti: "))
    out=0
    while out<sum:
        for i in bancnote:
             if i<=sum-out:
                out=out+i
                d[i]=d[i]+1
                break
    for i in d:
        if d[i]!=0:
            print(d[i],'x',i)
def afisarea():
    print(f"Sunt {nr_200} bancnote de 200")
    print(f"Sunt {nr_100} bancnote de 100")
    print(f"Sunt {nr_50} bancnote de 50")
    print(f"Sunt {nr_20} bancnote de 20")
    print(f"Sunt {nr_10} bancnote de 10")
    print(f"Sunt {nr_5} bancnote de 5")
    print(f"Sunt {nr_1} bancnote de 1")
def scierea_fisier():
    with open('output.txt','w')as f:
        f.write(f"{nr_200}\n{nr_100}\n{nr_50}\n{nr_20}\n{nr_10}\n{nr_5}\n{nr_1}\n")
    print("Ati scris cu succes in fisier!!!")

def menu():
        print("1.Citirea de tast: ")
        print("2.Afisarea")
        print("3.Citirea din fisier")
        print("4.Rezolvarea problemelor")
        print("5.Scrierea Fisierul:")
menu()
while True:
        opt = input("Alege optiunea: ")
        match opt:
            case '1':
                citirea_tast()
            case '2':
                afisarea()
            case '3':
                citirea_fisier()
            case'4':
                rezovolvarea_pr()
            case '5':
                scierea_fisier()
