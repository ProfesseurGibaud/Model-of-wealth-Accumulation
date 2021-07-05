import sympy as sp
v = sp.symbols('v')
c = sp.symbols('c')
y = sp.symbols('y')
t = sp.symbols('t')
delta = sp.symbols('delta',positive = True)
mm2 = sp.symbols('m2')
K1 = sp.symbols('K1')
pv2 = 2*(c-v)**2/c**2
pv = (2*(c-v)*v/(c**2) + (v/c)**2)
pc = (v/c)**2
py = (2*(c-v)*v/(c**2))


m1 = v*(c-v)/(delta*c) + y/delta + K1*sp.exp(-delta*t)
E = sp.limit(m1,K1,0)

MM2 = pv2*(mm2 + (v+y)*m1 + (v/2 + y/2)**2) + pv * (mm2 + 2*(v + y/2)*m1 + (v + y/2)**2) + pc*(mm2 + 2*(-c + y/2)*m1 + (-c + y/2)**2) + py*(mm2 + y*m1 + y**2/4) + (-2 - delta)*mm2

MM2 = sp.limit(MM2,K1,0)

Test1 = (2 * c**2 * delta) * MM2


Test2 = (c**2 * delta)*(- 2*delta * m2 + 3*v**2 + 2*v*y + y**2 + 2*v**3/c + 2*v**2*y/c - v**4/(c**2) + 4*v**2/delta + 8*v*y/delta +4*y**2/delta -8*v**3/(delta*c) - 8*v**2*y/(delta*c) + 4*v**4/(c**2*delta) )

Test2 = sp.limit(Test2,K1,0)













Tv2 = pv2*((v+y)*m1 + (v/2 + y/2)**2)
Tv = pv*((2*v + y)*m1 + (v + y/2)**2)
Tc = pc*((-2*c + y)*m1 + (-c+y/2)**2)
Ty = py*(y*m1 + y**2/4)

m2 = Tv2 + Tv + Tc + Ty


Var = m2 - m1**2
Limit = sp.limit(Var,K1,0)*(2*c**2*delta**2)
VarLimit = sp.latex(Limit)

Vy = y**2 * c**2 +2*y*c*v*(c-v)
Vartest = delta**2 * (Vy + v**2 *(3*c**2 + 2*c*v - v**2)) + 4*delta*(Vy + v**2*(c-v)**2) - 2*(Vy + v**2*(c-v)**2)

Ratio = sp.sqrt(Vartest)/E

Derivee = sp.diff(Ratio,delta)

Sim = sp.simplify(Derivee)














import numpy as np
v = 2
c = 4
y = 10
delta = 0.1
K1 = 1
t = 10000000


VarRR =(v**2/c**2 + v*(2*c - 2*v)/c**2)*((v + y/2)**2 + (2*v + y)*(K1*np.exp(-delta*t) + y/delta + v*(c - v)/(c*delta))) - (K1*np.exp(-delta*t) + y/delta + v*(c - v)/(c*delta))**2 + v**2*((-2*c + y)*(K1*np.exp(-delta*t) + y/delta + v*(c - v)/(c*delta)) + (-c + y/2)**2)/c**2 + v*(2*c - 2*v)*(y**2/4 + y*(K1*np.exp(-delta*t) + y/delta + v*(c - v)/(c*delta)))/c**2 + 2*(c - v)**2*((v/2 + y/2)**2 + (v + y)*(K1*np.exp(-delta*t) + y/delta + v*(c - v)/(c*delta)))/c**2

M2 = (v**2/c**2 + v*(2*c - 2*v)/c**2)*((v + y/2)**2 + (2*v + y)*(K1*np.exp(-delta*t) + y/delta + v*(c - v)/(c*delta))) + v**2*((-2*c + y)*(K1*np.exp(-delta*t) + y/delta + v*(c - v)/(c*delta)) + (-c + y/2)**2)/c**2 + v*(2*c - 2*v)*(y**2/4 + y*(K1*np.exp(-delta*t) + y/delta + v*(c - v)/(c*delta)))/c**2 + 2*(c - v)**2*((v/2 + y/2)**2 + (v + y)*(K1*np.exp(-delta*t) + y/delta + v*(c - v)/(c*delta)))/c**2


MM2 = (-2*c**2*delta**2*m2 + 2*c**2*delta*v**2 + 2*c**2*delta*v + c**2*delta*y**2 + 4*c**2*v**2 + 8*c**2*v*y + 4*c**2*y**2 + 4*c*delta*v**3 + 2*c*delta*v**2*y - 4*c*delta*v**2 - 8*c*v**3 - 8*c*v**2*y - 2*delta*v**4 - 2*delta*v**3*y + 2*delta*v**3 + 4*v**4)/(2*c**2*delta)