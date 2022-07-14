##Luke Meyers 5/4/22
# Trying to create a function oriented program out of object oriented package lol 

import matplotlib as mpl 
import matplotlib.pyplot as plt
import matplotlib.patches as ptch

'''
fig = plt.figure()
ax = fig.add_subplot()


ax.plot([0,1,2,3],[0,1,2,3])
'''

def makeFig(figname='ax'):
    '''generates a subplot with figname and plots arbitary data on it'''
    fig = plt.figure()
    locals()[figname] = fig.add_subplot()
    locals()[figname].plot([0,1],[0,1])

'''
x = 'ax'
globals()[x] = fig.add_subplot()
globals()[x].plot([0,1],[0,1])
'''
'''Ok so basically,globals()[varname] allows you to retrieve the content of 
varname and then you can set it as a name of somthing
and you can reference it as much as you. Use globals for whole 
program and locals for functions.'''

makeFig('lol')

plt.show()
plt.pause(15)
plt.close()

