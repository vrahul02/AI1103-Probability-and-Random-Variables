# Simulation to verify prob 1.5 using numpy
import random as rn
import numpy as np
import matplotlib.pyplot as plt

box1=[3,6,9,12,15]
box2=[6,11,16,21,26]

# Declaring our simulation size
sim=1000000
print("Let us run the simulation 1000000 times and check the number of cases in which product is an even number")

# Simulation probabilities
num_sim=0
for i in range(sim):
    b1=rn.choice(box1)
    b2=rn.choice(box2)
    b=b1*b2
    if b%2==0:
       num_sim+=1

# Printing results
print("Result of Simulation:")
print("The number of cases out of 1000000 in which product is an even number is",num_sim)
print("Thus the probability that product is an even number is",num_sim/sim)
print("And the simulated probability",num_sim/sim,"is close to",0.76,"which we received theoretically")

# Plotting bar graph
x = 0
plt.bar(x + 0, 0.76, color = 'red', width = 0.5, label = 'Theoretical')
plt.bar(x + 1, num_sim/sim, color = 'yellow', width = 0.5, label = 'Simulation')
plt.ylabel('Probabilities')
plt.legend()
plt.show()