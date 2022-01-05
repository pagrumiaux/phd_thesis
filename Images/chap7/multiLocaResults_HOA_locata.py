# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 10:11:46 2021

@author: RQML4978
"""

import numpy as np
import matplotlib.pyplot as plt
import sys

#%%
plt.rc('xtick', labelsize=14) 
plt.rc('ytick', labelsize=11) 
plt.rc('axes', labelsize=14)
plt.rc('figure', titlesize=20)
plt.rc('legend', fontsize=12)
plt.rcParams['figure.figsize'] = [15,7]

#%% load numpy arrays
path_np = "C:/Users/RQML4978/Documents/Python/c_loca_counting/data/results/narray/"
testSets = ['loc_task1', 'loc_task2', 'loc_task3', 'loc_task4']
suffices = ['VVM', '6b_MPf4_FOA','6b_MPf4_HOA']

errorDoa_l = [[], [], []]
for iSuffix, suffix in enumerate(suffices):
    for itestSet, testSet in enumerate(testSets):
        errorDoa_l[iSuffix].append(np.load(path_np + testSet + '/' + suffix + ".npy"))
    
#%% bloxplots/violins
        
colors = ['#311947','#5c2d87', '#8b47cc', '#4947cc', '#4787cc', '#47cacc', '#63bcc9', '#cdb3d4', '#e7b7c8', '#ffbe88']
labels = ['Task 1', 'Task 2', 'Task 3', 'Task 4']
legends= ['Baseline (VVM)',
          r'Baseline ($M_{6,4}$)',
          r'$M^{HO}_{6,4}$',]
width = 0.6

fig, ax = plt.subplots(1)

ax.boxplot(errorDoa_l[0], positions=[1,5,9,13], showfliers=False,showmeans=False,
            boxprops=dict(color=colors[0]),
            capprops=dict(color=colors[0]),
            whiskerprops=dict(color=colors[0]),
            flierprops=dict(color=colors[0], markeredgecolor=colors[0]),
            medianprops=dict(color=colors[0]),widths = width)
violin1 = ax.violinplot(errorDoa_l[0], positions=[1,5,9,13],widths = width, showextrema=False)
for vp in violin1['bodies']:
    vp.set_facecolor(colors[0])
    vp.set_edgecolor(colors[0])

ax.boxplot(errorDoa_l[1], positions=[2,6,10,14], showfliers=False,showmeans=False,
            boxprops=dict(color=colors[1]),
            capprops=dict(color=colors[1]),
            whiskerprops=dict(color=colors[1]),
            flierprops=dict(color=colors[1], markeredgecolor=colors[1]),
            medianprops=dict(color=colors[1]),widths = width)
violin2 = ax.violinplot(errorDoa_l[1], positions=[2,6,10,14], widths=width, showextrema=False)
for vp in violin2['bodies']:
    vp.set_facecolor(colors[1])
    vp.set_edgecolor(colors[1])
    
ax.boxplot(errorDoa_l[2], positions=[3,7,11,15], showfliers=False,showmeans=False,
            boxprops=dict(color=colors[2]),
            capprops=dict(color=colors[2]),
            whiskerprops=dict(color=colors[2]),
            flierprops=dict(color=colors[2], markeredgecolor=colors[2]),
            medianprops=dict(color=colors[2]),widths = width)
violin2 = ax.violinplot(errorDoa_l[2], positions=[3,7,11,15], widths=width, showextrema=False)
for vp in violin2['bodies']:
    vp.set_facecolor(colors[2])
    vp.set_edgecolor(colors[2])
    
    
ax.set_ylabel('Angular error (°)')
ax.grid(axis='y')
ax.set_ylim([-1,40])
ax.set_xlim([0.5,15.5])
plt.xticks([2,6,10,14],labels)

h0, = plt.plot([1,1],color=colors[0])
h1, = plt.plot([1,1],color=colors[1])
h2, = plt.plot([1,1],color=colors[2])
plt.legend((h0,h1,h2),tuple(legends), loc=2)
h0.set_visible(False)
h1.set_visible(False)
h2.set_visible(False)

#%% task 1
print('Task 1')

acc10_l = []
acc15_l = []
acc20_l = []
mean_l = []
median_l = []

for i in range(len(suffices)):
    acc10_l.append(np.sum(errorDoa_l[i][0]<=10)/errorDoa_l[1][0].size)
    acc15_l.append(np.sum(errorDoa_l[i][0]<=15)/errorDoa_l[1][0].size)
    acc20_l.append(np.sum(errorDoa_l[i][0]<=20)/errorDoa_l[1][0].size)
    mean_l.append(np.mean(errorDoa_l[i][0]))
    median_l.append(np.median(errorDoa_l[i][0]))

for i in range(len(acc10_l)):
    print(f'\n{suffices[i]}')
    print(f'acc <10°: {acc10_l[i]}')
    print(f'acc <15°: {acc15_l[i]}')
    print(f'acc <20°: {acc20_l[i]}')
    print(f'mean: {mean_l[i]}')
    print(f'median: {median_l[i]}')
    
#%% task 2
print('Task 2')

acc10_l = []
acc15_l = []
acc20_l = []
mean_l = []
median_l = []

for i in range(len(suffices)):
    acc10_l.append(np.sum(errorDoa_l[i][1]<=10)/errorDoa_l[1][1].size)
    acc15_l.append(np.sum(errorDoa_l[i][1]<=15)/errorDoa_l[1][1].size)
    acc20_l.append(np.sum(errorDoa_l[i][1]<=20)/errorDoa_l[1][1].size)
    mean_l.append(np.mean(errorDoa_l[i][1]))
    median_l.append(np.median(errorDoa_l[i][1]))

for i in range(len(acc10_l)):
    print(f'\n{suffices[i]}')
    print(f'acc <10°: {acc10_l[i]}')
    print(f'acc <15°: {acc15_l[i]}')
    print(f'acc <20°: {acc20_l[i]}')
    print(f'mean: {mean_l[i]}')
    print(f'median: {median_l[i]}')
        
#%% task 3
print('Task 3')

acc10_l = []
acc15_l = []
acc20_l = []
mean_l = []
median_l = []

for i in range(len(suffices)):
    acc10_l.append(np.sum(errorDoa_l[i][2]<=10)/errorDoa_l[1][2].size)
    acc15_l.append(np.sum(errorDoa_l[i][2]<=15)/errorDoa_l[1][2].size)
    acc20_l.append(np.sum(errorDoa_l[i][2]<=20)/errorDoa_l[1][2].size)
    mean_l.append(np.mean(errorDoa_l[i][2]))
    median_l.append(np.median(errorDoa_l[i][2]))

for i in range(len(acc10_l)):
    print(f'\n{suffices[i]}')
    print(f'acc <10°: {acc10_l[i]}')
    print(f'acc <15°: {acc15_l[i]}')
    print(f'acc <20°: {acc20_l[i]}')
    print(f'mean: {mean_l[i]}')
    print(f'median: {median_l[i]}')    
#%% task 4
print('Task 4')

acc10_l = []
acc15_l = []
acc20_l = []
mean_l = []
median_l = []

for i in range(len(suffices)):
    acc10_l.append(np.sum(errorDoa_l[i][3]<=10)/errorDoa_l[1][3].size)
    acc15_l.append(np.sum(errorDoa_l[i][3]<=15)/errorDoa_l[1][3].size)
    acc20_l.append(np.sum(errorDoa_l[i][3]<=20)/errorDoa_l[1][3].size)
    mean_l.append(np.mean(errorDoa_l[i][3]))
    median_l.append(np.median(errorDoa_l[i][3]))

for i in range(len(acc10_l)):
    print(f'\n{suffices[i]}')
    print(f'acc <10°: {acc10_l[i]}')
    print(f'acc <15°: {acc15_l[i]}')
    print(f'acc <20°: {acc20_l[i]}')
    print(f'mean: {mean_l[i]}')
    print(f'median: {median_l[i]}')    