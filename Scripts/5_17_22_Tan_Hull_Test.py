## Luke Meyers
# testing connecting polygons with tangeant points

import matplotlib as mpl 
from matplotlib import pyplot as plt 
from matplotlib import patches as ptch
import math
import numpy as np 


import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np 
import random 
import math
import sys

sys.path.insert(0,"C:\\Users\\lqmey\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\scipy") 
from scipy.spatial._qhull import ConvexHull


#random.seed(.74502)

#---------Functions--------------
def getRandX(lower,upper):
    '''returns a random float betweeen bounds'''
    xOut = random.uniform(lower,upper)
    return xOut 

def getCirclePoint(xIn,radius = 10,center=[0,0]):
    '''returns a random positive point on a defined circle'''
    y1 = math.sqrt((radius**2)-xIn**2)
    point = [xIn,y1]
    return point


def getRandPointInCircleArea(radius = 10, center = [0,0]):
    '''returns a random point within the circle specified'''
    x = getRandX(-radius,radius)
    y = random.uniform(0,(getCirclePoint(x,radius,center)[1]))
    yMult = random.choice([1,-1])
    return([x,y*yMult])


def genRandData(center,radius,num):
    '''generates a dataset of random points within a circle'''
    x = []
    y = [] 
    for i in range(num):
       point = getRandPointInCircleArea(radius,center)
       x.append(point[0])
       y.append(point[1])
    return [x,y]


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

def pythagMe(coord1,coord2):
    '''performs pythagorean theorum to return the 
    distance between two points. Input coords as [x,y]'''
    x1 = coord1[0]
    y1 = coord1[1]
    x2 = coord2[0]
    y2 = coord2[1]
    return math.sqrt((y2-y1)**2+(x2-x1)**2)


#-----generating the random points 

data = genRandData([0,0],10,3)

workingData = unScattify(data[0],data[1])

#----- ok lets try this 

def avgTwoPoints(point1,point2):
    '''returns the avg point of two points as [x,y]'''
    avgX = (point1[0]+point2[0])/2
    avgY = (point1[1]+point2[1])/2
    return [avgX,avgY]

#print(avgTwoPoints([0,0],[3,5]))

def shortestDist(pointsIn,type='coord'):
    '''returns the points that are closest to each other from a dataset'''
    dist = 10
    shortest1I = 0
    shortest2I = 0
    tckr1 = 0 
    for point1 in pointsIn:
        tckr2 = 0
        for point2 in pointsIn:
            check = pythagMe(point1,point2)
            if point1 != point2:
                if check < dist:
                    shortest2I = tckr2
                    shortest1I = tckr1
                    dist = check 
                    #print(tckr1,tckr2)
            tckr2 = tckr2+1
        tckr1 = tckr1+1
    if type == 'coord':
        return [pointsIn[shortest1I],pointsIn[shortest2I],dist] #returns coords 
    elif type == 'index':
        return [shortest1I,shortest2I,dist] #returns just index 


def lastTry(pointsIn,clustersIn):
    '''takes a point list and a correlated cluster set and 
    returns it after one iteration, two closest points are avg'd in point 
    list and cluster is added in clusterlist.'''
    nextPoints = []
    nextClusters = [] 
    results = shortestDist(pointsIn,'index')
    point1 = pointsIn[results[0]]
    point2 = pointsIn[results[1]]
    dist = results[2]
    tckr = 0 
    for point in pointsIn:
        if point == point1:
            newPoint = avgTwoPoints(point1,point2)
            nextClusters.append([clustersIn[tckr],clustersIn[results[1]]])
            nextPoints.append(newPoint)
        elif point != point2:
            nextPoints.append(point)
            nextClusters.append(clustersIn[tckr])
        tckr = tckr + 1
    return [nextPoints,nextClusters,dist]
    #return nextClusters

def makeOTUs(pointsIn):
    '''Runs last try to make sets of point lists and different clusters
    for differnt grouping of points'''
    results = [[len(pointsIn),0,]]#pointsIn,pointsIn]]
    pIn = pointsIn
    cIn = pointsIn
    for i in range(len(pointsIn)):
        trial = lastTry(pIn,cIn)
        results.append([len(trial[1]),trial[2],trial[1],trial[0]])
        pIn = trial[0]
        cIn = trial[1]
    return results

def chooseOTU(resultsIn,cutOffDist): ## lets eventually make this auto based on graph 
    '''picks a level of clustering based on a cutoff distance'''
    #---first makes a list to scan
    finalResults = [len(resultsIn),0] 
    for i in resultsIn:
        if i[1] > finalResults[1] and i[1]< cutOffDist:
            finalResults = i 
    return finalResults[0:3]

