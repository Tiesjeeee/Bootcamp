from time import sleep

aantal_meldingen = 1

aantal = int(input('Hoeveel wilt u kopen?'))
prijs = 1000000

for _ in range(aantal_meldingen):
    print("Een moment geduld a.u.b., de de website wil niet werken.")
    sleep(1)
print('Je ziet me niet lol')
totaal = prijs * aantal

print(f'Het scherpste prijs voor het product {aantal}  is: Eur {totaal}')