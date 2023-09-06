# Definieer de gegevens
totaal_bedrag = 625
getal_te_delen = 13

# Bereken het aantal keren dat getal_te_delen helemaal in totaal_bedrag past
aantal_keer = totaal_bedrag // getal_te_delen

# Bereken wat er overblijft na de deling
overblijfsel = totaal_bedrag % getal_te_delen

# Druk de resultaten af
print(f"{getal_te_delen} past helemaal {aantal_keer} keer in {totaal_bedrag}.")
print(f"Het overblijvende bedrag is {overblijfsel}.")