def parseList2Step(listIn): ### clean up this function
    '''takes a list of any organization in and returns a list 
    without subdivison: [[][[][]]] to [[][][]]'''
    cleanList = [] 
    listCheck = listIn 
    #nextList = [] #may need to alternate?
    light = 'red'
    nextList = []
    while light == 'red':
        tckr = 0
        for i in listCheck:
            if type(i[0]) != list:
                #print(type(i[0]))
                cleanList.append(i)
                tckr = tckr + 1
            else:
                nextList = i 
                tckr = 0
                for i in nextList:
                    if i[0] == float or int:
                        cleanList.append(i)
                        tckr = tckr + 1
                    else:
                        listCheck = i 
                if tckr == len(nextList):
                    light = 'green'
                    #tckr = tckr + 1
        if tckr == len(listCheck):
            light = 'green'
    return cleanList
      
def checkList(listIn):
    '''inspects a list to make sure it is just sets of coordinates 
    with no nesting'''
    verdict = True
    if type(listIn) == list:
        for i in listIn:
            if type(i) == list:
                if type(i[0]) == list:
                    verdict = False
    return verdict

def fullParse(listIn):
    workingList = listIn
    verdict = checkList(listIn)
    while verdict == False:
        workingList = parseList2Step(workingList)
        verdict = checkList(workingList)
    return workingList 

def makeOTUHullGroups(listIn,cutoff=4.6):
    '''takes in a list of coordinates, and makes them into hull groups based on 
    proximity and with the cuttoff value. returns as lists of coords'''
    OTUresults = makeOTUs(listIn)
    OTUpick = chooseOTU(OTUresults,cutoff)
    print(OTUpick[0:2])
    '''parses nested list to make lists of coordinates to be fed into 
    hull chooser '''
    listIn = OTUpick[2]
    listOut = [] 
    for i in listIn:
        listOut.append(fullParse(i))
    return listOut




def getTanPoints(center1,center2,r):
    '''gets the end points of a tangeant line that connects
    two circles with radius r centered at the points enetered as 
    [x,y],[x,y]'''
    x1 = center1[0]
    y1 = center1[1]
    x2 = center2[0]
    y2 = center2[1]
    if x1>=x2:
        xDif = x1-x2
    else:
        xDif = x2-x1
    if y1>=y2:
        yDif = y1-y2
    else:
        yDif = y2-y1
    difAng = math.atan(yDif/xDif)
    addAng = np.pi - difAng - (np.pi/2)
    xAdd = math.cos(addAng)*r
    yAdd = math.sin(addAng)*r
    return [[x1+xAdd,y1+yAdd],[x2+xAdd,y2+yAdd]]

def getTanPolyPoints(centerList,r):
    points = []  
    for i in range((len(centerList)-1)):
        results = getTanPoints(centerList[i],centerList[i+1],r)
        points.append(results[0])
        points.append(results[1])
    return points 

print(workingData)
polyPoints = getTanPolyPoints(workingData,.495)



#print(makeOTUHullGroups(workingData))

#OTUoptData = getScatterReady(OTUresults) #need to get just dist and num to plot 
#print(OTUoptData)
 
def convexHull(p):
    p = np.array(p)
    hull = ConvexHull(p)
    return p[hull.vertices,:]

def addHulls(plotName,coordList,cutoff=4.6):
    '''adds hulls to a graph based on OTU's of proximity, when given coordsList'''
    OTUs = makeOTUHullGroups(workingData,cutoff)
    for i in OTUs:
        #print(i)
        if len(i)>=3:
            points = convexHull(i)
            print(points)
            poly = plt.Polygon(points)
            plotName.add_patch(poly)



#-------plotting it 
fig = plt.figure(figsize=(8,4))
ax = fig.add_subplot()
#ax.plot([0,1],[1,2])
#ax.axis('off') #hide axes 
ax.set_aspect(1)
#-Defining bounds of graph()
ax.set_xlim(-12,12)
ax.set_ylim(-12,12)  
ax.grid() 



ax.scatter(data[0],data[1],s=[3000,3000,3000])
#ax.scatter([7.8588,6.576],[.15649,-.64272]) #shortest dist works 
#ax.plot(OTUoptData[0],OTUoptData[1])

ax.plot(getScatterReady(polyPoints)[0],getScatterReady(polyPoints)[1],c='r')



circle1 = plt.Circle((0,0),10,fill=False,edgecolor='b')
ax.add_artist(circle1)

#addHulls(ax,workingData,5)


plt.show()
plt.pause(25)
plt.close()

