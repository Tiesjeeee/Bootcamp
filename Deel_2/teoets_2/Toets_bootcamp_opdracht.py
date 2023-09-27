#OPDRACHT 1
#a: Waarom is Visual Studio Code handiger voor software development dan bijvoorbeeld Notepad (kladblok)? Noem de voordelen!
# antwoord: je kan het testen en je kan zien waar fouten zitten

#b: Waarom is het goed dat je de commits van jouw code pusht naar github.com?
# antwoord: zo raak je het nooit kwijt

#OPDRACHT 2
# Maak het commentaar af.
a = 5  # dit is een voorbeeld van het datatype:interger
b = 10.5# dit is een voorbeeld van het datatype:float
c = "Hallo wereld" # dit is een voorbeeld van het datatype:string

#OPDRACHT 3
a = 5
b = 10
print(f"a = {b}, b = {a}") # Moet "a = 10 b = 5" printen

#OPDRACHT 4
leeftijd = input("Hoe oud ben je?")
leeftijd = int(leeftijd)  
jaren_tot_pensioen = 67 - leeftijd
print(f"Dan duurt het nog ongeveer {jaren_tot_pensioen} jaar voordat je met pensioen mag!")

#OPDRACHT 5
def som(a, b, c):
    resultaat = a + b + c
    return resultaat

getal1 = 200
getal2 = 5
getal3 = 12
antwoord = som(getal1, getal2, getal3)
print(f"De som geeft het antwoord {getal1} + {getal2} + {getal3} = {antwoord}")

#OPDRACHT 6
AANTAL_GB = 20 
AANTAL_BEL_MINUTEN = 200 
ONBEPERKT = False 
aantal_minuten_gebeld = int(input("Hoeveel minuten heb je gebeld? "))
aantal_GB_internet = int(input("Hoeveel GB's heb je gebruikt? "))
if aantal_GB_internet > 20 or aantal_minuten_gebeld > 200:
    print("Let op: je moet bijbetalen!")
else:
    print("Niet aan de hand gebruik je mobiel lekker verder!")

#OPDRACHT 7
for i in range(1, 251):
    print(i)
