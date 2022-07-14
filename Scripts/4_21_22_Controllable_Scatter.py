##4/21/22 Luke Meyers 
#Making a program to generate precise scatter plots 

#from matplotlib.lines import _LineStyle
import numpy as np 
from matplotlib import pyplot as plt 
import matplotlib as mpl 
import random 

def genLinearData(n,slope,b=0,lower=0):
    '''creates a linear dataset using slope and lower bound provided
    with n data points'''
    x = []
    y = [] 
    for i in range(n):
        x.append(lower+i)
    for val in x:
        y.append(val*slope+b) 
    return([x,y])

#print(genLinearData(20,6,5,10))

def genLinScatData(n,slope,spread,b=0,lower=0):
    '''creates a linear dataset using slope and lower bound provided
    with n data points'''
    x = []
    y = [] 
    yFinal = []
    xFinal = [] 
    tckr = 0 
    for i in range(n):
        x.append(lower+i)
        x.append(lower+i+.25)
        x.append(lower+i+.5)
        x.append(lower+i+.75)
    for val in x:
        y.append(val*slope+b)
    for val in y:
        yAdd = random.uniform(-spread,spread)
        yFinal.append(val+yAdd)
        xFinal.append(x[tckr]-(slope*yAdd))
        tckr = tckr + 1
    return([xFinal,yFinal])



#def genLinearScatter(slope,n,spread):
def genLinScatter(n,slope,spread,b=0,lower=0):
    '''creates a scatter plot with n number points, with slope, but the points
    are distributed randomly across the spread listed'''
    data = genLinScatData(n,slope,spread,b,lower)
    xData = data[0]
    yData = data[1]
    fig, ax = plt.subplots()
    ax.set_aspect(1)
    ax.scatter(xData,yData)
    if xData[len(xData)-1] > yData[len(yData)-1]:
        xUp = xData[len(xData)-1]+1
        yUp = xUp
    else: 
        xUp = yData[len(yData)-1]+1
        yUp = xUp
    #ax.set_xlim((xData[0]-1),xUp)
    #ax.set_ylim((yData[0]-1),yUp)
    #plt.grid(True,linestyle='-',linewidth=1)
    ax.axis('off')
    plt.show(block=False)
    plt.pause(45)
    plt.close()



#linData = genLinScatData(20,.54,1)
genLinScatter(20,.5,.7)
#print(len([1,2,3,4]))