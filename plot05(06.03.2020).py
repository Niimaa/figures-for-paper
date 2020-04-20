import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys
import plot_func
# reload (plot_func)
import os
#~ root = 'D:/Nima/ABI/Python'
data = pd.read_csv('Figure_05.csv')


# X = data[X_name]


X = data[data.keys()[0]]
Y1 = data[data.keys()[33]]
Y2 = data[data.keys()[34]]
Y3 = data[data.keys()[35]]
Y4 = data[data.keys()[36]]

Y5 = data[data.keys()[29]]
Y6 = data[data.keys()[30]]
Y7 = data[data.keys()[31]]
Y8 = data[data.keys()[32]]

Y9 = data[data.keys()[25]]
Y10 = data[data.keys()[26]]
Y11 = data[data.keys()[27]]
Y12 = data[data.keys()[28]]

Y13 = data[data.keys()[21]]
Y14 = data[data.keys()[22]]
Y15 = data[data.keys()[23]]
Y16 = data[data.keys()[24]]

Y17 = data[data.keys()[37]]
Y18 = data[data.keys()[38]]
Y19 = data[data.keys()[39]]
Y20 = data[data.keys()[40]]

Y21 = data[data.keys()[1]]
Y22 = data[data.keys()[2]]
Y23 = data[data.keys()[3]]
Y24 = data[data.keys()[4]]

Y25 = data[data.keys()[5]]
Y26 = data[data.keys()[6]]
Y27 = data[data.keys()[7]]
Y28 = data[data.keys()[8]]

Y29 = data[data.keys()[9]]
Y30 = data[data.keys()[10]]
Y31 = data[data.keys()[11]]
Y32 = data[data.keys()[12]]

Y33 = data[data.keys()[13]]
Y34 = data[data.keys()[14]]
Y35 = data[data.keys()[15]]
Y36 = data[data.keys()[16]]

Y37 = data[data.keys()[17]]
Y38 = data[data.keys()[18]]
Y39 = data[data.keys()[19]]
Y40 = data[data.keys()[20]]



plt.figure(figsize=(14,14))


# X, Y1 = plot_func.smooth_func(X,Y1,31,1,kind='linear')
plt.subplot(251)
plt.plot(X, Y1, 'k', linestyle='-',  marker='d', markevery = slice(30,10000,600),  label = 'NaCl=130')
#
# x, y = plot_func.smooth_func(X,Y3,3,1,kind='linear')
plt.subplot(251)
plt.plot(X, Y2, 'k', linestyle='-',  marker='o', markevery = slice(30,10000,600),  label = 'NaCl=100')
#
# x, y = plot_func.smooth_func(X,Y56,3,1,kind='linear')
plt.subplot(251)
plt.plot(X, Y3, 'k', linestyle='-',  marker='+', markevery = slice(30,10000,600), label = 'NaCl=70')

# x, y = plot_func.smooth_func(X,Y4,3,1,kind='linear')
plt.subplot(251)
plt.plot(X, Y4, 'k', linestyle='-',  marker='^', markevery = slice(30,10000,600), label = 'NaCl=40')

# x, y = plot_func.smooth_func(X,Y5,3,1,kind='linear')
# plt.subplot(231)
# plt.plot(x, y, 'k',linestyle='-', marker='x', markevery = slice(30,3000,50),  label = 'G_l=200')

plt.grid()
plt.xlim(0, 10000,5000)
plt.tick_params(axis='x', which='major', labelsize=13)
plt.tick_params(axis='y', which='major', labelsize=13)
plt.ylim(1e-15, 6e-15)
plt.xlabel ('time(s)', fontsize = '14')
plt.ylabel ('Cell volume (m3)', fontsize = '14')
plt.title('A')
plt.legend(loc = 'upper left', fontsize = '12')


# x, y = plot_func.smooth_func(X,Y49,3,1,kind='linear')
# plt.subplot(232)
# plt.plot(x, y, 'k', linestyle ='-', marker='.', markevery = slice(10,3000,50),  label = 'G_l=5')

# x, y = plot_func.smooth_func(X,Y7,3,1,kind='linear')
# plt.subplot(242)
# plt.plot(x, y, 'k', linestyle='-',  marker='+', markevery = slice(10,3000,50),  label = 'G_l=10')

# x, y = plot_func.smooth_func(X,Y8,3,1,kind='linear')
plt.subplot(252)
plt.plot(X, Y5, 'k', linestyle='-',  marker='d', markevery = slice(30,10000,600),  label = 'NaCl=130')
#
# x, y = plot_func.smooth_func(X,Y9,3,1,kind='linear')
plt.subplot(252)
plt.plot(X, Y6, 'k', linestyle='-',  marker='o', markevery = slice(30,10000,600),  label = 'NaCl=100')

