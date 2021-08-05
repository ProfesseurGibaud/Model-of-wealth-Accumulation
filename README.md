# Model-of-wealth-Accumulation

We propose here a program in order to simulate the behaviour of the model of wealth accumulation described by Weibull and Gibaud (2017).

The preprint is described in ArXiv : https://arxiv.org/abs/1707.00996


In Individual systems program: 

The parameters are : 
- v,c,y,delta described in the Model
- N the number of individuals
- T the number of occurence of the main Poisson Process
- Wealth_Strength is a boolean. When it is True, the program simulates the Model when wealth is strengh (see Section 5).
- Wealth_Strength_mixed is a boolean. When it is True, player play the Nash Equilibrium (see Proposition 4), when it is False wealthier player plays Hawk, poorer plays Dove (equality they both play Hawk with probability v/c).
- sigma is the sigma used in Section Wealth is Strengh. 

The class Individual represents an individual. Attributes and methods are described in the program.

Fonction Simu lauches the simulation and returns the whole wealth distribution in a vector Wealth (it also prints every 10,000 iterations).

Fonction Save take in argument a wealth distribution (the former Wealth vector) and save it either in "Strength.txt" if Wealth_Strength is True, or in "WithoutStrength.txt" if Wealth_Strength is False.




In ReadResults program, you just have to run the program to see histograms and, after closing the diagram frame, type in the console the statistical data you want (instructions are given in the program).





The program needs to run the following libraries : random, matplotlib, numpy.

