##Luke Meyers 5/13/22 
#Attempting to make program for connecting circles with a polygon 

import matplotlib as mpl 
from matplotlib import pyplot as plt 
from matplotlib import patches as ptch
import math
import numpy as np 


fig = plt.figure(figsize=(8,4))
ax = fig.add_subplot()
ax.set_xlim(-1,5)
ax.set_ylim(-1,3)
ax.set_aspect (1)

testCoords = [[2,0],[0,2]]

ax.scatter(testCoords[0],testCoords[1])

#circle = plt.Circle((1,2),.495,alpha=.3) #circle coords need ()
ax.scatter(testCoords[0],testCoords[1],s=[3000,3000],alpha=.5,linewidths=0)
#ax.add_artist(circle)

def getTanPoints(center1,center2,r):
    '''gets the end points of a tangeant line that connects
    two circles with radius r centered at the points enetered as 
    [x,y],[x,y]'''
    x1 = center1[0]
    y1 = center1[1]
    x2 = center2[0]
    y2 = center2[1]
    xDif = abs(x1-x2)
    yDif = abs(y1-y2)
    difAng = math.atan(yDif/xDif)
    addAng = np.pi - difAng - (np.pi/2)
    xAdd = math.cos(addAng)*r
    yAdd = math.sin(addAng)*r
    if x1< x2 and y1 >= y2:
        return [[x1+xAdd,y1+yAdd],[x2+xAdd,y2+yAdd]]
    elif x1 >= x2 and y1 >= y2:
         return [[x1+xAdd,y1-yAdd],[x2+xAdd,y2-yAdd]]
    elif x1 >= x2 and y1 < y2:
        return [[x1-xAdd,y1-yAdd],[x2-xAdd,y2-yAdd]]
    elif x1 < x2 and y1 < y2:
        return [[x1-xAdd,y1+yAdd],[x2-xAdd,y2+yAdd]]
def getScatterReady(coordsList):
   '''input a list of coordinates as [[x,y],[x,y]...
   and recieve list of [[x,x,...],[y,y,...]]'''
   xData = []
   yData = []
   for coord in coordsList:
       xData.append(coord[0])
       yData.append(coord[1])
   return [xData,yData]

def unScattify(xList,yList):
    '''takes two list like what are inputed to a scatter plot: 
    [x,x,x...],[y,y,y...] and returns them as a list of coordinates:
    [[x,y],[x,y],...]'''
    listOut = [] 
    for i in range(len(xList)):
        listOut.append([xList[i],yList[i]])
    return listOut 

def getScatterReady(coordsList):
   '''input a list of coordinates as [[x,y],[x,y]...
   and recieve list of [[x,x,...],[y,y,...]]'''
   xData = []
   yData = []
   for coord in coordsList:
       xData.append(coord[0])
       yData.append(coord[1])
   return [xData,yData]

centers = unScattify(testCoords[0],testCoords[1])

points = getTanPoints(centers[0],centers[1],.495)

ax.plot(getScatterReady(points)[0],getScatterReady(points)[1])

plt.savefig('C:\\Users\\lqmey\\OneDrive\\Desktop\\Python Code\\Projects Lab\\tan_Circle.svg',format='svg')
plt.show()

