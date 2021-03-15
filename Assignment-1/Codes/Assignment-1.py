# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hwq0Vir8iqHU7xdXKKBv7MhCnnwdmvE4
"""

# Simulation to verify prob 1.5 using numpy
import random as rn
import numpy as np
import matplotlib.pyplot
from scipy.stats import binom

def binomial(k):
    return binom.pmf(k,5,0.8)

prob_theo = [0 for i in range(6)]
prob_sim = [0 for j in range(6)]
for i in range(6):
    prob_theo[i] = binomial(i)



#denoting 'swimmer' as 0 and 'non swimmer' as 1
student = [0,1]
#choosing our sample of 5 students as the size of result of each outcome
num_student = 5
#assigning 'swimmer' and 'non swimmer' probabilities
probabilities = [0.8,0.2]

print("Let us run the simulation 1000000 times and check the number of cases in which 4 are swimmers")
#declaring our simulation size
sim = 1000000
for i in range(sim):
    num_swimmer = 0
    outcome = np.random.choice(student,size = num_student,p = probabilities)
    for j in outcome:
        if j == 0:
            num_swimmer += 1
    if num_swimmer == 0:
        prob_sim[0] += 1
    elif num_swimmer == 1:
        prob_sim[1] += 1
    elif num_swimmer == 2:
        prob_sim[2] += 1
    elif num_swimmer == 3:
        prob_sim[3] += 1
    elif num_swimmer == 4:
        prob_sim[4] += 1
    elif num_swimmer == 5:
        prob_sim[5] += 1
print("Result of Simulation:")
print("The number of cases out of 1000000 in which 4 students were swimmers is",prob_sim[4])
print("Thus the probability that 4 students were swimmers out of a random sample of 5 is",prob_sim[4]/sim)
print("And the simulated probability",prob_sim[4]/sim,"is close to",0.4096,"which we received using binomial distribution")

for i in range(6):
    prob_sim[i] = prob_sim[i]/sim

cases = ["0","1","2","3","4","5"]


x = np.arange(len(cases))
matplotlib.pyplot.bar(x + 0.00, prob_theo, color = 'red', width = 0.25, label = 'Calculated')
matplotlib.pyplot.bar(x + 0.25, prob_sim, color = 'yellow', width = 0.25, label = 'Simulated')
matplotlib.pyplot.xlabel('No of students who are swimmers')
matplotlib.pyplot.ylabel('Probabilities')
matplotlib.pyplot.xticks(x  + 0.25/2,cases)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()