# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 12:14:50 2023

@author: gj
"""

from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

def ODE(x,t,k1, k2):
    dxdt = [x[1],-k1*x[1]-k2*x[0]]
    return dxdt

# Initial condition
x0 =[0.01, 0]

timePoints = np.linspace(1, 10, 400)
k1 = 2
k2 = 400

# we call the odeint() function
solutionOde = odeint(ODE,x0,timePoints, args=(k1, k2))

# plot solution
plt.plot(timePoints, solutionOde[:, 0], 'b', label = 'x1')
plt.plot(timePoints, solutionOde[:, 1], 'g', label = 'x2')
plt.legend(loc='best')
plt.xlabel('time')
plt.ylabel('x1(t), x2(t)')
plt.grid()
plt.savefig('Simulation.png')
plt.show()