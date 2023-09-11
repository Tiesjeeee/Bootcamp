from time import sleep

aantal_meldingen = 5  

oppervlakte = int(input('Hoeveel m2 vloerbedekking heeft u nodig?'))
prijs_m2 = 40

for _ in range(aantal_meldingen):
    print("Een moment geduld a.u.b., de scherpste prijs wordt berekend.")
    sleep(1)
print('Je ziet me niet lol')
totaal = prijs_m2 * oppervlakte

print(f'Het scherpste prijs voor een oppervlakte van {oppervlakte} m2 is: Eur {totaal}')
