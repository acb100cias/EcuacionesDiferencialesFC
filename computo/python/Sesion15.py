
# coding: utf-8

# In[126]:

from numpy import *
from matplotlib.pyplot import*
from scipy.integrate import*


# In[127]:

def s(t,c):
    return (200*t)/10. +c*(200-t)**(26)


# In[130]:

x=arange(0,200,0.1)
c=0.
plot(s(x,c))


# In[131]:

def f(s,t):
    return (5./2)-(26*s)/(200-t)


# In[132]:

x0=0
T=arange(0,200,0.1)
sim=odeint(f,x0,T)
plot(T,sim)
show()


# In[124]:




# In[125]:




# In[ ]:



