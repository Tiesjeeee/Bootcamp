# Definieer de gegevens
seconden_per_minuut = 60
minuten_per_uur = 60
uren_per_dag = 24
dagen_per_week = 7
dagen_per_jaar = 365

# Bereken het aantal seconden in een dag
seconden_in_dag = seconden_per_minuut * minuten_per_uur * uren_per_dag

# Bereken het aantal seconden in een week
seconden_in_week = seconden_in_dag * dagen_per_week

# Bereken het aantal seconden in een jaar
seconden_in_jaar = seconden_in_dag * dagen_per_jaar

# Druk de resultaten af
print(f"Aantal seconden in een dag: {seconden_in_dag} seconden")
print(f"Aantal seconden in een week: {seconden_in_week} seconden")
print(f"Aantal seconden in een jaar: {seconden_in_jaar} seconden")
