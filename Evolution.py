from copy import *

"""

DP(W(t) = w) = 2(1-v/c)^2 P(W = w -v/2 - y/2) + 2(1-v/c)v/c[P(W = w -v - y/2) + P(W = w - y/2)] + (v/c)^2 [P(W = w - v - y/2) + P(W = w + c - y/2)] - 2 P(W = w) - Dw

"""

#Dw = delta P(W = w) si w \neq 0 et D0 = delta (P(W = 0) -1)


v = 2
c = 4
y = 8
d = 0.1  #Delta
DicoWealth = {-6:0,-5:0,-4:0,-3:0,-2:0,-1:0,0:1}

def Ajout(cle):
    global DicoWealth
    if cle not in DicoWealth:
        DicoWealth[cle] = 0

def NouvelleValeur():
    global DicoWealth
    Liste = list(DicoWealth.keys())
    L = deepcopy(Liste)
    for cle in L:
        Ajout(int(cle + v + y/2))
        Ajout(int(cle + v/2 + y/2))
        Ajout(int(cle + y/2))
        Ajout(int(cle - c + y/2))

NouvelleValeur()
for cle in DicoWealth.keys():
    if cle > 0 :
        DicoWealth[cle] = 2*(1 - v/c)**2 * DicoWealth[cle - v/2 - y/2] + 2*(1 - v/c)*v/c*(DicoWealth[cle - v - y/2] + DicoWealth[cle - y/2]) + (v/c)**2*(DicoWealth[cle + c - y/2] + DicoWealth[cle -v -y/2]) - DicoWealth[cle]
