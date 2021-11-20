import math
aantal = int(input("Aantal personen ? "))
persLid = input("Bent u personeelslid ? (j/n) ")
leeftijd = 0
prijs = 0
film3d = 0
lang = 0
student = 0
totaalPrijs = 0
korting = 0

for i in range(1,aantal+1):
    print("Persoon ",i)
    leeftijd = int(input("Geef de leeftijd in "))
    student = input("Student ? (j/n) ")
    film3d = input("Is de film in 3D ? (j/n) ")
    lang = input("Is het een lang/speelfilm ? (j/n) ")

    if(leeftijd < 15):
        prijs = 4
    elif(leeftijd < 19):
        prijs = 5
    elif(leeftijd < 22):
        prijs = 6
    else:
        prijs = 7
    if(film3d == "j"):
        prijs = prijs +2
    else:
        prijs = prijs + 0
    if(lang == "j"):
        prijs = prijs + 2
    else:
        prijs = prijs + 0
    if (student == "j") and (leeftijd < 26):
        prijs = prijs - 2
    else:
        prijs = prijs + 0
    totaalPrijs = totaalPrijs + prijs
    print("Persoon",i, "betaald:",prijs,"euro")
    print("********************************************")

if (persLid == "j"):
    korting=(totaalPrijs*10)/100
    print("Het totaal is ",totaalPrijs-korting,"euro (met personeelskorting)")
else: print(" Het totaal is", totaalPrijs,"euro" )





