name = (input('wat is je naam'))
age = int(input('wat is je leeftijd?'))

if age < 18:
    print('Beste <name>, je bent nog geen 18. Alleen autorijden zit er dus niet in :-( ')
else:
    if age >= 18:
        print('Beste <name> je mag alleen autorijden')