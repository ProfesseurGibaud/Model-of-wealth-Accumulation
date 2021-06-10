import random as rd
import matplotlib.pyplot as plt
import numpy as np
v = 20
c = 40
y = 100
delta = 0.1  #Delta
N = 10000
T = 1000000
lamda = 1
Wealth_Strengh = True
alpha = v/delta*(1 - v/c)
E = alpha + y/delta #Mean of W
beta = v**2/(2*delta)*(3 - (1 - v/c)**2)
Var = (alpha + y/delta)**2 + y**2/delta + beta

class Individual:
    def __init__(self):
        self.w = 0
        self.name = -1
        self.pH = v/c
    def ProbaH(self,signal):
        global Wealth_Strengh
        if not Wealth_Strengh:
            self.pH = 1/2
        else:
            Signal1 = self.w
            Signal2 = signal
            if abs(Signal1 - Signal2)<np.log(c/v)/lamda:
                f = np.exp(lamda*Signal1)/(np.exp	(lamda*Signal1) + np.exp(lamda * Signal2))
                self.pH = v /(2*(v+c)*f-v)
            elif (Signal1 - Signal2)>np.log(c/v)/lamda:
                self.pH = 1
            else: #Vérifier le else
                self.pH = 0
    def Depreciation(self):
        global delta
        #print(str(self.name) + " Depreciation")
        if rd.random()< delta:
            self.w = 0



def Jeu(I1,I2):
    global Dico
    #print(str(I1.name) + " " + str(I2.name) + "Game")
    Signal1 = I1.w
    Signal2 = I2.w
    f = 1/2*(Wealth_Strengh == False) + (np.exp(lamda*Signal1)/(np.exp	(lamda*Signal1) + np.exp(lamda * Signal2)))*(Wealth_Strengh == True)
    I1.ProbaH(Signal2)
    I2.ProbaH(Signal1)
    A1 = 1*(rd.random() < I1.pH)  # 1 = Hawk, 0 = Dove
    A2 = 1*(rd.random() < I2.pH)
    if A1 == 0 and A2 == 0:
        I1.w += int(v/2 + y/2)
        I2.w += int(v/2 + y/2)
    if A1 == 0 and A2 == 1:
        I1.w += int(y/2)
        I2.w += int(v + y/2)
    if A1 == 1 and A2 == 0:
        I1.w += int(v + y/2)
        I2.w += int(y/2)
    if A1 == 1 and A2 == 1:
        if rd.random()<f:
            I1.w += int(v+ y/2)
            I2.w += int(-c + y/2)
        else:
            I1.w += int(-c + y/2)
            I2.w += int(v + y/2)




Dico = {}
for i in range(N):
    I = Individual()
    I.name = i
    Dico[i] = I

def Event():
    global Dico
    if rd.random()< 1/2:
        rd.choice(Dico).Depreciation()
    else:
        A = 0
        B = 0
        while A == B:
            [A,B] = rd.choices(Dico,k=2)
        Jeu(A,B)

for i in range(T):
    print(i)
    Event()





Name = [I.name for I in Dico.values()]
Wealth = [I.w for I in Dico.values()]
HistoWealth = []
for i in range(max(Wealth) +1):
    HistoWealth.append(Wealth.count(i))

Mean = np.mean(Wealth)
Med = np.median(Wealth)

with open("SaveWithStrength.txt","w+") as file:
    for i in Wealth:
        file.write(str(i) + ",")

plt.plot(range(max(Wealth)+1),HistoWealth)
plt.savefig("Wealth Acc Strength.jpg")
plt.show()
