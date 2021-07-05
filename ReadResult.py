import matplotlib.pyplot as plt
import numpy as np


with open("Strength.txt","r") as file:
    strL = file.read()
    strL = strL[:-1]
    WS =strL.split(",") #WS : list wealth with Strength


with open("WithoutStrength.txt","r") as file:
    strL = file.read()
    strL = strL[:-1]
    BM =strL.split(",") #BM : list wealth in base line model

for i in range(0,len(BM)):
    BM[i] = int(BM[i])
    WS[i] = int(WS[i])

HistoStrength = []
HistoWithout = []
for i in range(max(max(BM),max(WS)) +1):
    HistoStrength.append(WS.count(i))
    HistoWithout.append(BM.count(i))


bins = np.linspace(0, max(WS), 100)

plt.hist(BM, bins, alpha=1, label='Base Line Model',color = "black",histtype = "step",linewidth = 3)
#plt.hist(WS, bins, alpha=0.3, label='Wealth is Strength',color = "black",histtype = "bar")
plt.legend(loc='upper right')
#plt.savefig("Compar.jpg")
plt.show()
