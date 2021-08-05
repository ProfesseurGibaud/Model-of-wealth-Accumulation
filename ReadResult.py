import matplotlib.pyplot as plt
import numpy as np


"""

Recover Data saved in :
- BM for the baseline model
- WS for the model when wealth is strength

"""

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



"""

Histogram creation


Comment line 50 to just see the wealth is strength
Comment line 51 to just see the baseline model
Change line 53 to change the name of the save

"""

HistoStrength = []
HistoWithout = []
for i in range(max(max(BM),max(WS)) +1):
    HistoStrength.append(WS.count(i))
    HistoWithout.append(BM.count(i))


bins = np.linspace(0, max(WS), 100)

plt.hist(BM, bins, alpha=1, label='Baseline model',color = "black",histtype = "step",linewidth = 3)
plt.hist(WS, bins, alpha=0.3, label='Wealth is strength model',color = "black",histtype = "bar")
plt.legend(loc='upper right')
plt.savefig("Compar.jpg")
plt.show()


"""

To compute statistical data type in the console.

- To have the gini coefficient of the base line type gini(BM) and for wealth is strength gini(WS)
- type np.mean, np.median, np.std, np.max to have the mean, median, standard deviation, maximum of the distribution of wealth you want (BM or WS).

"""


def gini(x):
    # (Warning: This is a concise implementation, but it is O(n**2)
    # in time and memory, where n = len(x).  *Don't* pass in huge  samples!)

    # Mean absolute difference
    mad = np.abs(np.subtract.outer(x, x)).mean()
    # Relative mean absolute difference
    rmad = mad/np.mean(x)
    # Gini coefficient
    g = 0.5 * rmad
    return g