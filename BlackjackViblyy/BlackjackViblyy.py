from random import *
valet=10
dama=10
kuningas=10
tuz=11
m�ngejakardid=[]
dillerikardid=[]
kardid=[2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,valet,valet,valet,valet,dama,dama,dama,dama,kuningas,kuningas,kuningas,kuningas,tuz,tuz,tuz,tuz]
while True:
    try:
        vastus1=int(input("Kas tahad m�ngida BlackJack? Jah-(1) Ei-(0)"))
        if vastus1==1 or 0:
            break
        else:
            print("Palun sissetage 1 v�i 2")
    except ValueError:
        print("Sissetage t�isarv")
if vastus1==1:
    while True:
        try:
            pakkumine=int(input("Sull on 200 euro, kui palju sa tahad bettida?"))
            if 0<pakkumine<=200:
                break
            else:
                print("Palun sissetage arv diaposonis �hest kahesajani")
        except ValueError:
            print("Sissetage t�isarv")
while len(m�ngejakardid)<2:
    randomkard1=random.choice(kardid)
    m�ngejakardid.append(randomkard1)
    kardid.remove(randomkard1)
    randomkard2=random.choice(kardid)
    dillerikardid.append(randomkard2)
    kardid.remove(randomkard2)
while True:
    try:
        vastus2=int(input("Sull on: {m�ngejakardid}. Dilleril on", randomkard2 "ja veel �ks kaard, kas tahat v�tta veel �he kardi(1) v�i ei(0)?"))
        if vastus2==1 or 0:
            break
        else:
            print("Palun sissetage 1 v�i 2")
    except ValueError:
        print("Sissetage t�isarv")
if vastus2==1:
    
        