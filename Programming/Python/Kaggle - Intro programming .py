#!/usr/bin/env python
# coding: utf-8

# # Inspired by : Kaggle

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


# Function with arguments

def working_days(days, hours):
    no_of_days = days
    no_of_hours = hours
    total_billable = no_of_days*no_of_hours
    return total_billable


# In[3]:


print(working_days(5,8))


# In[4]:


# Function without arguments

def hello():
    print("Hello!")
    print("Please continue your work")


# In[5]:


hello()


# In[6]:


# Data types

var_int = 7
var_float = 7.5
var_string = "Hello!"
var_bool = True

print(type(var_int))
print(type(var_float))
print(type(var_string))
print(type(var_bool))


# In[7]:


# Conditional statements

def temp(val):
    if val > 38 :
        message = "Fever!"
    elif val > 35:
        message = "Normal"
    else:
        message = "Low temperature!"
    return message


# In[8]:


print(temp(37))


# # Intro to lists

# In[9]:


flower_list =['rose','lily','jasmine','sun-flower']
print(flower_list)
print(type(flower_list))


# In[10]:


print(flower_list[0]) # First element
print(flower_list[-1]) # Last element
print(flower_list[1:3]) # 2nd and 3rd element - Reads i to j-1 element 


# In[11]:


print(flower_list[:3]) # Reads i to j-1
print(flower_list[1:]) # Reads i to j


# In[12]:


print(len(flower_list))


# In[13]:


get_list = [1,2,3,4,5]
list_append = get_list.append(6)
list_extend = get_list.extend([7,8,9,10])
print(get_list)


# In[14]:


# Check append test

test_append = get_list.append([11,12])
print(get_list)


# In[15]:


get_list.remove([11,12])
print(get_list)


# In[16]:


print(sum(get_list)) # Sum
print(min(get_list)) # Min
print(max(get_list)) # Max


# In[17]:


print(get_list*3)


# In[ ]:




