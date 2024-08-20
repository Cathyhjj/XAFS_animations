# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 11:37:36 2021

@author: Juanjuan Huang
"""
import glob 
import os
import numpy as np
import matplotlib.pyplot as plt
os.chdir("D://Google Drive//TUM_PhD//10_PhD_thesis//codes//Pd_foil_standard_example_XANES_EXAFS")

def change_font_size(size):
    from matplotlib import pylab
    params = {'legend.fontsize': size,
             'axes.labelsize': size,
             'axes.titlesize':size,
             'xtick.labelsize':size,
             'ytick.labelsize':size,
             'font.family':'calibri',
             }
    pylab.rcParams.update(params)
    
#%%
#%

Pd_standard = np.loadtxt('Pd_K_standard.dat.nor')
Pd_R = np.loadtxt('marked.chir_mag')
Pd_K = np.loadtxt('marked.chik2')

fit = np.loadtxt('Pd_K_standard.dat.rmag')
fit_k = np.loadtxt('Pd_K_standard.dat.k2')


#%%

para = {'linewidth': 2.5, 'alpha': 0.7,}
plt.figure(figsize = (12,4))
change_font_size(20)
plt.plot(Pd_standard[:,0], Pd_standard[:,1], color = 'navy', **para)
plt.plot(Pd_standard[:,0], Pd_standard[:,2], color = 'crimson', **para)

plt.ylim(-0.1, 1.2)
plt.xlim(24100,25750)


#plt.xlabel('X-ray Energy [eV]')
#plt.savefig('Pd_spectrum_spring8.jpg', dpi = 300)
plt.legend(['$\mu(E)$','$\mu_0(E)$'])

plt.savefig('Pd_spectrum_spring8_fit.jpg', dpi = 300)


#%%
change_font_size(20)

plt.figure(figsize = (5,4))

plt.plot(Pd_K[:,0], Pd_K[:,2], color = 'navy', **para)

#plt.ylim(-0.1, 1.2)
plt.xlim(0,15)

#plt.xlabel('X-ray Energy [eV]')
plt.savefig('Pd_K.jpg', dpi = 300)

#%%
plt.figure(figsize = (5,4))
plt.plot(Pd_R[:,0], Pd_R[:,1], color = 'navy', **para)


#plt.ylim(-0.1, 1.2)
plt.xlim(0,6)

#plt.xlabel('X-ray Energy [eV]')
plt.savefig('Pd_R.jpg', dpi = 300)

#%%

plt.figure(figsize = (5,4))
plt.plot(fit[:,0], fit[:,1]/10., color = 'navy', **para)

plt.plot(fit[:,0], fit[:,2]/10., color = 'crimson', **para)

#plt.ylim(-0.1, 1.2)
plt.xlim(0,6)
plt.legend(['Measured data', 'fitting (first shell)'])
#plt.xlabel('X-ray Energy [eV]')
plt.savefig('fit_R.jpg', dpi = 300)



#%%

plt.figure(figsize = (10,4))
plt.plot(fit_k[:,0], fit_k[:,1]/10., color = 'navy', **para)

plt.plot(fit_k[:,0], fit_k[:,2]/10., color = 'crimson', **para)

#plt.ylim(-0.1, 1.2)
plt.xlim(0,15)
plt.legend(['Measured data', 'fitting (first shell)'])
#plt.xlabel('X-ray Energy [eV]')
plt.savefig('fit_K.jpg', dpi = 300)







