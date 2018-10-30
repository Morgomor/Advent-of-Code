"""Opdracht 1:
1: vind het getal in de reeks die als combinatie getallen achter elkaar voorkomen en tel ze op
    voorbeeld: 1122 is 3, de combinatie 1 komt 1x voor, combinatie 2 komt 1x voor, dus (1 * 1) + (2 * 1)
    voorbeeld: 91212129 is 9, want de combinatie negen komt maar 1x voor
2: vind nu het getal op de helft van lengte van de lijst vandaan en vergelijk deze
    """

file = "./bestanden/assignment1.txt"

voorbeeld = '1122'
totaal_voorbeeld = 0
# begin tellen vanaf het einde (list is een cirkel!)
for i in range(0, len(voorbeeld)-1):
    # check ieder getal na
    if voorbeeld[i] == voorbeeld[i + 1]:
        totaal_voorbeeld += int(voorbeeld[i])
    if voorbeeld[0] == voorbeeld[-1]:
        totaal_voorbeeld += int(voorbeeld[i])

with open(file, 'r') as f:
    totaal1 = 0
    totaal2 = 0
    data = f.readline().strip()
    for getal in range(len(data)-1):
        if data[getal] == data[getal + 1]:
            totaal1 += int(data[getal])
    if data[0] == data[-1]:
        totaal1 += int(data[0])
    for getal in range(0, len(data)-1):
        if data[getal] == data[(getal + len(data) // 2) % len(data)]:
            totaal2 += int(data[getal])
print(totaal1)
print(totaal2)

zippert = tuple(zip(['one', 'two', 'three'], [1, 2, 3]))
f = open(file).readline().strip()
# voeg de eerste nog een keer toe, zodat je deze met het laatste getal kunt vergelijken in een tuple
data = f + f[0]
checksum = sum([int(a) for a, b in zip(data, data[1:])if a == b])
print(checksum)
