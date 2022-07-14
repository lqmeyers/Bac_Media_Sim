##Luke Meyers, Bioinfo Projects Lab 4_10_22
#First test at animating colony growth on a plate 


from statistics import stdev
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

import random
import sys

#sys.path.insert(0,"C:\\Users\\lqmey\\OneDrive\\Desktop\\Python Code\\Bioinfo") 
#make bioinfo functions available for import 

#from CovidGenesExtraFun import highestPeak
#from AvgLentoCodonwPllot import avgList 

def avgList(listIn):
    '''returns the avg of a list of ints'''
    val = sum(listIn)
    avg = val/len(listIn)
    return avg


def genScatterData(num):
    '''generate random scatterplot data with n = num '''
    x = []
    y = []
    i = 0 
    while i < num:
        x.append(random.uniform(0.00,5.00))
        y.append(random.uniform(0.00,5.00))
        i = i+1
    return [x,y]
        

def getBound(listIn,bound='upper'):
    '''gets the most extreme value from a list depending 
    on which bound is specified'''
    if bound == 'upper':
        highest = 0
        for i in listIn:
            if i > highest:
                highest = i 
        return highest 
    else:
        lowest = 0
        for i in listIn:
            if i < lowest:
                lowest = i 
        return lowest


ax = plt.subplot()

xData = genScatterData(30)[0]
yData = genScatterData(30)[1]

centerX = avgList(xData)
centerY = avgList(yData)


plt.xlim(getBound(xData,'lower')-stdev(xData),getBound(xData,'upper')+stdev(xData))
plt.ylim(getBound(yData,'lower')-stdev(yData),getBound(yData,'upper')+stdev(yData))

ax.set_aspect(1) #sets aspect of graph view need to get square/circle not elipse 

circle = plt.Circle((centerX,centerY),(getBound(xData,'upper')-centerX),facecolor='#ECE0A1',alpha=.3,edgecolor='black',linewidth = 1) 
#pretty sure 2nd arg is radius 
#need to select for biggest radius 

ax.add_artist(circle)
#plt.figure(figsize=(7,5)) #this creates a new figure window 
scatter = ax.scatter(xData,yData,color='#C7A37D') #need # to recognize Hex color 
ax.axis('off') #hides axis and labels 
scatter.set_clip_path(circle)


plt.show(block=False) #cant find much on what block does but necessarty tpo close 
plt.pause(40) #keeps viewer open 
plt.close() #closes viewer