#
# x, y = plot_func.smooth_func(X,Y57,3,1,kind='linear')
plt.subplot(252)
plt.plot(X, Y7, 'k', linestyle='-',  marker='+', markevery = slice(30,10000,600), label = 'NaCl=70')

# x, y = plot_func.smooth_func(X,Y10,3,1,kind='linear')
plt.subplot(252)
plt.plot(X, Y8, 'k', linestyle='-',  marker='^', markevery = slice(30,10000,600), label = 'NaCl=40')

# x, y = plot_func.smooth_func(X,Y11,3,1,kind='linear')
# plt.subplot(232)
# plt.plot(x, y, 'k',linestyle='-', marker='x', markevery = slice(10,3000,50),  label = 'G_l=200')

plt.grid()
plt.xlim(0, 10000)
plt.tick_params(axis='x', which='major', labelsize=13)
plt.tick_params(axis='y', which='major', labelsize=13)
plt.ylim(0, 10)
plt.xlabel ('time(s)', fontsize = '14')
plt.ylabel ('Intracellular Glucose Concentration(mM)', fontsize = '14')
plt.title('B')
plt.legend(loc = 'upper left', fontsize = '12')


# x, y = plot_func.smooth_func(X,Y62,3,1,kind='linear')
plt.subplot(253)
plt.plot(X, Y9, 'k', linestyle='-',  marker='d', markevery = slice(30,10000,600),  label = 'NaCl=130')
#
# x, y = plot_func.smooth_func(X,Y64,3,1,kind='linear')
plt.subplot(253)
plt.plot(X, Y10, 'k', linestyle='-',  marker='o', markevery = slice(30,10000,600),  label = 'NaCl=100')

#
# x, y = plot_func.smooth_func(X,Y66,3,1,kind='linear')
plt.subplot(253)
plt.plot(X, Y11, 'k', linestyle='-',  marker='+', markevery = slice(30,10000,600), label = 'NaCl=70')

# x, y = plot_func.smooth_func(X,Y68,3,1,kind='linear')
plt.subplot(253)
plt.plot(X, Y12, 'k', linestyle='-',  marker='^', markevery = slice(30,10000,600), label = 'NaCl=40')

# x, y = plot_func.smooth_func(X,Y11,3,1,kind='linear')
# plt.subplot(232)
# plt.plot(x, y, 'k',linestyle='-', marker='x', markevery = slice(10,3000,50),  label = 'G_l=200')

plt.grid()
plt.xlim(0, 10000)
plt.tick_params(axis='x', which='major', labelsize=13)
plt.tick_params(axis='y', which='major', labelsize=13)
plt.ylim(15, 60)
plt.xlabel ('time(s)', fontsize = '14')
plt.ylabel ('Intracellular Sodium Concentration(mM)', fontsize = '14')
plt.title('C')
plt.legend(loc = 'upper left', fontsize = '12')


# x, y = plot_func.smooth_func(X,Y63,3,1,kind='linear')
plt.subplot(254)
plt.plot(X, Y13, 'k', linestyle='-',  marker='d', markevery = slice(30,10000,600),  label = 'NaCl=130')
#
# x, y = plot_func.smooth_func(X,Y65,3,1,kind='linear')
plt.subplot(254)
plt.plot(X, Y14, 'k', linestyle='-',  marker='o', markevery = slice(30,10000,600),  label = 'NaCl=100')

#
# x, y = plot_func.smooth_func(X,Y67,3,1,kind='linear')
plt.subplot(254)
plt.plot(X, Y15, 'k', linestyle='-',  marker='+', markevery = slice(30,10000,600), label = 'NaCl=70')

# x, y = plot_func.smooth_func(X,Y69,3,1,kind='linear')
plt.subplot(254)
plt.plot(X, Y16, 'k', linestyle='-',  marker='^', markevery = slice(30,10000,600), label = 'NaCl=40')

# x, y = plot_func.smooth_func(X,Y11,3,1,kind='linear')
# plt.subplot(232)
# plt.plot(x, y, 'k',linestyle='-', marker='x', markevery = slice(10,3000,50),  label = 'G_l=200')

