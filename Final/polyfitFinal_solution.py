import numpy as np
import matplotlib.pyplot as plt

#Create the x,y data pairs
#Fit polynomial functions of degree 1, 2 and 3
#Plot all on the same figure

x=np.linspace(-10,10,200)
y= 0.1* (x**3) - 0.5 * (x**2) - x + 20  + np.random.normal(1,5,x.shape[0])

plt.plot(x,y,'.',label='y=y(x)')

polyfits=[]

for i in [1,2,3]:
    coefs = np.polyfit(x,y,deg=i)
    polyfits.append(coefs)
    
for i in range(len(polyfits)):
    poly=np.poly1d(polyfits[i])
    plt.plot(x,poly(x),label='Poly. Ord. {}'.format(i+1))
    
plt.legend()
plt.show()

