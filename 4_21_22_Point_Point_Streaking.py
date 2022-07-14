##Luke Meyers 4/21/22 Attempt at realistic Streaking graphics 
#

#-----Import Code---------

from statistics import stdev
import matplotlib as mpl 
import matplotlib.pyplot as plt
import numpy as np
import random 

#----------Scatter graph streaking simulator

def genStreakData(n,spread,point1,point2):
    '''creates a linear dataset using point provided in format of [x,y]
    with n data points,can randomly scatter points out up to spread distance 
    perpendicular to fit line'''
    x = []
    y = []
    yFinal = []
    xFinal = [] 
    tckr = 0 
    lowX = point1[0]
    lowY = point1[1]
    upX = point2[0]
    upY = point2[1]
    slope = (upY-lowY)/(upX-lowX)
    b = lowY-(lowX*slope)
    xRange = upX-lowX
    xInc = xRange/n
    for i in range(n):
        x.append(lowX+i*xInc)
    for val in x:
        y.append(val*slope+b)
    for val in y:
        yAdd = random.uniform(-spread,spread)
        yFinal.append(val+yAdd)
        xFinal.append(x[tckr]-(slope*yAdd))
        tckr = tckr + 1
    return([xFinal,yFinal])
   
def genSizes(min,max,xData):
    '''randomly generates list of ints same length as xData
    between min and max to be used as sizes for scatter plots '''
    sizes = [] 
    for i in xData:
        sizes.append(random.uniform(min,max))
    return sizes 

def genColors(listIn,xData):
    '''randomly generates lsit of hex strings same len as 
    xData by randomly choosign among input list'''
    colors = []
    for i in xData:
        colors.append(random.choice(listIn))
    return colors


##-----------Input testing vars here---------------


xData = []
yData = []

s1 = genStreakData(12,0.1,[-3.2,-5.6],[1.309,9.235]) #setting with coordinates found on Desmos 
s2 = genStreakData(15,0.05,[-4.057,-8.339],[-1.534,9.199])
s3 = genStreakData(10,.2,[-7,-4],[-2,8])

xData = xData + s1[0] + s2[0] + s3[0]
yData = yData + s1[1] + s2[1] + s3[1]

print(xData)

s = genSizes(1,25,xData) #generate the sizes randomly 
c = genColors(['#FBF9EC','#FDF6E7','#FDF5E4'],xData)


##-----------------generate Figure----------------- 

fig, ax = plt.subplots() #generate mpl figure 
fig.set_facecolor('black')

scatter = ax.scatter(xData,yData,s=s,c=c)#gerenerate scatter graph
ax.axis('off') #hide axes 
ax.set_aspect(1)

##-----Defining bounds of graph
ax.set_xlim(-12,12)
ax.set_ylim(-12,12)


##--------Add circle for plate--------------

circle = plt.Circle((0,0),10,facecolor='#ECE0A1',alpha=.35,edgecolor='white',linewidth = 3,) 
ax.add_artist(circle)
scatter.set_clip_path(circle) 



#------Show graph------------

plt.show(block=False)
plt.pause(45)
plt.close()


