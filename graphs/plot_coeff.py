import matplotlib.pyplot as plt
import numpy as np

data = np.loadtxt('mfcc_2_3.txt')

plt.axis('equal')
plt.plot(data[:,0], data[:,1], marker = '+', mec = 'r', linestyle = 'None')


plt.title('MFCC')
plt.xlabel('2ndo coeficiente')
plt.ylabel('3r coeficiente')
plt.grid(True)
plt.show()