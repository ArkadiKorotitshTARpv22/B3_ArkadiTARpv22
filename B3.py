from moodul import *

print("Arkadi Korotitsh TARpv22 poolt\n")

linnad=[]
elanikkond=[]

n=int(input("Sisestage linna arv: "))

for j in range(n):
    linn=input("Sisestage linna nimi: ")
    elanik=int(input("Sisestage selle linna elanikkond: "))
    linnad.append(linn)
    elanikkond.append(elanik)

print(linnad,elanikkond)

while True:
        menu=int(input("Käsklused: \n1-saab teada, kui palju on elanikke, sisestades linna nime\n2- Kuvab linnade nimekirja ja elanike arvu tähestikulises järjekorras\n3-saab linna rahvaarvu, sisestades linna nime\n4-saab linnad, kus on vähem kui n elanikku\n5-saab suurima rahvaarvuga linna\n"))
        if menu==1:
            get_population(elanikkond,linnad)
        elif menu==2:
            show_inf(elanikkond,linnad)
        elif menu==3:
            get_city(elanikkond,linnad)
        elif menu==4:
            less(elanikkond,linnad)
        elif menu==5:
            most_pop(elanikkond,linnad)
