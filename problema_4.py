import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

datos = np.loadtxt("tabla.dat",delimiter=" ")

x = datos[:,0]
y = datos[:,1]

def lineal(t,a,b):
    return a*t+b

parametros = curve_fit(lineal,x,y) 

t = np.linspace(4,10,50)

a,b = parametros[0]

print("pendiente=",a,"Ordenada=",b)
plt.figure(figsize=(9, 6))
plt.scatter(x, y, color='r', label='Datos')
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(t, lineal(t, a, b),label='Linear_Fit')
plt.savefig('dataFitted.pdf', bbox_inches=0, dpi=600)
plt.show()


