#!/usr/bin/env python
# coding: utf-8

# ## PROOFS
# 
# Samanata Silwal 
# 
# 274779
# 
# CPSMA-3913-01
# 
# Module 8 (Final Project)
# 
# Dr. Matthew Lynam

# 1. Typeset a small proof
# 
# (a) Create a linear equation y = mx+b by assigning non-zero values to m and b. Graph this function.
# (b) Write a proof of the statement
# (0, b) is the y-intercept for the function y = mx + b
# 
# 2. Be sure to comment on the following:
# (a) Describe your findings in words.
# (b) Discuss the steps in your proof. Remember finding a value is different from proving that value
# works.

# In[1]:


# Given the independent variable values, x
equa = 20
x = [x for x in range(1,equa+1)]

# Giving values for m and b
m = 3
b = 7

# Assess the values of the dependent variable, y
y = [m*y+b for y in x]

# Import matplotlib.pyplot for plotting
from matplotlib import pyplot as plt

# Ploting y against x
plt.plot(x,y)

# Adding the title, x Label and y label for the plot
plt.xlabel("Independent variable / x")
plt.ylabel("Dependent variable / y")
plt.title("y = mx + b")

# Ploting the graph
plt.show()

The y-intercept for the function y = mx + b is (0, b).

The y-intercept of the function y = mx + b is given by the statement (0, b).


Proof:

    It is assumed that (0,b). As a result, the x coordinate is 0 and the y coordinate is b. When the x coordinate is equal to zero. The y intercept will be represented by the y coordinate, which is shown below. y = mx + b when x = 0.
y = m0 + b because m*0 = 0 y = 0 + b b + 0 = 0\s   y = b 
    
    As a result, the function's y intercept coordinate will be (0,b).