plt.grid()
plt.xlim(0, 10000)
plt.tick_params(axis='x', which='major', labelsize=13)
plt.tick_params(axis='y', which='major', labelsize=13)
plt.ylim(20, 70)
plt.xlabel ('time(s)', fontsize = '14')
plt.ylabel ('Intracellular Chloride Concentration(mM)', fontsize = '14')
plt.title('D')
plt.legend(loc = 'upper left', fontsize = '12')

# x, y = plot_func.smooth_func(X,Y50,3,1,kind='linear')
# plt.subplot(233)
# plt.plot(x, y, 'k', linestyle ='-', marker='.', markevery = slice(10,3000,50),  label = 'G_l=5')

# x, y = plot_func.smooth_func(X,Y13,3,1,kind='linear')
# plt.subplot(243)
# plt.plot(x, y, 'k', linestyle='-',  marker='+', markevery = slice(10,3000,50),  label = 'G_l=10')

# x, y = plot_func.smooth_func(X,Y14,3,1,kind='linear')
plt.subplot(2,5,5)
plt.plot(X, Y17, 'k', linestyle='-',  marker='d', markevery = slice(30,10000,600),  label = 'NaCl=130')

# x, y = plot_func.smooth_func(X,Y15,3,1,kind='linear')
plt.subplot(2,5,5)
plt.plot(X, Y18, 'k', linestyle='-',  marker='o', markevery = slice(30,10000,600),  label = 'NaCl=100')
#
# x, y = plot_func.smooth_func(X,Y58,3,1,kind='linear')
plt.subplot(2,5,5)
plt.plot(X, Y19, 'k', linestyle='-',  marker='+', markevery = slice(30,10000,600), label = 'NaCl=70')

# x, y = plot_func.smooth_func(X,Y16,3,1,kind='linear')
plt.subplot(2,5,5)
plt.plot(X, Y20, 'k', linestyle='-',  marker='^', markevery = slice(30,10000,600), label = 'NaCl=40')

# x, y = plot_func.smooth_func(X,Y17,3,1,kind='linear')
# plt.subplot(233)
# plt.plot(x, y, 'k',linestyle='-', marker='x', markevery = slice(10,3000,50),  label = 'G_l=200')

plt.grid()
plt.xlim(0, 10000)
plt.tick_params(axis='x', which='major', labelsize=13)
plt.tick_params(axis='y', which='major',  labelsize=13)
plt.ticklabel_format(axis='y', style='sci',  scilimits=(-6,-6))
# plt.yaxis.major.formatter._useMathText = True
plt.ylim(-3e-7, -30e-7)
# plt.yticks(np.arange(0,0.0000006,0.00000002))
plt.xlabel ('time(s)', fontsize = '14')
plt.ylabel ('Apical water flux (umol/sec)', fontsize = '14')
plt.title('E')
plt.legend(loc = 'upper left', fontsize = '12')


# x, y = plot_func.smooth_func(X,Y20,3,1,kind='linear')
plt.subplot(256)
plt.plot(X, Y21, 'k', linestyle='-',  marker='d', markevery = slice(30,10000,600),  label='NaCl=130')
#
# x, y = plot_func.smooth_func(X,Y21,3,1,kind='linear')
plt.subplot(256)
plt.plot(X, Y22, 'k', linestyle='-',  marker='o', markevery = slice(30,10000,600),  label='NaCl=100')
#
# x, y = plot_func.smooth_func(X,Y59,3,1,kind='linear')
plt.subplot(256)
plt.plot(X, Y23, 'k', linestyle='-',  marker='+', markevery = slice(30,10000,600), label='NaCl=70')

# x, y = plot_func.smooth_func(X,Y22,3,1,kind='linear')
plt.subplot(256)
plt.plot(X, Y24, 'k', linestyle='-',  marker='^', markevery = slice(30,10000,600), label='NaCl=40')

# x, y = plot_func.smooth_func(X,Y23,3,1,kind='linear')
# plt.subplot(234)
# plt.plot(x, y, 'k',linestyle='-', marker='x', markevery = slice(10,3000,50),  label = 'G_l=200')

plt.grid()
plt.xlim(0, 10000)
plt.tick_params(axis='x', which='major', labelsize=13)
plt.tick_params(axis='y', which='major', labelsize=13)
plt.ylim(1e-15, 6e-15)
plt.xlabel ('time(s)', fontsize = '14')
plt.ylabel ('Cell volume (m3)', fontsize = '14')
plt.title('F')
plt.legend(loc = 'upper left', fontsize = '12')


# x, y = plot_func.smooth_func(X,Y53,3,1,kind='linear')
# plt.subplot(235)
# plt.plot(x, y, 'k', linestyle ='-', marker='.', markevery = slice(10,3000,50),  label = 'G_l=5')

