import itertools

"""Opdracht 2 van AOC
1: vind per regel het verschil tussen het grootste en kleinste getal
2: vind het grootste en kleinste getal per regel met modulo == 0"""
file = './bestanden/assignment2.txt'
with open(file, 'r') as f:
    # tel het verschil per regel op bij totaal1 en totaal2
    totaal1 = 0
    totaal2 = 0
    # voeg iedere regel als lijst met integers in alle_regels
    genummerde_regels = []
    # haal \n weg, split iedere regel op \t
    for regel in f:
        r = regel.strip().split('\t')
        getallenlijst = [int(i) for i in r]
        genummerde_regels.append(getallenlijst)
    # reken het verschil tussen het maximum en het minimum van iedere regel, tel op bij totaal
    for regel in genummerde_regels:
        verschil1 = max(regel) - min(regel)
        totaal1 += verschil1
        # combinatie tussen het grootste en kleinste getal in regel die geen restgetal hebben
        for getal in itertools.combinations(regel, 2):
            groot = max(getal)
            klein = min(getal)
            # tel het quotient op bij totaal2
            if groot % klein == 0:
                verschil2 = max(getal) / min(getal)
                totaal2 += verschil2
    # reken het verschil tussen tussen getallen met modulo = 0
    print(totaal1)
    print(totaal2)


"""map: koppel functie aan meerdere iterables in adhv het aantal parameters die de functie neemt"""
# def myfunc(a, b):
#   return a + b
#
# x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
# y = []
# print(list(y))
