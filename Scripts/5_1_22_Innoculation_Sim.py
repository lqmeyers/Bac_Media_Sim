##Luke Meyers 4/21/22 Attempt at realistic Streaking graphics 
#

#-----Import Code---------

import matplotlib as mpl 
import matplotlib.pyplot as plt
import random 
import math

#----------Scatter graph attribute functions------------------------

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


#-----pick a point on circle------------------------------------------- 

def getRandX(lower,upper):
    '''returns a random float betweeen bounds'''
    xOut = random.uniform(lower,upper)
    return xOut 

def getCirclePoint(xIn,radius = 10,center=[0,0]):
    '''returns a random positive point on a defined circle'''
    y1 = math.sqrt((radius**2)-xIn**2)
    point = [xIn,y1]
    return point


def getRandCircPoint(radius = 10,center = [0,0]):
    '''returns a random point on a circle'''
    xLow = center[0]-radius
    xHigh = center[0]+radius 
    return getCirclePoint(getRandX(xLow,xHigh))

def getRandPointInCircleArea(radius = 10, center = [0,0]):
    '''returns a random point within the circle specified'''
    x = getRandX(-radius,radius)
    y = random.uniform(0,(getCirclePoint(x,radius,center)[1]))
    yMult = random.choice([1,-1])
    return([x,y*yMult])

#print(getRandPointInCircleArea())


##---------Useful functions for transforming coordinates--------------------

def getScatterReady(coordsList):
   '''input a list of coordinates as [[x,y],[x,y]...
   and recieve list of [[x,x,...],[y,y,...]]'''
   xData = []
   yData = []
   for coord in coordsList:
       xData.append(coord[0])
       yData.append(coord[1])
   return [xData,yData]

##----------------Generating the Data--------------------------------------------

def genInocPlate(radius,center,colNum,colSizes=[0,25],colColors=['#FBF9EC','#FDF6E7','#FDF5E4']):
    '''returns data for a scatter within circle defined by radius, center, with colNum # of colonies and 
    sizes and colors randomly selected from colSizes and colNum'''
    data = []
    for i in range(colNum):
        data.append(getRandPointInCircleArea(radius,center))
    xData = getScatterReady(data)[0]
    yData = getScatterReady(data)[1]
    s = genSizes(colSizes[0],colSizes[1],xData)
    c = genColors(colColors,xData)
    return [xData,yData,s,c,]
        
#print(genInocPlate(10,[0,0],10))
        


##----------------Points along circle for testing------------

#pointIn = [-3.686,9.295] #ok got it working with (-,+) quadrant 
#pointIn = [3.800,9.249]#set point for quad 1 


coordIn = getRandCircPoint(9.5) #Seed point for entire streak generator #add circle radius here 



###------------------------------------------Input testing vars here---------------------------------------------------

inocData = genInocPlate(9,[0,0],30,[10,30])


###----------------Generating the Figure-------------------------------------------------------

fig, ax = plt.subplots() #generate mpl figure 
fig.set_facecolor('black')


scatter = ax.scatter(inocData[0],inocData[1],s=inocData[2],c = inocData[3])
ax.axis('off') #hide axes 
ax.set_aspect(1)

##-----Defining bounds of graph
ax.set_xlim(-12,12)
ax.set_ylim(-12,12)


##--------Add circle for plate--------------

circle = plt.Circle((0,0),10,facecolor='#ECE0A1',alpha=.35,edgecolor='white',linewidth = 3,) 
ax.add_artist(circle)
scatter.set_clip_path(circle) 
#scatter2.set_clip_path(circle) 



#------Show graph------------

plt.show(block=False)
plt.pause(45)
plt.close()

