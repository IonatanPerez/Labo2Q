
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

data = np.genfromtxt('prueba.csv', delimiter=",")
X = np.array(data[1:,0])
Y = np.array(data[1:,1])
Z = np.array(data[1:,2])


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

