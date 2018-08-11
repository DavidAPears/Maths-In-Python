
# coding: utf-8

# Numbers

# In[6]:


5*5/2


# In[7]:


5+3.5


# In[8]:


2**3


# # *** Fractions ***

# In[10]:


from fractions import Fraction


# In[11]:


f3_2 = Fraction(3,2)


# In[12]:


f6_4 = Fraction(6,4)


# In[13]:


f12_15 = Fraction(12,15)


# In[14]:


f3_2 == f6_4


# In[15]:


f3_2 * f6_4


# In[16]:


1/f3_2


# In[17]:


3*f3_2


# In[18]:


f3_2 + f6_4


# In[19]:


float (f3_2 + f6_4)


# In[20]:


Fraction('0.12213')


# In[21]:


Fraction(0.12213)


# In[22]:


Fraction(0.1)


# In[23]:


import math


# In[24]:


pi_fraction = Fraction(math.pi)
print(pi_fraction)


# # *** Arbitrary Integer Precision***
# 
# Python has fantastic integer arthimatic, it can respect integers to arbitrrary
# 

# *** numbers ***

# a_float = 3.0**100.0
# 

# In[26]:


a_float = 3.0**100.0


# In[27]:


b_float = 3.0**100 + 1.0


# In[28]:


print(b_float - a_float)


# In[29]:


a = 3.0
#Take the 1000th root
root = a ** (1/1000)
print(root)


# In[30]:


root**1000


# In[31]:


root**1000 == 3.0


# In[32]:


def are_floats_equal(a,b):


# In[33]:


def are_floats_equal(a, b, delta):
    if a == 0 or b === 0:
        #Delta is an *absolute error. 
        return max(abs(a), abs(b)) <= delta
    else: 
        #elta is a *fractional error. 
        return( (a-b) / max( abs(a), abs(b) )) <= delta


# In[34]:


def are_floats_equal(a, b, delta):
    if a == 0 or b == 0:
        #Delta is an *absolute error. 
        return max(abs(a), abs(b)) <= delta
    else: 
        #elta is a *fractional error. 
        return( (a-b) / max( abs(a), abs(b) )) <= delta


# In[35]:


x = 0.0
y = 1E-9
print(are_floats_equal(x,y,1E-10))


# In[36]:


x = 0.0
y = 1E-12
print(are_floats_equal(x,y,1E-10))


# In[37]:


x = 9.1
y = 10.4
print(are_floats_equal(x,y,1E-10))


# # ***Arthimetic operations in 'perfect' maths are associative' ***
# 

# In[38]:


x = (0.1 + 0.2) + 0.3
y = 0.1 + (0.2 + 0.3)
x == y


# In[39]:


print('%.20f' %x)


# In[40]:


print('%.20f' %y)


# In[44]:


x = (0.5 + 0.25) + 0.125
y = 0.5 + (0.25 + 0.125)
x == y


# In[53]:


print('%.20f' %x)
print('%.20f' %y)


# In[54]:


#Any positive integer is either prime of can be writtern as a product of primes


# In[56]:


#Write a function to say whether one integer is a factor of another

def is_a_factor(dividend, candidate_factor):
    if dividend % candidate_factor == 0:
        return True
    else:
        return False
    


# In[57]:


print(is_a_factor(30,5))


# In[58]:


print(is_a_factor(dividend = 27, candidate_factor = 4))


# In[59]:


print(is_a_factor(12, candidate_factor = 3))


# In[64]:


import math
def simple_factorise(x):
    factors = []
    for number in range( x, 0, -1 ):
        if x % number == 0:
            factors.append(number)
    return factors


# In[65]:


get_ipython().run_line_magic('time', 'simple_factorise(100001)')


# In[67]:


x = 24 / 8
print(x)


# In[68]:


def slightly_better_factorise(x):
    factors = []
    low_limit = math.floor( math.sqrt(x) ) - 1
    for number in range( x, low_limit, -1 ):
        if x % number == 0:
            factors.append(number)
            cofactor = int( x / number)
            if cofactor != number:
                factors.append(cofactor)
    return factors


# In[69]:


get_ipython().run_line_magic('time', 'slightly_better_factorise(100001)')


# In[70]:


def even_better_factorise(x):
    factors = []
    high_limit = math.ceil( math.sqrt(x) ) + 1
    for number in range( 1, high_limit, 1 ):
        if x % number == 0:
            factors.append(number)
            cofactor = int( x / number)
            if cofactor != number:
                factors.append(cofactor)
    return factors


# In[71]:


get_ipython().run_line_magic('time', 'even_better_factorise(100001)')


# In[82]:


#  This routine writes the prime factors of a number

def prime_factors(x):
    x = int(x)
    factors = []
    high_limit = math.ceil( math.sqrt(x) ) + 1
    #Try two's first
    while x % 2 ==0:
        x = int( x / 2)
        factors.append(2)
    # Now, no even factors left, start at 3, try only odd factors
    for trial_factor in range(3, high_limit, 2):
        while x % trial_factor == 0:
            x = int( x / trial_factor)
            factors.append(trial_factor)
        if x == 1:
            break
        if x > 2:
            factors.append(x)
            return factors
    
    


# In[87]:


prime_factors(7)

