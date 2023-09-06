# Vaste waarden voor a en b
a = 3
b = 7

# Vergelijking van a en b
if a > b:
    print(f"Variabele a is het grootst want {a} is groter dan {b}")
elif b > a:
    print(f"Variabele b is het grootst want {b} is groter dan {a}")
else:
    print("Variabele a en b zijn gelijk.")

# Gebruiker invoer voor a en b met foutafhandeling
try:
    a = float(input("3"))
    b = float(input("7"))
except ValueError:
    print("Ongeldige invoer. Voer numerieke waarden in.")

# Opnieuw vergelijken na gebruiker invoer
if a > b:
    print(f"Variabele a is het grootst want {a} is groter dan {b}")
elif b > a:
    print(f"Variabele b is het grootst want {b} is groter dan {a}")
else:
    print("Variabele a en b zijn gelijk.")

