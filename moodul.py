def get_population(e:list,l:list):
    linn=input("Sisestage linna nimi, mille elanike arvu soovite teada:")
    while linn not in l:
        linn=input("Palun kirjuta õige linna nimi\n")
    print(f"{linn} rahvaarv on võrdne ",e[l.index(linn)],"")

def get_city(e:list,l:list):
    arv=int(input("Sisestage elanike arv: "))
    erinev_ls=[]
    while arv<1:
        arv=int(input("Arv peab olema suurem kui 0: "))
    for i in e:
        erinevus=abs(i-arv)
        erinev_ls.append(erinevus)
    min_erinevus=min(erinev_ls)
    print("Selle linna ligikaudne rahvaarv: ",l[erinev_ls.index(min_erinevus)])
    
def less(e:list,l:list):
    n=int(input("Sisestage elanike arv: "))
    linna=[]
    while n<1:
        n=int(input("Arv peab olema suurem kui 0: "))
    for i in e:
        if n>i:
            elanik_index=e.index(i)
            linna.append(l[elanik_index])
    print("Nendes linnades on elanike arv väiksem: ",linna)

def show_inf(e:list,l:list):
    l_copy=l.copy()
    l_copy.sort()
    sorted_elanikud=[]
    for element in l_copy:
        temp_var=l.index(element)
        sorted_elanikud.append(e[temp_var])
    print(l_copy)
    print(sorted_elanikud)
    print()

def most_pop(e:list,l:list):
    print("Suurima elanikkonnaga linn: ")
    print(min(e), l[e.index(min(e))])
