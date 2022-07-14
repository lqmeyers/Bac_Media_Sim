##Luke Meyers 4/25/22 
#Trying to  make a zig zag generator 

import math
import matplotlib as mpl
import matplotlib.pyplot as plt 
import numpy as np 
import random 

##----------first generate graph-------------------

fig, ax = plt.subplots()
fig.set_facecolor('black')

ax.axis('off') #hide axes 
ax.set_aspect(1) 

##-----Defining bounds of graph
ax.set_xlim(-12,12)
ax.set_ylim(-12,12)


##--------Add circle for plate--------------

circle = plt.Circle((0,0),10,facecolor='#ECE0A1',alpha=.35,edgecolor='white',linewidth = 3,) 
ax.add_artist(circle)

#-----pick a point on circle 

def getRandX(lower,upper):
    '''returns a random float betweeen bounds'''
    xOut = random.uniform(lower,upper)
    return xOut 

    xLow = center[0]-radius
    xHigh = center[0]+radius 
    ylow = center[1]-radius
    yHigh = center[1]+radius 

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

#print(getRandCircPoint())

##-----------------some trig functions------------------

def pythagMe(coord1,coord2):
    '''performs pythagorean theorum to return the 
    distance between two points. Input coords as [x,y]'''
    x1 = coord1[0]
    y1 = coord1[1]
    x2 = coord2[0]
    y2 = coord2[1]
    return math.sqrt((y2-y1)**2+(x2-x1)**2)

def lawCosinesOppSide(s1,opAng,s2):
    '''uses law of cosines to return len of opp side when 
    given two sides and an angle bwteen them'''
    return math.sqrt(s1**2+s2**2-(2*s1*s2*math.cos(opAng)))

def lawCosinesOppAngle(oppSide,s1,s2):
    '''returns the angle across from oppSide using law of Cosines
    when you know all three sides'''
    calcI =(oppSide**2)-(s1**2+s2**2)
    denom = 2*s1*s2
    calcII = calcI/denom
    oppAngle = np.pi - math.acos(calcII)
    return oppAngle

def lawSinesOppAngle(s1,oppAng,s2):
    '''returns the angle across from S2 using law of sines 
    when given a side and its oppAngle'''
    return math.asin((math.sin(oppAng)*s2)/s1)


##--------------Ok functions for getting rect nested in circle-------------------

def getSecantPoint(sLen,xIn,yIn,r):
    '''returns a point on the other side of a secant
    of length sLen, from point xIn, and yIn on a circle
    of radius r'''
    coordAngle = math.atan(yIn/xIn) #know this is calcing right 
    #print(math.degrees(coordAngle)) 
    secAngle = lawCosinesOppAngle(sLen,r,r)
    #print(math.degrees(secAngle))
    if xIn > 0:
         coord2Angle = coordAngle - secAngle #best for quad 1 
    else:
        coord2Angle = np.pi - abs(coordAngle) - secAngle # best for quad 2
    #print(math.degrees(coord2Angle)) #to define what gets subtracted to find the right angle 
    y2 = np.sin(coord2Angle)*r
    x2 = np.cos(coord2Angle)*r
    return [x2,y2]

#SOHCAHTOA

def getRectCoord3(coord1,coord2,s1,s2):
    '''returns the 3rd coord of a rectangle clockwise from top 
    left when given top left (coord1) and top right (coord2)
    coordinates and the ratio of sides with s1 being between the 
    given coordinates. Need to input the coords as [x,y]'''
    x1 = coord1[0]
    y1 = coord1[1]   
    x2 = coord2[0]
    y2 = coord2[1]
    s1Len = pythagMe(coord1,coord2)
    s2len = (s1Len/s1)
    rLen = pythagMe(coord2,[0,0])
    secAngle = lawCosinesOppAngle(s1Len,rLen,rLen)
    oppSecAngle = ((np.pi)-secAngle)/2
    #coord2Ang = math.atan(x2/y2) #gets coord 3 bottom right
    coord2AdjAng = math.atan(y2/x2) #gets coord 3 bottom right 
    hOppAng = (np.pi/2)-oppSecAngle
    h = lawCosinesOppSide(rLen,hOppAng,s2len)
    hAdjAng = lawSinesOppAngle(h,hOppAng,s2len)
    coord3AdjAng = coord2AdjAng - hAdjAng
    y3 = math.sin(coord3AdjAng)*h
    x3 = math.cos(coord3AdjAng)*h
    return [x3,y3]