# x, y = plot_func.smooth_func(X,Y25,3,1,kind='linear')
# plt.subplot(246)
# plt.plot(x, y, 'k', linestyle='-',  marker='+', markevery = slice(10,3000,50),  label = 'G_l=10')

# x, y = plot_func.smooth_func(X,Y26,3,1,kind='linear')
plt.subplot(257)
plt.plot(X, Y25, 'k', linestyle='-',  marker='d', markevery = slice(30,10000,600),  label='NaCl=130')
#
# x, y = plot_func.smooth_func(X,Y27,3,1,kind='linear')
plt.subplot(257)
plt.plot(X, Y26, 'k', linestyle='-',  marker='o', markevery = slice(30,10000,600),  label='NaCl=100')
#
# x, y = plot_func.smooth_func(X,Y60,3,1,kind='linear')
plt.subplot(257)
plt.plot(X, Y27, 'k', linestyle='-',  marker='+', markevery = slice(30,10000,600), label='NaCl=70')

# x, y = plot_func.smooth_func(X,Y28,3,1,kind='linear')
plt.subplot(257)
plt.plot(X, Y28, 'k', linestyle='-',  marker='^', markevery = slice(30,10000,600), label='NaCl=40')

# x, y = plot_func.smooth_func(X,Y29,3,1,kind='linear')
# plt.subplot(235)
# plt.plot(x, y, 'k',linestyle='-', marker='x', markevery = slice(10,3000,50),  label = 'G_l=200')

plt.grid()
plt.xlim(0, 10000)
plt.tick_params(axis='x', which='major', labelsize=13)
plt.tick_params(axis='y', which='major', labelsize=13)
plt.ylim(0, 10)
plt.xlabel ('time(s)', fontsize = '14')
plt.ylabel ('Intracellular Glucose Concentration(mM)', fontsize = '14')
plt.title('G')
plt.legend(loc = 'upper left', fontsize = '12')

# x, y = plot_func.smooth_func(X,Y70,3,1,kind='linear')
plt.subplot(258)
plt.plot(X, Y29, 'k', linestyle='-',  marker='d', markevery = slice(30,10000,600),  label='NaCl=130')
#
# x, y = plot_func.smooth_func(X,Y72,3,1,kind='linear')
plt.subplot(258)
plt.plot(X, Y30, 'k', linestyle='-',  marker='o', markevery = slice(30,10000,600),  label='NaCl=100')
#
# x, y = plot_func.smooth_func(X,Y74,3,1,kind='linear')
plt.subplot(258)
plt.plot(X, Y31, 'k', linestyle='-',  marker='+', markevery = slice(30,10000,600), label='NaCl=70')

# x, y = plot_func.smooth_func(X,Y76,3,1,kind='linear')
plt.subplot(258)
plt.plot(X, Y32, 'k', linestyle='-',  marker='^', markevery = slice(30,10000,600), label='NaCl=40')

# x, y = plot_func.smooth_func(X,Y29,3,1,kind='linear')
# plt.subplot(235)
# plt.plot(x, y, 'k',linestyle='-', marker='x', markevery = slice(10,3000,50),  label = 'G_l=200')

plt.grid()
plt.xlim(0, 10000)
plt.tick_params(axis='x', which='major', labelsize=13)
plt.tick_params(axis='y', which='major', labelsize=13)
plt.ylim(15, 60)
plt.xlabel ('time(s)', fontsize = '14')
plt.ylabel ('Intracellular Sodium Concentration(mM)', fontsize = '14')
plt.title('H')
plt.legend(loc = 'upper left', fontsize = '12')


# x, y = plot_func.smooth_func(X,Y71,3,1,kind='linear')
plt.subplot(259)
plt.plot(X, Y33, 'k', linestyle='-',  marker='d', markevery = slice(30,10000,600),  label='NaCl=130')
#
# x, y = plot_func.smooth_func(X,Y73,3,1,kind='linear')
plt.subplot(259)
plt.plot(X, Y34, 'k', linestyle='-',  marker='o', markevery = slice(30,10000,600),  label='NaCl=100')
#
# x, y = plot_func.smooth_func(X,Y75,3,1,kind='linear')
plt.subplot(259)
plt.plot(X, Y35, 'k', linestyle='-',  marker='+', markevery = slice(30,10000,600), label='NaCl=70')

