import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys
import plot_func
# reload (plot_func)
import os
#~ root = 'D:/Nima/ABI/Python'
data = pd.read_csv('(17.03.2020)figure6.csv')
X_name = 'Glucose_l'
#~ X1_name = 'X2'
#~ X2_name = 'X3'
#~ X3_name = 'X3'
y_name = 'with A_GLUT2'
y1_name = 'without A_GLUT2'
y2_name = 'with A_GLUT2(N)'
y3_name = 'without A_GLUT2(N)'
# y4_name = 'Na_i'
# y5_name = 'K_i'
# y6_name = 'Cl_i'
# y7_name = 'v_ms'
# y8_name = 'J_W_A'
# y9_name = 'J_W_B'
# y10_name = 'v_cell'
# y8_name = 'glucose_m'
#~ y8_name = 'v_mc(Thorsen)'
#~ y9_name = 'v_sc(Thorsen)'
#~ y10_name = 'glucose_i(Thorsen)'
#~ y11_name = 'sodium_i(Thorsen)'
#~ y12_name = 'potassium_i(Thorsen)'
#~ y13_name = 'chloride_i(Thorsen)'



X = data[X_name]
#~ X1 = data[X1_name]
#~ X2 = data[X2_name]
#~ X3 = data[X3_name]
#~ data.set_index(X,inplace=True)
Y = data[y_name]
Y1 = data[y1_name]
Y2 = data[y2_name]
Y3 = data[y3_name]
# Y4 = data[y4_name]
# Y5 = data[y5_name]
# Y6 = data[y6_name]
# Y7 = data[y7_name]
# Y8 = data[y8_name]
# Y9 = data[y9_name]
# Y10 = data[y10_name]

# Y8 = data[y8_name]


plt.figure(figsize=(18,8))

# x, y = plot_func.smooth_func(X,Y8,3,1,kind='linear')
# plt.subplot(421)
# plt.plot(x, y, 'k',  label = 'Glucose Stimulus')
# plt.grid()
# plt.xlim(0, 600)
# #~ plt.ylim(0.0, 0.2)
# plt.xlabel ('time(s)')
# plt.ylabel ('Mucosal Concentration(mM)')
# plt.title('A')
# plt.legend(loc = 'best')


x, y = plot_func.smooth_func(X,Y,3,1,kind='linear')
plt.subplot(121)
plt.plot(x, y, 'k',linewidth = 2.5 , marker='d', markevery = slice(0,5000,100), label = 'With Apical GLUT2')

x, y = plot_func.smooth_func(X,Y1,3,1,kind='linear')
plt.subplot(121)
plt.plot(x, y, 'k', linewidth = 2.5, marker='o', markevery = slice(0,5000,100),  label = 'Without Apical GLUT2')

plt.grid()
plt.xlim(10,50)
plt.tick_params(axis='x', which='major', labelsize=15)
plt.tick_params(axis='y', which='major', labelsize=15)
#~ plt.ylim(0.0, 0.2)
plt.xlabel ('Luminal Glucose(mM)', fontsize = '14')
plt.ylabel ('Cell Volume(m3)', fontsize = '14')
plt.legend(loc = 'best', fontsize = '14')
plt.title('A')

x, y = plot_func.smooth_func(X,Y2,3,1,kind='linear')
plt.subplot(122)
plt.plot(x, y, 'k',linewidth = 2.5 , marker='d', markevery = slice(0,5000,100), label = 'With Apical GLUT2(Naftalin)')

x, y = plot_func.smooth_func(X,Y3,3,1,kind='linear')
plt.subplot(122)
plt.plot(x, y, 'k', linewidth = 2.5, marker='o', markevery = slice(0,5000,100),  label = 'Without Apical GLUT2(Naftalin)')

plt.grid()
plt.xlim(10,50)
plt.tick_params(axis='x', which='major', labelsize=15)
plt.tick_params(axis='y', which='major', labelsize=15)
#~ plt.ylim(0.0, 0.2)
plt.xlabel ('Luminal Glucose(mM)', fontsize = '14')
plt.ylabel ('Cell Volume(m3)', fontsize = '14')
plt.legend(loc = 'best', fontsize = '14')
plt.title('B')

# x, y = plot_func.smooth_func(X,Y7,3,1,kind='linear')
# plt.subplot(422)
# # plt.plot(x, y, 'k',  label = 'Transepithelial Potential')
# # plt.grid()
# # plt.xlim(0, 30000)
# # #~ plt.ylim(0.0, 0.2)
# # plt.xlabel ('time(s)')
# # plt.ylabel ('Membrane Potential(mV)')
# # plt.title('C')
# # plt.legend(loc = 'best')




#~ legend = ax.legend(loc='upper center', shadow=True)
#~ frame = legend.get_frame()
#~ frame.set_facecolor('0.90')
# Set the fontsize
#~ for label in legend.get_texts():
    #~ label.set_fontsize('small')
#~
#~ for label in legend.get_lines():
    #~ label.set_linewidth(1.5)  # the legend line width

#~ plt.xlim(0, 50)
#~ plt.ylim(0, 0.1)
#~ plt.xlabel ('')
#~ plt.ylabel ('')
#~ plt.title('Results')
#~ plt.xticks(np.arange(min(x), max(x)+1, 50))
#~ plt.legend(loc = 'best', fontsize='medium')
#~ plt.grid()
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)

plt.savefig('C:/Nima\ABI/2nd Paper/Figure06(17.03.2020).png')
plt.show()
#~ plt.legend(loc=0)
