import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys
import plot_func
# reload (plot_func)
import os
#~ root = 'D:/Nima/ABI/Python'
data = pd.read_csv('Figure02.csv')
# X_name = 'time'
# #~ X1_name = 'X2'
# #~ X2_name = 'X3'
# #~ X3_name = 'X3'
# y_name = 'pH_int'
# y1_name = 'v_mc'
# y2_name = 'v_sc'
# y3_name = 'glucose_i'
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


X = data[data.keys()[0]]
Y1 = data[data.keys()[1]]
Y2 = data[data.keys()[2]]
Y3 = data[data.keys()[4]]
Y4 = data[data.keys()[8]]
Y5 = data[data.keys()[3]]
Y6 = data[data.keys()[7]]
Y7 = data[data.keys()[9]]
Y8 = data[data.keys()[5]]
Y9 = data[data.keys()[6]]
Y10 = data[data.keys()[10]]

# X = data[X_name]
# #~ X1 = data[X1_name]
# #~ X2 = data[X2_name]
# #~ X3 = data[X3_name]
# #~ data.set_index(X,inplace=True)
# Y = data[y_name]
# Y1 = data[y1_name]
# Y2 = data[y2_name]
# Y3 = data[y3_name]
# Y4 = data[y4_name]
# Y5 = data[y5_name]
# Y6 = data[y6_name]
# Y7 = data[y7_name]
# Y8 = data[y8_name]
# Y9 = data[y9_name]
# Y10 = data[y10_name]

# Y8 = data[y8_name]


plt.figure(figsize=(10,12))

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


# x, y = plot_func.smooth_func(X,Y1,3,1,kind='linear')
plt.subplot(421)
plt.plot(X, Y1, 'k',  label = 'Apical Potential')

# x, y = plot_func.smooth_func(X,Y2,3,1,kind='linear')
plt.subplot(421)
plt.plot(X, Y2, 'k', linestyle='-.',  label = 'Basolateral Potential')

plt.grid()
plt.xlim(-100,6000)
#~ plt.ylim(0.0, 0.2)
plt.xlabel ('time(s)')
plt.ylabel ('Membrane Potential(mV)')
plt.title('A')
plt.legend(loc = 'best')
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
# x, y = plot_func.smooth_func(X,Y3,31,1,kind='linear')
plt.subplot(422)
plt.plot(X, Y3, 'k',  label = 'Glucose')
plt.grid()
plt.xlim(-100, 6000)
# ~ plt.ylim(0.0, 0.2)
plt.xlabel ('time(s)')
plt.ylabel ('Interacellular Concentration(mM)')
plt.title('B')
plt.legend(loc = 'best')

# x, y = plot_func.smooth_func(X,Y4,31,1,kind='linear')
plt.subplot(423)
plt.plot(X, Y4, 'k',  label = 'Sodium')
plt.grid()
plt.xlim(-100, 6000)
# plt.ylim(41.5, 43.5)
plt.xlabel ('time(s)')
plt.ylabel ('Interacellular Concentration(mM)')
plt.title('C')
plt.legend(loc = 'best')

x, y = plot_func.smooth_func(X,Y5,31,1,kind='linear')
plt.subplot(424)
plt.plot(X, Y5, 'k',  label = 'Potassium')
plt.grid()
plt.xlim(-100, 6000)
# plt.ylim(0, 130)
plt.xlabel ('time(s)')
plt.ylabel ('Interacellular Concentration(mM)')
plt.title('D')
plt.legend(loc = 'best')

# x, y = plot_func.smooth_func(X,Y6,31,1,kind='linear')
plt.subplot(425)
plt.plot(X, Y6, 'k', label = 'Chloride')
plt.grid()
plt.xlim(-100, 6000)
# plt.ylim(51, 52.5)
plt.xlabel ('time(s)')
plt.ylabel ('Interacellular Concentration(mM)')
plt.title('E')
plt.legend(loc = 'best')
# x, y = plot_func.smooth_func(X,Y,31,1,kind='linear')
plt.subplot(426)
plt.plot(X, Y7, 'k',  label = 'pH')
plt.grid()
plt.xlim(-100, 6000)
# plt.ylim(7.2, 7.23)
plt.xlabel ('time(s)')
plt.ylabel ('Intracellular pH')
plt.title('F')
plt.legend(loc = 'best')

# x, y = plot_func.smooth_func(X,Y8,3,1,kind='linear')
plt.subplot(427)
plt.plot(X, Y8, 'k', linestyle='-.',  label = 'J_w_A')

# x, y = plot_func.smooth_func(X,Y9,3,1, kind='linear')
plt.subplot(427)
plt.plot(X, Y9, 'k',  label = 'J_w_B')
plt.grid()
plt.xlim(-100, 6000)
#~ plt.ylim(0.0, 0.2)
plt.xlabel ('time(s)')
plt.ylabel ('Water Flux(Microm/s)')
plt.title('G')
plt.legend(loc = 'best')

# X, Y10 = plot_func.smooth_func(X,Y10,5,1,kind='linear')
plt.subplot(428)
plt.plot(X, Y10, 'k',  label = 'v_cell')


plt.grid()
plt.xlim(-100, 6000)
# plt.ylim(1.8e-15,2e-15)
plt.xlabel ('time(s)')
plt.ylabel ('Cell Volume(m3)')
plt.title('H')
plt.legend(loc = 'best')

#~ x, y = plot_func.smooth_func(X,Y7,3,1,kind='linear')
#~ plt.subplot(428)
#~ plt.plot(x, y, 'b',  label = 'pH')
#~ plt.grid()
#~ plt.xlim(0, 300)
#~ plt.ylim(0.0, 0.2)
#~ plt.xlabel ('time(s)')
#~ plt.ylabel ('Interacellular pH')
#~ plt.title('pH')
#~ plt.legend(loc = 'best')



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

plt.savefig('C:/Nima/ABI/2nd Paper/Figure02(17.03.2020).png')
plt.show()
#~ plt.legend(loc=0)
