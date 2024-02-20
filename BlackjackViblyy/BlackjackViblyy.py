from random import *
valet=10
dama=10
kuningas=10
tuz=11
mängejakardid=[]
dillerikardid=[]
kardid=[2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,valet,valet,valet,valet,dama,dama,dama,dama,kuningas,kuningas,kuningas,kuningas,tuz,tuz,tuz,tuz]
while True:
    try:
        vastus1=int(input("Kas tahad mängida BlackJack? Jah-(1) Ei-(0)"))
        if vastus1==1 or 0:
            break
        else:
            print("Palun sissetage 1 või 2")
    except ValueError:
        print("Sissetage täisarv")
if vastus1==1:
    while True:
        try:
            pakkumine=int(input("Sull on 200 euro, kui palju sa tahad bettida?"))
            if 0<pakkumine<=200:
                break
            else:
                print("Palun sissetage arv diaposonis ühest kahesajani")
        except ValueError:
            print("Sissetage täisarv")
while len(mängejakardid)<2:
    randomkard1=random.choice(kardid)
    mängejakardid.append(randomkard1)
    kardid.remove(randomkard1)
    randomkard2=random.choice(kardid)
    dillerikardid.append(randomkard2)
    kardid.remove(randomkard2)
while True:
    try:
        vastus2=int(input("Sull on: {mängejakardid}. Dilleril on", randomkard2 "ja veel üks kaard, kas tahat võtta veel ühe kardi(1) või ei(0)?"))
        if vastus2==1 or 0:
            break
        else:
            print("Palun sissetage 1 või 2")
    except ValueError:
        print("Sissetage täisarv")
if vastus2==1:
    
        