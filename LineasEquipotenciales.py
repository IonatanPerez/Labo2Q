
# coding: utf-8

# Equipotenciales - Cuba

# In[3]:


import numpy as np
import matplotlib.pyplot as plt
import numpy.matlib as npm
from scipy import interpolate
from scipy.interpolate import griddata


# In[2]:


#Deben ingresar tres vectores o cargarlos desde un txt
#X,Y,Z: X,Y son las posiciones, Z es la diferencia de potencial

X = np.array([1, 1.2, 0.9, 1, 2.5, 2, 2.3, 1.8, 3, 3, 3, 3])
Y = np.array([1, 2.2, 3, 4.5, 1.5, 2, 3.6, 4, 1, 2.8, 3.1, 4])
Z = np.array([.11,.1,.11,.09,5.1,5.0,5.4,5.3,10.2,10.0,9.9,10.1])


# In[4]:


numIndexes = 100
ti = np.linspace(np.min(X), np.max(X),numIndexes)
tj = np.linspace(np.min(Y), np.max(Y),numIndexes)

xi,yi = np.meshgrid(ti,tj)
zi = griddata((X,Y),Z,(xi,yi),method='linear')

plt.figure()
plt.contour(xi,yi,zi,colors='k')
plt.contourf(xi,yi,zi)
plt.colorbar()
plt.title('Lineas equipotenciales')
plt.xlabel('X [cm]')
plt.ylabel('Y [cm]')
plt.show()

