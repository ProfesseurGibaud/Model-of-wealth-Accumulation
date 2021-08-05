import random as rd
import numpy as np

"""

Initialisation

"""

v = 20
c = 40
y = 100
delta = 0.1  # Delta
rho = 1/10 #Probability of dying with probability delta
N = 10000 # Number of individuals
T = 10000000 # Number of realisations of the Poisson process 


sigma = 10
Wealth_Strength = True # True = we simulate if wealth is strength, False we simulate the baseline model 
Wealth_Strength_mixed = False #True = Player plays H according to the Nash Equilibrium, False = Wealthier player plays H, Poorer plays D.

"""

We make a class of interacting individuals

"""

class Individual:
    def __init__(self):
        """
        
        An individual will have a wealth w, a name (which will be an index) and a probability of playing Hawk pH.

        """
        
        self.w = 0
        self.name = -1
        self.pH = -1
        
    def ProbaH(self,signal,v,c,y,delta):
        """
        

        Parameters
        ----------
        signal : integer
            the wealth of the other player
        y is not usefull here but letting it here, normalize the argument of the function
        delta is not usefull here but letting it here, normalize the argument of the function

        Returns
        -------
        
         We compute the probability of fighting : 
            if wealth is not strength, pH is 1/2
            else:
                if we look at our current wealth and the signal sent by the other player. pH is computed according to the probability given in the paper.

        """
    
        global Wealth_Strength,Wealth_Strength_mixed
        if not Wealth_Strength:
            self.pH = 1/2
        else:
            Signal1 = self.w
            Signal2 = signal
            if Wealth_Strength_mixed:
                if abs(Signal1 - Signal2)<np.log(c/v)/sigma:
                    f = np.exp(sigma*Signal1)/(np.exp	(sigma*Signal1) + np.exp(sigma * Signal2))
                    self.pH = v /(2*(v+c)*f-v)
                elif (Signal1 - Signal2)>np.log(c/v)/sigma:
                    self.pH = 1
                else: 
                    self.pH = 0
            else:
                if Signal1 > Signal2:
                    self.pH = 1
                elif Signal1 < Signal2:
                    self.pH = 0
                else:
                    self.pH = v/c

    def Depreciation(self,v,c,y,delta,rho):
        """


        Parameters
        ----------
        v is not usefull here but letting it here, normalize the argument of the function
        c is not usefull here but letting it here, normalize the argument of the function
        y is not usefull here but letting it here, normalize the argument of the function
        rho : real number between 0 and 1
            the probability of doing a drastic depreciation
        delta : real number between 0 and 1
            the depreciation parameter

        Returns
        -------
        
        we compute the depreciation of the wealth 's individual.

        """

        if rd.random()< rho:
            if rd.random()<delta:
                self.w = 0
        else:
            Z = np.random.binomial(self.w,delta)
            self.w = self.w - Z



def Jeu(I1,I2,v,c,y,delta):
    """
    

    Parameters
    ----------
    I1 : Object Individual
        Player 1
    I2 : Object Individual
        Player 2
    v : integer
    c : integer larger than v
    y : integer larger than 2c
    delta : real number between 0 and 1
    global Wealth_Strength : Boolean : False for baseline model, True when wealth is strength

    Returns
    -------
    We get the signals from the players. 
    If wealth is strength is True, then we compute the probability of player 1 winning (which is f). 
    Then we update (given the signals) the probability of playing hawks (for the players)
    Finally we update the wealth of the player

    """
    global Wealth_Strength

    Signal1 = I1.w
    Signal2 = I2.w
    if Wealth_Strength:
        f = (np.exp(sigma*Signal1)/(np.exp	(sigma*Signal1) + np.exp(sigma * Signal2)))
    else:
        f = 1/2
    I1.ProbaH(Signal2,v,c,y,delta)
    I2.ProbaH(Signal1,v,c,y,delta)
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



def make_dictionnary(N):
    """
    

    Parameters
    ----------
    N : Integer
        Size of the population.

    Returns
    -------
    Dico : dictionnary
        Dictionnary where the key is the name of an individual and the value is this individual.

    It is the function to create all the individuals
    """
    
    Dico = {}
    for i in range(N):
        I = Individual()
        I.name = i
        Dico[i] = I
    return Dico

Dico = make_dictionnary(N)

def Event(Dico,v,c,y,delta,rho):
    """
    

    Parameters
    ----------
    Dico : Dictionnary
        Dictionnary of players.
    v : integer
    c : integer bigger than v
    y : integer bigger than 2c
    delta : real number between 0 and 1
    rho : real number between 0 and 1
    global Wealth_Strength : Boolean : False for baseline model, True when wealth is strength

    Returns
    -------
    
    Event simulate a realisation of the main Poisson Process:
        with probability 1/2, depreciation occurs to a random individual
        with probability 1/2, two players A and B are drawn to play a game.

    """
    
    global Wealth_Strength
    if rd.random()< 1/2:
        rd.choice(Dico).Depreciation(v,c,y,delta,rho)
    else:
        A = 0
        B = 0
        while A == B:
            [A,B] = rd.choices(Dico,k=2)
        Jeu(A,B,v,c,y,delta)




def Simu(v,c,y,delta,rho,N,T):
    """
    

    Parameters
    ----------
    N : Number of individuals
    T : Number of events (realisation of Poisson Process)
    v : integer
    c : integer greater than v
    y : integer greater than 2c
    delta : real number between 0 and 1
    rho : real number between 0 and 1
    global Wealth_Strength : Boolean : False for baseline model, True when wealth is strength
    
    
    
    Returns
    -------
    Wealth : Vector of individuals' wealth
    mean :  mean of individual's wealth
    
    
    We make a dictionnary of all individuals, and we simulate T events. To finish we extract wealth of all individuals and comute the mean.

    """
    global Wealth_Strength
   
    Dico = make_dictionnary(N)
    for i in range(T):
        if i%10000==0:
            print(i/10000)
        Event(Dico,v,c,y,delta,rho)
    Wealth = [I.w for I in Dico.values()]
    mean = np.mean(Wealth)
    return Wealth,mean




def save(Wealth):
    """
    

    Parameters
    ----------
    Wealth : Vector of individual wealth
    global Wealth_Strength : Boolean : False for baseline model, True when wealth is strength
    
    Returns
    -------
    Save the wealth of individuals in : 
        Strength.txt if Wealth_Strength is True
        WithoutStrength.txt if Wealth_Strength is False

    """
    global Wealth_Strength
    if Wealth_Strength:
        with open("Strength.txt","w+") as file:
            for i in Wealth:
                file.write(str(i) + ",")
    else:
        with open("WithoutStrength.txt","w+") as file:
            for i in Wealth:
                file.write(str(i) + ",")


