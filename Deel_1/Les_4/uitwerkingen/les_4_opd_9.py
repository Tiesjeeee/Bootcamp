# Gegevens over coStelllegegeld
aantal_studenten = 24
collegegeld_per_student = 1115

# Bereken het totale collegegeld
totaal_collegegeld = aantal_studenten * collegegeld_per_student

# Gegevens over fruitaankopen
prijs_appels = 3.40
prijs_druiven = 2.45
prijs_bananen = 1.95

# Bereken de totale kosten van fruit
totaal_fruitkosten = prijs_appels + prijs_druiven + prijs_bananen

# BTW-percentage op fruit (in Nederland)
btw_percentage_fruit = 9  

# Bereken de BTW op fruit
btw_bedrag_fruit = (btw_percentage_fruit / 100) * totaal_fruitkosten

# Druk de resultaten af
print(f"Totaal collegegeld betaald door alle studenten: {totaal_collegegeld} euro")
print(f"Totaal kosten van fruit: {totaal_fruitkosten} euro")
print(f"BTW op fruit ({btw_percentage_fruit}%): {btw_bedrag_fruit} euro")
