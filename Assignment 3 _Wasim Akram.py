#!/usr/bin/env python
# coding: utf-8

# # Assignment -3  

# Task 1:
# 
# 1.
# 
# Write a function to compute 5/0 and use try/except to catch the exceptions.
# 

# In[3]:


def Div(num):

    try:
        if num/0:
            print(num)
    except:
        print("Number  can not be divide by Zero")
    else: 
        print("code working fine")
    finally:
        print("Practice is best way to learning")
Div(5)


# 2.
# 
# Implement a Python program to generate all sentences where subject is in ["Americans",
# "Indians"] and verb is in ["Play", "watch"] and the object is in ["Baseball","cricket"].
# 
# Hint: Subject,Verb and Object should be declared in the program as shown below.
# subjects=["Americans ","Indians"]
# verbs=["play","watch"]
# objects=["Baseball","Cricket"]
# 
# Output should come as below:
# Americans play Baseball.
# Americans play Cricket.
# Americans watch Baseball.
# Americans watch Cricket.
# Indians play Baseball.
# Indians play Cricket.
# Indians watch Baseball.
# Indians watch Cricket.

# In[1]:


subject=["Americans", "Indians"]
verb=["Play", "watch"]
obj=["Baseball","cricket"]
for i in subject:
    for j in verb:
        for k in obj:
            print(i+" "+j+" "+k,end='.\n')
print()


#  Q.3
#  
#  Write a function so that the columns of the output matrix are powers of the input vector.
# The order of the powers is determined by the increasing boolean argument. Specifically, when
# increasing is False, the i-th output column is the input vector raised element-wise to the power
# of N - i - 1.
# HINT: Such a matrix with a geometric progression in each row is named for Alexandre-
# Theophile Vandermonde.
# 

# In[4]:


import numpy as np


# In[11]:


x=np.array([1,2,3,4,5])
N=4

np.vander(x,N)


# In[122]:


def my_vander(vector,N,increasing=False):
    if not increasing:
        output_mat=np.array([x**(N-1-i)for x in vector for i in range(N)]).reshape(vector.size,N)
    else:
        output_mat=np.array([x**i for x in vector for i in range(N)]).reshape(vector.size,N)
        
    return output_mat
x=np.array([1,2,3,4,5])
N=3
print("Input vector= ",x)
print("Size of input vector= ", x.size)
print("the columns of the output matrix are powers of the input vector when increasing=False :", my_vander(x,N,increasing=False))
print("the columns of the output matrix are powers of the input vector when increasing=True :", my_vander(x,N,increasing=True))


# In[120]:


x.size


# In[ ]:




