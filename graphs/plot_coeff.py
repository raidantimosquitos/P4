import matplotlib.pyplot as plt
import numpy as np

lp = np.loadtxt('lp_2_3.txt')
lpcc = np.loadtxt('lpcc_2_3.txt')
mfcc = np.loadtxt('mfcc_2_3.txt')

plt.figure(1)
plt.axis('equal')
plt.plot(lp[:,0], lp[:,1], marker = '+', mec = 'r', linestyle = 'None')
plt.title('LP')
plt.xlabel('2o coef')
plt.ylabel('3r coef')
plt.grid(True)
plt.show()

plt.figure(2)
plt.axis('equal')
plt.plot(lpcc[:,0], lpcc[:,1], marker = '+', mec = 'b', linestyle = 'None')
plt.title('LPCC')
plt.xlabel('2o coef')
plt.ylabel('3r coef')
plt.grid(True)
plt.show()

plt.figure(3)
plt.axis('equal')
plt.plot(mfcc[:,0], mfcc[:,1], marker = '+', mec = 'g', linestyle = 'None')
plt.title('MFCC')
plt.xlabel('2o coef')
plt.ylabel('3r coef')
plt.grid(True)
plt.show()