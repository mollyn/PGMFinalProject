# must have this to ensure float division!
# PYTHON REQUIRES THAT __FUTURE__ IMPORTS BE AT THE BEGINNING OF A FILE
from __future__ import division
# put these here even though they are in props.py just so I can get tips from
# the IDE as I type
import matplotlib.pyplot as plt
import numpy as np

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Use our script to load properties, modules, and csv data
Run only once before beginning analysis to avoid wasting time by loading data
more than once!
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""
UNCOMMENT HERE TO LOAD THE DATA FOR THE FIRST RUN
COMMENT OUT AFTER THE FIRST RUN SO AS TO NOT WASTE TIME
"""
#exec(open("loadData.py"))

ca()

basePlotTitles = ['Jan 2017', 'Jun 2017', 'Dec 2017']


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Histograms to examine gender
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
I = pd.Index(['unkPct', 'malPct', 'femPct'])
C = pd.Index(['Jan17', 'Jun17', 'Dec17'])
data = np.ones([I.size, C.size])

# Make some preliminary plots
for mIdx,m in enumerate(months):
    fig = plt.figure(basePlotTitles[mIdx] + ' Gender')
    plt.bar(range(3), np.bincount(m.gender),width=0.8,align='center')
    plt.xticks(range(3), ['Unknown','Male','Female'])
    plt.xlim([-1,3])
    plt.title(basePlotTitles[mIdx] + ' Gender')
    plt.show()
    
    for whichGender in range(0,3):
        data[whichGender][mIdx] = m.loc[m.gender==whichGender].shape[0] / \
            m.gender.shape[0]  * 100
    
    
genderPcts = pd.DataFrame(data, index=I, columns=C)
# This is STRONGLY skewed towards male riders?......WHY?
# I wasn't expecting that drastic of a difference!


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Histograms to examine user type
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

I = pd.Index(['unkPct', 'subscriberPct', 'tempPct'])
C = pd.Index(['Jan17', 'Jun17', 'Dec17'])
data = np.ones([I.size, C.size])
numData = np.ones([I.size, C.size])

# Make some preliminary plots
for mIdx,m in enumerate(months):
    fig = plt.figure(basePlotTitles[mIdx] + ' User Type')
    plt.bar(range(3), np.bincount(m.usertype),width=0.8,align='center')
    plt.xticks(range(3), ['Unknown','Subscriber','Temporary'])
    plt.xlim([-1,3])
    plt.title(basePlotTitles[mIdx] + ' User Type')
    plt.show()
    
    for whichType in range(0,3):
        data[whichType][mIdx] = m.loc[m.usertype==whichType].shape[0] / \
            m.usertype.shape[0]  * 100
        numData[whichType][mIdx] = m.loc[m.usertype==whichType].shape[0]    
    
typePcts = pd.DataFrame(data, index=I, columns=C)
typeNums = pd.DataFrame(numData, index=I, columns=C)
# I expected subscriber number to remain approximately the same throughout
#the year, even though its percentage went down (due to the large number of temp
#subscribers).  However, the subscriber went up as well, just not AS much as 
#the temp number, hence a smaller subscriber percentage

    
"""
This will be where I do percentage calculations, maybe some ad hoc work,
perhaps some curve fitting, etc.  Any data analysis will go in here (or
possibly be expanded into other files if trends arise in how I am going 
about my analysis).
"""   
    
    
    
    
    
