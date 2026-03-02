palavra1=str(input())
palavra2=str(input())
palavra3=str(input())

if palavra1 == "vertebrado":
    if palavra2 == "ave":
        if palavra3 == "carnivoro":
            print("aguia")
        elif palavra3 == "onivoro":
            print("pomba")
    elif palavra2 == "mamifero":
            print("homem")
    elif palavra3 == "herbivoro":
            print("vaca")
elif palavra1 == "invertebrado":
    if palavra2 == "inseto":
        if palavra3 == "hematofado":
            print("pulga")
        elif palavra3 == "herbivoro":
            print("Lagarta")
    elif palavra2 == "anelideo":
        if palavra3 == "hematofago":
            print("sanguessuga")
        elif palavra3 == "onivoro":
            print("minhoca")