def getRectCoord4(coord1,coord2,s1,s2): ##DISGUSTING 
    '''returns the fourth coordinate of a rectangle from 
    top left, using two coords and the side ratio between 
    them'''
    x1 = coord1[0]
    y1 = coord1[1]
    s1Len = pythagMe(coord1,coord2)
    s2len = (s1Len/s1)
    rLen = pythagMe(coord1,[0,0])
    secAngle = lawCosinesOppAngle(s1Len,rLen,rLen)
    coord1AdjAng = abs(math.atan(y1/x1)) #WORKS 
    #coord1AdjAng = math.atan(y1/x1)
    #print(math.degrees(math.atan(y1/x1)))
    oppSecAngle = ((np.pi)-secAngle)/2
    hOppAng = (np.pi/2)-oppSecAngle
    h = lawCosinesOppSide(rLen,hOppAng,s2len)
    #print(h)
    hAdjAng = lawSinesOppAngle(h,hOppAng,s2len)
    #print(math.degrees(hAdjAng))
    if x1 < 0:
        coord4AdjAng = coord1AdjAng - hAdjAng
    else:
        coord4AdjAng = np.pi - coord1AdjAng - hAdjAng
    #print(math.degrees(coord4AdjAng))
    y4 = math.sin(coord4AdjAng)*h
    x4 = -math.cos(coord4AdjAng)*h #k so this works for quad 2    
    #x4 = math.cos(coord4AdjAng)
    return [x4,y4]
    
def plotRectInCirc(coord1,radius,secLen,s1,s2):
    '''returns coordinates for a rectangle from coord1 and length of secant side with 
    s1:s2 side ratio, from top left clockwise as [[coord1x,coord1y],...'''
    coord2 = getSecantPoint(secLen,coord1[0],coord1[1],radius)
    return [coord1,coord2,getRectCoord3(coord1,coord2,s1,s2),getRectCoord4(coord1,coord2,s1,s2)]


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

def unScattify(xList,yList):
    '''takes two list like what are inputed to a scatter plot: 
    [x,x,x...],[y,y,y...] and returns them as a list of coordinates:
    [[x,y],[x,y],...]'''
    listOut = [] 
    for i in range(len(xList)):
        listOut.append([xList[i],yList[i]])
    return listOut 

##---------Functions for getting ZigZag in Rect-----
#----will imitate streaking 

def getLineFormula(coord1,coord2):
    '''intakes two coordinates and returns
    slope and y intercept to be used in 
    y = mx + b of line between points 
    '''
    x1 = coord1[0]
    y1 = coord1[1]
    x2 = coord2[0]
    y2 = coord2[1]
    m = (y2-y1)/(x2-x1)
    b = y1-m*x1
    return [m,b]

def getRandPointsAlongLine(coord1,coord2,num):
    '''returns num # of points along line y = 
    mx + b evenly spaced '''
    x1 = coord1[0]
    y1 = coord1[1]
    x2 = coord2[0]
    y2 = coord2[1]
    m = getLineFormula(coord1,coord2)[0]
    b = getLineFormula(coord1,coord2)[1]
    xRange = x2-x1
    xInc = xRange/num 
    #print(xInc)
    xOut = []
    yOut = []
    xStep = x1
    for inc in range(num):
        #xVal = random.uniform(xStep,(xStep+xInc)) #this generates weirdness 
        randIncNum = 4 #number of decimals options you want
        randInc = 1/randIncNum
        possibleIncNum = xInc/randInc
        xAdd = randInc + (random.uniform(0,possibleIncNum)*randInc) ##fix this
        xVal = xStep + xAdd
        #xVal = xStep+xInc/2
        xOut.append(xVal)
        xStep = xStep + xInc
    for x in xOut:
        yOut.append(m*x+b)
    return [xOut,yOut]

