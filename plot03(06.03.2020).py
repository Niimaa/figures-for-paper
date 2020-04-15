import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(12,8))
objects = ('Model', 'Experiment')
#~ y_pos = np.arange(len(objects))
X1 = (0)
ymin, ymax = 0, 7e-11
Y1 = [4.2e-11]

X2 = (0.2)
Y2 = [3.4e-11]
A2 = [5e-12]
A1 = [2e-12]
plt.subplot(132)
plt.bar(X1, Y1, align='center', yerr=A1, color='b', ecolor='black', capsize=10,  alpha=0.5, width = 0.2, label = 'Model')

plt.bar(X2, Y2, align='center', yerr=A2, color='r', ecolor='black', capsize=10,alpha=0.5, width = 0.2, label = 'Experiment')

plt.ylim(ymin, ymax)
plt.tick_params(axis='x', which='major', labelsize=15)
plt.tick_params(axis='y', which='major', labelsize=15)
#~ plt.xticks(y_pos, objects)
plt.ylabel('Sodium Absorption Rate(mmol/min)', fontsize ='14')
plt.xticks([])
plt.legend(loc = 'best', fontsize ='14')
plt.title('B')


#~ X1 = (0)
ymin, ymax = 0, 6e-11
Y3 = [3.1e-11]

#~ X2 = (0.2)
Y4 = [3.4e-11]
B4 = [5e-12]
B3 = [6e-12]
plt.subplot(131)
plt.bar(X1, Y3, yerr = B3, align='center', color='b',alpha=0.5, ecolor='black', capsize=10, width = 0.2, label = 'Model')
plt.bar(X2, Y4, yerr=B4, align='center', color='r',alpha=0.5, ecolor='black', capsize=10, width = 0.2, label = 'Experiment')
plt.ylim(ymin, ymax)
plt.tick_params(axis='x', which='major', labelsize=15)
plt.tick_params(axis='y', which='major', labelsize=15)
# plt.xticks(y_pos, objects)
plt.ylabel('Glucose Absorption Rate(mmol/min)', fontsize = '14')
plt.xticks([])
plt.legend(loc = 'best', fontsize ='14')
plt.title('A')


#~ X1 = (0)
ymin, ymax = 0, 0.8e-9
Y5 = [3.7e-10]

#~ X2 = (0.2)
Y6 = [4.18e-10]
C6 = [5e-11]
C5 = [1.2e-10]
plt.subplot(133)
plt.bar(X1, Y5, yerr = C5, align='center', color='b',alpha=0.5, ecolor='black', capsize=10, width = 0.2, label = 'Model')
plt.bar(X2, Y6, yerr=C6, align='center', color='r',alpha=0.5, ecolor='black', capsize=10, width = 0.2, label = 'Experiment')
plt.ylim(ymin, ymax)
# plt.xticks(y_pos, objects)
plt.ylabel('Water Absorption Rate(mmol/min)', fontsize ='14')
plt.tick_params(axis='x', which='major', labelsize=15)
plt.tick_params(axis='y', which='major', labelsize=15)
plt.xticks([])
plt.legend(loc = 'best', fontsize ='14')
plt.title('C')
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)
plt.savefig('C:/Nima\ABI/2nd Paper/Figure03(17.03.2020).png')
plt.show()