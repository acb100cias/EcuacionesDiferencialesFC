#!/usr/bin/env python
# coding: utf-8

# # Oscilador de Van Der Pol
# 
# La ecuación diferencial de Van der Pol es
# 
# $$
# \frac{d^2 x}{dt^2} - \mu (1-x^2) \frac{dx}{dt} + x = 0
# $$
# 
# La ecuación describe un sistema con amortiguamiento no lineal, el grado de no linealidad dado por $\mu$. Si $\mu = 0$, el sistema es lineal y no amortiguado, pero a medida que $\mu$ aumenta, aumenta la fuerza de la no linealidad. Trazaremos el retrato de fase para la solución de la ecuación de Van der Pol en Python utilizando odeint.
# 

# In[4]:


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint



# **Sugerencia** Haga experimentos para distintos valores de $\mu$

# In[5]:


mu = 0.2

def van_der_pol_oscillator_deriv(x, t):
    nx0 = x[1]
    nx1 = -mu * (x[0] ** 2.0 - 1.0) * x[1] - x[0]
    res = np.array([nx0, nx1])
    return res



# In[ ]:


ts = np.linspace(0.0, 50.0, 500)

xs = odeint(van_der_pol_oscillator_deriv, [0.2, 0.2], ts)
plt.plot(xs[:,0], xs[:,1])
xs = odeint(van_der_pol_oscillator_deriv, [-3.0, -3.0], ts)
plt.plot(xs[:,0], xs[:,1])
xs = odeint(van_der_pol_oscillator_deriv, [4.0, 4.0], ts)
plt.plot(xs[:,0], xs[:,1])
plt.gca().set_aspect('equal')
#plt.savefig('vanderpol_oscillator.png')
plt.show() 