def alternatingOrderLists(list1,list2):
    '''takes 2 lists in and returns a combined list of
    alternating elements from each, starting with list1
    '''
    listOut = []
    #tckr = 0 
    list1Len = len(list1)
    list2Len = len(list2)
    if list1Len >= list2Len:
        for i in range(list1Len):
            listOut.append(list1[i])
            if list2Len > i:
                listOut.append(list2[i])
            #tckr = tckr + 1
    elif list2Len > list1Len:
        for i in range(list2Len):
            if list1Len > i:
                listOut.append(list1[i])
            listOut.append(list2[i])
            #tckr = tckr + 1 
    return listOut

##sometimes, but something with the end lines rand points they dont stay within the bounds
def getRandZigZagBounds(rect,numZZ,zigSide=1):
    '''returns the coords in order to graph a zigzag given a rectangle, 
    number of zig Zags, defined as back and forth, and side which zig will begin from.
    rect must be inputed as [x1,y1],[x2,y2].. with coord 1 as top 
    left and continuing clockwise. sides also follow clockwise, with coord1 -> 4 = side 1, the default '''
    #parsing ints 
    coord1 = rect[0]
    coord2 = rect[1]
    coord3 = rect[2]
    coord4 = rect[3]
    zigSideNum = numZZ + 1
    zagSideNum = numZZ 
    if zigSide == 1:
        zigLists = getRandPointsAlongLine(coord1,coord4,zigSideNum)
        zagLists = getRandPointsAlongLine(coord2,coord3,zagSideNum)
    elif zigSide == 2:
        zigLists = getRandPointsAlongLine(coord1,coord2,zigSideNum)
        zagLists = getRandPointsAlongLine(coord3,coord4,zagSideNum)
    elif zigSide == 3:
        zigLists = getRandPointsAlongLine(coord2,coord3,zigSideNum)
        zagLists = getRandPointsAlongLine(coord1,coord4,zagSideNum)
    elif zigSide == 4:
        zigLists = getRandPointsAlongLine(coord2,coord3,zigSideNum)
        zagLists = getRandPointsAlongLine(coord1,coord4,zagSideNum)
    zigPoints = unScattify(zigLists[0],zigLists[1])
    zagPoints = unScattify(zagLists[0],zagLists[1])
    pointsOut = alternatingOrderLists(zigPoints,zagPoints)
    return pointsOut 
    



##----------------Points along circle for testing------------
#pointIn = [-3.686,9.295] #ok got it working with (-,+) quadrant 
#pointIn = [3.800,9.249]#set point for quad 1 

pointIn = getRandCircPoint() #Seed point for entire streak generator 
print(pointIn)


#---------for testing points along line generator--------NEEDS WORK!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#randPoints = getRandPointsAlongLine([0,0],[10,10],10) #for testing zigzag gen 
#print(randPoints)
#print(getRandPointsAlongLine([0,0],[10,10],10))
#ax.scatter(randPoints[0],randPoints[1]) ##need to set to var cause callign multiple times gets differnr rand outs 
#ax.plot([0,10],[0,10])


##---------------Controlling Rectangle Parameters------------------

testRect = plotRectInCirc(pointIn,10,12,3,1)
testRectScatter = (getScatterReady(testRect))
#print(testRect)

#----------------Controlling ZigZag Parameters--------------------------

zzPoints = getRandZigZagBounds(testRect,3)
zzPointsScatter = getScatterReady(zzPoints)
#print(zzPoints)
#print(zzPointsScatter)


##-----------------Actually add them to graph----------------------

ax.scatter(testRectScatter[0],testRectScatter[1],c = ['red','blue','y','g'])   
ax.plot(zzPointsScatter[0],zzPointsScatter[1])



#------Show graph------------

plt.show(block=False)
plt.savefig('plate_sim.svg',format='svg')
plt.pause(10)
plt.close()

''' #this just seems like something helpful to have 
    x1 = coord1[0]
    y1 = coord1[1]
    x2 = coord2[0]
    y2 = coord2[1]
    x3 = coord3[0]
    y3 = coord3[1]
    x4 = coord4[0]
    y4 = coord4[1]
    
    s1 = getLineFormula(coord1,coord4)
    s1Len = pythagMe(coord1,coord4)
    s2 = getLineFormula(coord1,coord2)
    s2Len = pythagMe(coord1,coord2)
    s3 = getLineFormula(coord2,coord3)
    s3Len = pythagMe(coord2,coord3)
    s4 = getLineFormula(coord3,coord4)
    s4Len = pythagMe(coord3,coord4)
    
    '''