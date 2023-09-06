# Berekeningen met verschillende spatiëring, maar dezelfde uitkomst
print(5 * 2 - 3 + 4 / 2)  # Uitkomst: 8.0
print(5 * 2 - 3 + 4 / 2)  # Uitkomst: 8.0

# Beide uitdrukkingen geven dezelfde uitkomst omdat Python operatorprecedentie volgt.
# Eerst worden vermenigvuldigingen en delingen van links naar rechts uitgevoerd,
# en daarna optellingen en aftrekkingen van links naar rechts.

# Berekeningen met haakjes en prioriteit
print((5 * 2) - (3 + 4) / 2)   # Uitkomst: 6.0
print(((5 * 2) - (3 + 4)) / 2)  # Uitkomst: 3.5

# Het gebruik van haakjes beïnvloedt de volgorde van uitvoering van bewerkingen.
# In het eerste geval worden eerst de haakjes (3 + 4) en (5 * 2) uitgevoerd,
# gevolgd door deling en aftrekking, wat resulteert in 6.0.
# In het tweede geval worden eerst de haakjes (3 + 4) en (5 * 2) uitgevoerd,
# gevolgd door aftrekking en deling, wat resulteert in 3.5.
