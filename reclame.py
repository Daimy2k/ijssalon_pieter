from  algemene_functies import mijn_functie_2

def aanbieding_1(smaak,prijs,korting):
    korting= float(prijs) - (float(prijs) * float(korting))
    korting=format(korting,'.2f')
    uitvoer= f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de {smaak}, van {prijs} voor {korting}"
    return uitvoer

print(aanbieding_1("aardbei","4","0.1"))

def inkomsten_totaal(inkomsten,btw):
    totaal=0
    for bedrag in inkomsten:
        totaal += bedrag
    bedrag=totaal * btw
    string=f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden."
    return string

print(inkomsten_totaal([220,420,125,160,205,90,345],0.09))


def laag_en_hoog(mijn_lijst):
    return min(mijn_lijst),max(mijn_lijst)

print(laag_en_hoog([220,430,125,160,205,90,345]))


def gemiddelde(mijn_lijst):
    totaal=0
    lengte=len(mijn_lijst)
    for bedrag in mijn_lijst:
        totaal += bedrag
    bedrag= totaal / lengte
    return f"De gemiddelde inkomsten deze week zijn {bedrag} euro."
    

print(gemiddelde([220,430,125,160,205,90,345]))


def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

print(meervoudig([10,12,213,21,45,32]))


def combinatie(invoer_lijst_2):
    korte_lijst=laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0],korte_lijst[1])
    return uitvoer