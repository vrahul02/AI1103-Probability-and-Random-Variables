# Simulation to verify Q.104 using numpy
import random as rn
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom
from tabulate import tabulate

# Function which returns probabilities for a binomial distribution
def binomial(k):
    return binom.pmf(k,11,1/3)

# Variables to store the theoretical and simulation probalities seperately
prob_theo = [0 for i in range(12)]
prob_sim = [0 for j in range(12)]
num_sim = [0 for k in range(12)]

# Theoretical probability
for i in range(12):
    prob_theo[i] = binomial(i)

# Denoting 'success' as 0 and 'failure' as 1
assign = [0,1]

# Choosing our sample of 11 as the size of result of each outcome
num = 11

# Assigning 'success' and 'failure' probabilities
probabilities = [1/3,2/3]

# Declaring our simulation size
sim = 1000000
print("Let us run the simulation 1000000 times")

# Simulation probabilities
for i in range(sim):
    num_success = 0
    outcome = np.random.choice(assign,size = num,p = probabilities)
    for j in outcome:
        if j == 0:
            num_success += 1
    if num_success == 0:
        num_sim[0] += 1
    elif num_success == 1:
        num_sim[1] += 1
    elif num_success == 2:
        num_sim[2] += 1
    elif num_success == 3:
        num_sim[3] += 1
    elif num_success == 4:
        num_sim[4] += 1
    elif num_success == 5:
        num_sim[5] += 1
    elif num_success == 6:
        num_sim[6] += 1
    elif num_success == 7:
        num_sim[7] += 1
    elif num_success == 8:
        num_sim[8] += 1
    elif num_success == 9:
        num_sim[9] += 1
    elif num_success == 10:
        num_sim[10] += 1
    elif num_success == 11:
        num_sim[11] += 1

# Converting no of simulations to probablity
for i in range(12):
    prob_sim[i] = num_sim[i]/sim

# Printing results
print("Result of Simulation:")
data = [
[0,prob_sim[0],prob_theo[0]],
[1,prob_sim[1],prob_theo[1]],
[2,prob_sim[2],prob_theo[2]],
[3,prob_sim[3],prob_theo[3]],
[4,prob_sim[4],prob_theo[4]],
[5,prob_sim[5],prob_theo[5]],
[6,prob_sim[6],prob_theo[6]],
[7,prob_sim[7],prob_theo[7]],
[8,prob_sim[8],prob_theo[8]],
[9,prob_sim[9],prob_theo[9]],
[10,prob_sim[10],prob_theo[10]],
[11,prob_sim[11],prob_theo[11]]
]
print(tabulate(data,headers=["k", "Simulated", "Theoretical"]))
print("Thus the simulated probability is close to theoretical probability which we received using binomial distribution")

# Calculating k for which Pr(X=k) is maximum
max=prob_theo[0]
maxi=0
for i in range(12):
 if prob_theo[i] > max:
   max=prob_theo[i]
   maxi=i

print("Pr(X=k) is maximised for k =",maxi,end = '')

for i in range(12):
 if prob_theo[maxi] == prob_theo[i]:
   if (i != maxi):
     print(" ,",i,end = '')

# Plotting bar graph
cases = ["0","1","2","3","4","5","6","7","8","9","10","11"]
x = np.arange(len(cases))
plt.bar(x + 0.00, prob_theo, color = 'red', width = 0.25, label = 'Theoretical')
plt.bar(x + 0.25, prob_sim, color = 'yellow', width = 0.25, label = 'Simulated')
plt.xlabel('k')
plt.ylabel('Pr(X=k)')
plt.xticks(x  + 0.25/2,cases)
plt.legend()
plt.show()