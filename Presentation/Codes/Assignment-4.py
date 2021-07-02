# Simulation to verify GATE 2021 (ST), Q.15 using numpy
import random as rn
import numpy as np
import matplotlib.pyplot

# Variables to store the theoretical and simulation probalities seperately
prob_theo_sum = [0 for i in range(2,13)]
prob_theo_diff= [0 for i in range(-5,6)]
prob_sim_sum = [0 for i in range(2,13)]
prob_sim_diff = [0 for i in range(-5,6)]
num_sim_sum = [0 for i in range(2,13)]
num_sim_diff = [0 for i in range(-5,6)]

# Variables for calculating expectation value
total_sim=0
num_sim=0
expect_sim=0

# Calculating theoretical probabilities
for i in range(2,13):
  for j in range(i-6,i):
    if j>=1 and j<=6:
      prob_theo_sum[i-2]+=1/36

for i in range(-5,6):
  for j in range(i+1,i+7):
    if j>=1 and j<=6:
      prob_theo_diff[i+5]+=1/36

# Declaring our simulation size
sim = 1000000
print("Let us run the simulation 1000000 times")

# Running simulation 
for i in range(sim):
    die1=rn.randint(1,6)
    die2=rn.randint(1,6)
    sum=die1+die2
    diff=die1-die2
    num_sim_sum[sum-2]+=1
    num_sim_diff[diff+5]+=1
    if diff==1 or diff==-1:
      total_sim+=sum
      num_sim+=1

# Converting no of simulations to probablity
for i in range(2,13):
    prob_sim_sum[i-2] = num_sim_sum[i-2]/sim

for i in range(-5,6):
  prob_sim_diff[i+5] = num_sim_diff[i+5]/sim

# Calculating expected value
expect_sim=total_sim/num_sim

# Printing results
print("Result of Simulation:")
print("The simulated expectation value",expect_sim,"is close to",7,"which we received theoretically")

# Plotting bar graph for sum
cases = ["2","3","4","5","6","7","8","9","10","11","12"]
x = np.arange(len(cases))
matplotlib.pyplot.bar(x + 0.00, prob_theo_sum, color = 'red', width = 0.25, label = 'Calculated')
matplotlib.pyplot.bar(x + 0.25, prob_sim_sum, color = 'yellow', width = 0.25, label = 'Simulated')
matplotlib.pyplot.xlabel('X + Y')
matplotlib.pyplot.ylabel('Probabilities')
matplotlib.pyplot.xticks(x  + 0.25/2,cases)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()

# Plotting bar graph for difference
cases = ["-5","-4","-3","-2","-1","0","1","2","3","4","5"]
x = np.arange(len(cases))
matplotlib.pyplot.bar(x + 0.00, prob_theo_diff, color = 'red', width = 0.25, label = 'Calculated')
matplotlib.pyplot.bar(x + 0.25, prob_sim_diff, color = 'yellow', width = 0.25, label = 'Simulated')
matplotlib.pyplot.xlabel('X - Y')
matplotlib.pyplot.ylabel('Probabilities')
matplotlib.pyplot.xticks(x  + 0.25/2,cases)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()
