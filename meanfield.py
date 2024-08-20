import random
import matplotlib.pyplot as plt
W_max = 1000
W_t = [0]*W_max
W_t[0] = 1
W = [W_t]


v = 20 
c = 40 
delta = 0.1
y = 100
T = 1000


W_max = 1000
W_t = [0]*W_max
W_t[0] = 1
stop = 0
W = [W_t]
for j in range(1,T):
    print("itération : ", j)
    W_t = [0]*W_max
    for w,masse in enumerate(W[j-1]):
        try:
            W_t[int(w + v/2 + y/2)] += 2*(1-v/c)**2 * masse
            W_t[int(w + v + y/2)] += 2*(v/c)*(1 - v/c)*masse
            W_t[int(w + y/2)] += 2*(v/c)*(1 - v/c)*masse
            W_t[int(w + v + y/2)] += (v/c)**2*masse
            W_t[int(w - c + y/2)] += (v/c)**2 * masse
            W_t[w] -= 2*masse
            if w > 0:
                W_t[w] -= delta*masse
            elif w == 0:
                W_t[w] += delta*masse - delta
            else:
                print("Error")
            W.append(W_t)
        except:
            pass
    if W_t != W[j-1]:
        plt.hist(W_t)
        plt.savefig(f"{j}.png")
    else:
        print("Chelou")