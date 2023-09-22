
def GetGetal():
    getalIngevoerd = False  
    while not getalIngevoerd:
        try:
            invoer = input('geef een getal ')
            getal = int(invoer)
            getalIngevoerd = True
        except:
            print('Dat is geen getal ')
    return getal

ingevoerd = GetGetal()
print(f'je hebt ingevoerd: {ingevoerd}')