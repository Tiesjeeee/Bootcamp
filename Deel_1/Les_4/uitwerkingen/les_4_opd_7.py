# Het volgende stuk code lijkt in eerste instantie triviaal:
# We delen 431 door 100 en vermenigvuldigen het resultaat vervolgens met 100.
# Dus, we zouden verwachten dat de uitkomst gewoon 431 is, omdat we hetzelfde getal vermenigvuldigen.
# Laten we eens kijken of dat klopt.

resultaat = (431 / 100) * 100
print(resultaat)

# Verwachte uitkomst: 431.0
# Werkelijke uitkomst: 431.0

# Het resultaat is inderdaad 431.0, zoals verwacht.
# Dit kan verwarrend lijken, maar het heeft te maken met het gebruik van drijvende-kommaberekeningen
# in computers, waarbij soms kleine afrondingsfouten optreden.
# In dit geval wordt 431/100 uitgevoerd met behulp van drijvende-kommaberekeningen en wordt het resultaat
# opgeslagen met enkele decimalen (431.0). Wanneer we dit resultaat met 100 vermenigvuldigen,
# krijgen we nog steeds 431.0.