# x, y = plot_func.smooth_func(X,Y77,3,1,kind='linear')
plt.subplot(259)
plt.plot(X, Y36, 'k', linestyle='-',  marker='^', markevery = slice(30,10000,600), label ='NaCl=40')

# x, y = plot_func.smooth_func(X,Y29,3,1,kind='linear')
# plt.subplot(235)
# plt.plot(x, y, 'k',linestyle='-', marker='x', markevery = slice(10,3000,50),  label = 'G_l=200')

plt.grid()
plt.xlim(0, 10000)
plt.tick_params(axis='x', which='major', labelsize=13)
plt.tick_params(axis='y', which='major', labelsize=13)
plt.ylim(20, 70)
plt.xlabel ('time(s)', fontsize = '14')
plt.ylabel ('Intracellular Chloride Concentration(mM)', fontsize = '14')
plt.title('I')
plt.legend(loc = 'upper left', fontsize = '12')


# x, y = plot_func.smooth_func(X,Y32,3,1,kind='linear')
plt.subplot(2,5,10)
plt.plot(X, Y37, 'k', linestyle='-',  marker='d', markevery = slice(30,10000,600),  label='NaCl=130')
#
# x, y = plot_func.smooth_func(X,Y33,3,1,kind='linear')
plt.subplot(2,5,10)
plt.plot(X, Y38, 'k', linestyle='-',  marker='o', markevery = slice(30,10000,600),  label='NaCl=100')
#
# x, y = plot_func.smooth_func(X,Y61,3,1,kind='linear')
plt.subplot(2,5,10)
plt.plot(X, Y39, 'k', linestyle='-',  marker='+', markevery = slice(30,10000,600), label='NaCl=70')

# x, y = plot_func.smooth_func(X,Y34,3,1,kind='linear')
plt.subplot(2,5,10)
plt.plot(X, Y40, 'k', linestyle='-',  marker='^', markevery = slice(30,10000,600), label='NaCl=40')



plt.grid()
plt.xlim(0, 10000)
plt.tick_params(axis='x', which='major', labelsize=13)
plt.tick_params(axis='y', which='major',  labelsize=13)
plt.ticklabel_format(axis='y', style='sci',  scilimits=(-6,-6))
# plt.yaxis.major.formatter._useMathText = True
plt.ylim(-3e-7, -30e-7)
# plt.yticks(np.arange(0,0.0000005,0.00000002))
plt.xlabel ('time(s)', fontsize = '14')
plt.ylabel ('Apical water flux (umol/sec)', fontsize = '14')
plt.title('J')
plt.legend(loc = 'upper left', fontsize = '12')

# x, y = plot_func.smooth_func(X,Y55,3,1,kind='linear')
# plt.subplot(248)
# plt.plot(x, y, 'k', linestyle ='-', marker='.', markevery = slice(10,3000,50),  label = 'G_l=5')
#
# # x, y = plot_func.smooth_func(X,Y43,3,1,kind='linear')
# # plt.subplot(248)
# # plt.plot(x, y, 'k', linestyle='-',  marker='+', markevery = slice(10,3000,50),  label = 'G_l=10')
#
# x, y = plot_func.smooth_func(X,Y44,3,1,kind='linear')
# plt.subplot(248)
# plt.plot(x, y, 'k', linestyle='-',  marker='d', markevery = slice(10,3000,50),  label = 'G_l=20')
# #
# x, y = plot_func.smooth_func(X,Y45,3,1,kind='linear')
# plt.subplot(248)
# plt.plot(x, y, 'k', linestyle='-',  marker='o', markevery = slice(10,3000,50),  label = 'G_l=50')
# #
# x, y = plot_func.smooth_func(X,Y46,3,1,kind='linear')
# plt.subplot(248)
# plt.plot(x, y, 'k', linestyle='-',  marker='^', markevery = slice(10,3000,50), label = 'G_l=100')
#
# x, y = plot_func.smooth_func(X,Y47,3,1,kind='linear')
# plt.subplot(248)
# plt.plot(x, y, 'k',linestyle='-', marker='x', markevery = slice(10,3000,50),  label = 'G_l=200')
#
# plt.grid()
# plt.xlim(0, 5000)
# plt.ylim(300, 630)
# # plt.yticks(np.arange(0,0.00000044,0.00000002))
# plt.xlabel ('time(s)')
# plt.ylabel ('Cell Osmolarity(mM)')
# plt.title('H')
# plt.legend(loc = 'upper left')

plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)

plt.savefig('C:/Nima/ABI/2nd Paper/Figure05(17.03.2020).png')
plt.show()
#~ plt.legend(loc=0)
