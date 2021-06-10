import matplotlib.pyplot as plt
import numpy as np


with open("SaveWithStrength.txt","r") as file:
    strL = file.read()
    strL = strL[:-1]
    WS =strL.split(",") #WS : list wealth with Strength


with open("SaveWithoutStrength.txt","r") as file:
    strL = file.read()
    strL = strL[:-1]
    BM =strL.split(",") #BM : list wealth in base line model

for i in range(0,len(BM)):
    BM[i] = int(BM[i])
    WS[i] = int(WS[i])

