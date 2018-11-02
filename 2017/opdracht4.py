"""Opdracht 4: valide wachtwoordcontrole. controleer hoeveel wachtwoorden geldig zijn
aaa bbb aaa dd is niet geldig
aaa aa a bbb is geldig
aa bb cc dd aaa is geldig
In deel 1 alles is lowercase!"""

file = "./bestanden/assignment4.txt"

voorbeeld = [['aaa aa dd bad'], ['aa', 'bb', 'aa', 'dd']]
totaalvoorbeeld = 0
for regel in voorbeeld:
    for phrase in regel:
        if phrase == regel:
            pass
# check per woord per regel of deze gelijk is aan een ander woord
with open(file, 'r') as f:
    totaal = 0
    totaal2 = 0
    alles = f.readlines()
    for regel in alles:
        a = regel.split()
        # pak alleen unieke phrases per regel eruit
        b = set(a)
        # phrases met eenzelfde lettercombinatie per regel eruithalen
        # itereer per woord in a, zet het op alfabetische volgorde en join ze weer terug samen
        c = set(''.join(sorted(phrase)) for phrase in a)
        if len(a) == len(b):
            totaal += 1
        if len(a) == len(c):
            totaal2 += 1
print(totaal)
print(totaal2)
