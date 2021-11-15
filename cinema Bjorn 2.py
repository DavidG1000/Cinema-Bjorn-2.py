leeftijd = 4
prijs = 0
film3d = "nee"
lang = "nee"
student = "j"

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

print("Persoon 1 betaald:",prijs,"euro")
