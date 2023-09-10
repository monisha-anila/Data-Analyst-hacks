#!/usr/bin/env python
# coding: utf-8

# # Inspired by : Kaggle 

# # Intro to Python

# In[1]:


spam_amount = 0
print(spam_amount)

# Ordering Spam, egg, Spam, Spam, bacon and Spam (4 more servings of Spam)
spam_amount = spam_amount + 4

if spam_amount > 0:
    print("But I don't want ANY spam!")

viking_song = "Spam " * spam_amount
print(viking_song)


# In[2]:


type(spam_amount)


# In[3]:


print(5/3) # True division similar to calculator
print(5//3) # Round-down to nearest integer


# In[4]:


# PEMDAS - Parentheses, Exponents, Multiplication/Division, Addition/Subtraction.

long_cal = (2+3)**2 + (5/5) + (3-2)
test_pemdas = 2+3**2 + 5/5 + 3-2

print(long_cal)
print(test_pemdas)


# In[5]:


print(abs(-10))


# # Functions and Getting help

# In[6]:


help(abs)


# In[7]:


def least_difference(a, b, c):
    """Return the smallest difference between any two numbers
    among a, b and c.
    
    >>> least_difference(1, 5, -5)
    4
    """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)


# In[8]:


print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7), # Python allows trailing commas in argument lists. How nice is that?
)


# In[9]:


help(least_difference)


# In[10]:


print(1,2,3, sep='<')


# In[11]:


def greet(who="Monisha"):
    print("Hello,", who)
    
greet()
greet(who="Kaggle")
# (In this case, we don't need to specify the name of the argument, because it's unambiguous.)
greet("Python")


# In[12]:


# Function applied to function

def num(x):
    return x*5

def get_num (fn,x):
    return fn(x)

def sq_num (fn,x):
    return fn(fn(x))

print(num(5))
print(get_num(num,5))
print(sq_num(num,5))


# # Boolean and conditionals

# In[13]:


def president_run(age,cond):
    if age >=35 and cond ==True :
        message = "yes"
    else:
        message ="no"
    return message

print(president_run(35,False))


# In[14]:


def number(x):
    if x<0:
        msg ="-ve number"
    elif x>0:
        msg ="+ve number"
    else:
        msg ="Neither -ve nor +ve number"
    return msg

print(number(0))
print(number(-1))
print(number(+1))


# In[15]:


# Boolean conversion

print(bool(0))
print(bool(1))
print(bool("")) # Empty string treated as False
print(bool("str"))


# # Lists

# In[16]:


# Indexing and slicing

list_num = [1,2,3,4,5]
print(list_num[0]) # 1st
print(list_num[-1]) # last
print(list_num[1:]) # i to last
print(list_num[1:4]) # i to j-1


# In[17]:


# List functions

print(len(list_num))
print(sorted([5,3,2,6,1]))
print(sum(list_num))
print(max(list_num))


# In[18]:


# List methods

planets = ['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune','Pluto']
print(planets.pop())
print(planets.append("Pluto!"))
print(planets.index("Earth"))
print("Mars" in planets)
print(planets)


# In[19]:


# Tuples 

x = 0.125
print(x.as_integer_ratio())

numerator, denominator = x.as_integer_ratio()
print(numerator / denominator)


# # Loops and list comprehension

# In[20]:


# For loop

for i in range(5):
    print(i)

# While loop    
i = 0     
while i<5:
    print(i)
    i = i+1


# In[21]:


squares = [n**2 for n in range(10)]
squares


# In[22]:


short_planets = [planet for planet in planets if len(planet) < 6]
short_planets


# In[23]:


# str.upper() returns an all-caps version of a string
loud_short_planets = [planet.upper() + '!' for planet in planets if len(planet) < 6]
loud_short_planets


# In[24]:


def count_negatives(nums):
    # Reminder: in the "booleans and conditionals" exercises, we learned about a quirk of 
    # Python where it calculates something like True + True + False + True to be equal to 3.
    return sum([num < 0 for num in nums])


# In[25]:


print(count_negatives([-1,2,-3,5,6,-10]))


# # Strings and dictionaries

# In[26]:


print('Pluto')
print('Pluto\'s not a planet')


# In[27]:


print('Hello,\n world!')


# In[28]:


# List properities applies to string 

word = "Python programming"
print(word[0])
print(word[3:])
print(len(word))


# In[29]:


# String methods

print(word.upper())
print(word.index('Python'))
print(word.startswith('Python'))
print(word.endswith('Python'))
print(word.split())


# In[30]:


planet = "Pluto"
position = 9


"{}, you'll always be the {}th planet to me.".format(planet, position)


# In[31]:


# Dictionaries 

numbers = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5}
print(numbers)


# In[32]:


numbers['six']= 6
print(numbers)


# In[33]:


numbers['one'] = 11
print(numbers)


# In[34]:


planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
planet_to_initial


# In[35]:


for k in numbers:
    print("{} = {}".format(k, numbers[k]))


# In[36]:


print(planet_to_initial.values())
print(planet_to_initial.keys())


# # External libraries

# In[37]:


import numpy as np
import pandas as pd
import math 


# In[38]:


rolls = np.random.randint(low=1, high=6, size=10)
print(rolls)


# In[39]:


type(rolls)


# In[40]:


dir(rolls)


# In[41]:


rolls+10


# In[42]:


rolls <=13

