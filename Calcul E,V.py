import numpy as np
import matplotlib.pyplot as plt
v = 20
c = 40
y = 80
delta = 0.1

A = (v**2)/(2*c**2) * (3*c**2 + 2*c*v - v**2) + y/(2*c) * (2*v*c + y*c - v**2)

B = 2*v**2 / c**2 * (c**2 - 2*c*v + v**2) + 2*y/c *(v*c + y*c - 2*v**2)

def f_A (v,c,y,delta):
    A = (v**2)/(2*c**2) * (3*c**2 + 2*c*v - v**2) + y/(2*c) * (2*v*c + y*c - v**2)
    return A

def f_B(v,c,y,delta):
    B = 2*v**2 / c**2 * (c**2 - 2*c*v + v**2) + 2*y/c *(v*c + y*c - 2*v**2)
    return B

def f_alpha(v,c,y,delta):
    alpha = v/delta*(1 - v/c)
    return alpha


def E(v,c,y,delta):
    return f_alpha(v,c,y,delta) + y/delta

def V(v,c,y,delta):
    return f_A(v,c,y,delta)/delta + f_B(v,c,y,delta)/(delta**2)

def Ratio(v,c,y,delta):
    return np.sqrt(V(v,c,y,delta))/E(v,c,y,delta)


I_delta = list(np.linspace(0.1,1,100))
I_v = list(np.linspace(1,50))



bool = True

for v in I_v:
    I_c = list(np.linspace(2*v,4*v))
    print("v = {}".format(v) )
    for c in I_c:
        #print("c = {}".format(c))
        I_y = list(np.linspace(2*c,4*c))
        for y in I_y:
            J = [Ratio(v,c,y,I_delta[0])]
            for i in range(1,len(I_delta)):
                J.append(Ratio(v,c,y,I_delta[i]))
                bool = bool and (J[i] > J[i-1])
                if not bool:
                    break
