#Last Updated By Luke Meyers 5/23/22

#Luke Meyers and Eva Alleman 
#Creating Differential and Selective Media Sim
#4/20/22

'''Purpose:
    An educational tool to demonstrate the usefulness of selective and 
    differental media in bacteria culturing. Help to distinguish between 
    the two types, as well as various bacteria traits that the media 
    act upon. Potentially show how media may be used in an investigative
    process '''

'''Input:
    User inputs media choice and bacteria strain'''

'''Process:
    takes user input, gets stats for grap appearance using a library, 
    feeds to graphing software and generates an image of what a plate
    may look like. Further on, may create blendr images of each combo to 
    be presented for each combo.'''

'''Output:
    Outputs an image of what the growth on the plate looks like, 
    accompanied with a control plate, potentially a count of colonies'''

##---------------Import relevant files----------------
from statistics import stdev
from typing import List #think this might be a bug 
import matplotlib.pyplot as plt
import matplotlib.patches as patch
import math
import numpy as np 


import random
import sys

sys.path.insert(0,"C:\\Users\\lqmey\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages\\scipy") 
from scipy.spatial import ConvexHull

#random.seed(.7685645) #in case you need to fix seed to test 


###------------------ADD INPUTS BELOW-----------------------------

##------------Input Plate Media Selection--------------
#plateIn = 'mac'
plateIn = 'msa'
#plateIn = 'blo'
#plateIn = 'nutrient'
#plateIn = 'hek'


##--------------Input Bacteria Selection-----------------

#bacIn = 'staphEp'
bacIn = 'staphAur'
#bacIn = 'eColi'
#bacIn = 'pseudomonas'
#bacIn = 'salmonella'
#bacIn = 'shigella'
#bacIn = #ADD NEW OPTIONS W/ DATA 

###------------------------ Set of dictionaries for adding Plate outcomes----------

##MacConkey agar is a selective and differential media that is used to idenity gram-negative bacteria and lactose-fermenting or non-lactose fermenting
mac = {'staphEp':[0,'#E36C7A'],
            'staphAur':[0,'#E36C7A'], 
            'eColi': [1,'#E36C7A','#E4A7B9',[50,50]],
            'pseudomonas':[1,'#E36C7A','#F4F2E6',[50,50]],
            'salmonella':[1,'#EBB503', '#FDD999',[50,50]],
            'shigella': [1,'#EBB503','#E9E0E0',[50,50]]}
#could use random choice function to distniguish between pseudomonas and salmonella

#gets a 1 if it will grow
#make sure to have '# for hex colors 

##Mannitol Salt Agar is differential media that is used to idenify staph auerus (yellow colonies) from other forms of staph (pink/light red colonies)
msa = {'staphEp':[1,'#E90E0E','#E36C7A',[45,50]],
           'staphAur':[1, '#FBC515', '#F0D783',[45,50]],
           'eColi': [0,'#E90E0E'],
           'pseudomonas':[0,'#E90E0E'],
           'salmonella':[0,'#E90E0E'],
           'shigella':[0,'#E90E0E']}

#Nutrient Agar is a non-selective media that can grow all of the strains of bacteria we have selected for the simulation
nutrient = {'staphEp':[1,'#F2DF61','#F1E59D',[35,40]],
                'staphAur':[1,'#F2DF61', '#F3D41B',[35,40]],
                'eColi': [1,'#F2DF61', '#F3F377',[25,30]],
                'pseudomonas':[1,'#F2DF61','#EDF7E3',[55,60]],
                'salmonella':[1,'#F2DF61','#FAE9AB',[45,50]],
                'shigella':[1,'#F2DF61','#DABD66',[45,50]]}
#could use random choice function here to pic the colony colors to get variation on white color

#Hektoen eneteric agar is a selective and differential media used to identify and isolate salmonella, looks for lactose fermenting bacteria, hydorgen sulfide
#production as well as inhibit the growth of gram-positive bacteria 
hek = {'staphEp':[0,'#FF4E00'],
       'staphAur':[0,'#FF4E00'],
       'eColi':[1, '#FF4E00', '#FFDB00',[50,50]],
        #plate is blue but ecoli turn plate red/orange color due to bile production
       'pseudomonas':[1,'#14707F', '#EDF7E3',[50,50]],
       #check with Dr. R on pseudomonas for this media
       'salmonella':[1,'#14707F','#000000',[50,50]],
       'shigella':[1,'#14707F','#97CF5A',[50,50]]}


##----------Function to select dictionary to use-----

def getBacStats(media,bac):
    '''return the graph input list needed based on inputs'''
    if media == 'mac':
        return mac[bac]
    elif media == 'msa':
        return msa[bac]
    elif media == 'nutrient':
        return nutrient[bac]
    elif media == 'hek':
        return hek[bac]
    #fill in with rest of dict options
#add hek to this function



##--------------Image Genration functions-----------------

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

##---------Useful functions for transforming coordinates--------------------

def pythagMe(coord1,coord2):
    '''performs pythagorean theorum to return the 
    distance between two points. Input coords as [x,y]'''
    x1 = coord1[0]
    y1 = coord1[1]
    x2 = coord2[0]
    y2 = coord2[1]
    return math.sqrt((y2-y1)**2+(x2-x1)**2)

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

def genColHighlights(xData,yData,s,hlColor,):
    '''generates an additional scatterplot dataSet to match the one fed in by xData and yData.
    '''
    xOut = []
    yOut = [] 
    sOut = []
    cOut = []
    aOut = []
    for i in range(len(xData)):
        xOut.append(xData[i]+(s[i]/500))
        yOut.append(yData[i]+(s[i]/500))
        sOut.append(s[i]*.4)
        cOut.append(hlColor)
        aOut.append(.4)
    return [xOut,yOut,sOut,cOut,aOut]

##---------------------------functions for generating biofilm gloupyness--------------------

##-----OTU point grouping function--------------

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

#----making groups of points based on proximity

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

#-----functions for cleaning OTU lists of coords 

def parseList2Step(listIn): ### clean up this function
    '''takes a list of any organization in and returns a list 
    without subdivison: [[][[][]]] to [[][][]]'''
    cleanList = [] 
    listCheck = listIn 
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
    with no nesting, i.e. leaves one set '''
    verdict = True
    if type(listIn) == list:
        for i in listIn:
            if type(i) == list:
                if type(i[0]) == list:
                    verdict = False
    return verdict

#-----fully get rid of nesting to feed OTU coords into image generation------

def fullParse(listIn):
    '''loops through getting rid of [] until only left to parameters of check list'''
    workingList = listIn
    verdict = checkList(listIn)
    while verdict == False:
        workingList = parseList2Step(workingList)
        verdict = checkList(workingList)
    return workingList 

#-------given all the possible grouping of points, picks on based on cutoff value 

def chooseOTU(resultsIn,cutOffDist): ## lets eventually make this auto based on graph optimization
    '''picks a level of clustering based on a cutoff distance'''
    #---first makes a list to scan
    finalResults = [len(resultsIn),0] 
    for i in resultsIn:
        if i[1] > finalResults[1] and i[1]< cutOffDist:
            finalResults = i 
    return finalResults[0:3]

#------final sets of coords for mucous blobs--------

def makeOTUCoordGroups(listIn,cutoff=4.6):
    '''takes in a list of coordinates, and makes them into groups based on 
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

##-----functions for tangent poly generation and convex hull point selection----- 

#-----differnt ways of choosing which OTU points to include in polygon 

def convexHull(p):
    '''uses scipy to get the points of a convex hull from a group of points'''
    p = np.array(p)
    hull = ConvexHull(p)
    return p[hull.vertices,:]

def ccw_sort(p):
    p = np.array(p)
    mean = np.mean(p,axis=0)
    d = p-mean
    s = np.arctan2(d[:,0], d[:,1])
    return p[np.argsort(s),:]

#----picks tan points from circles surrounding colonies to make polygons for blobs-------------

def getTanPoints(center1,center2,r,mode='ccw'):
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
    if mode =='ccw':
        if x1< x2 and y1 >= y2:
            return [[x1+xAdd,y1+yAdd],[x2+xAdd,y2+yAdd]]
        elif x1 >= x2 and y1 >= y2:
            return [[x1+xAdd,y1-yAdd],[x2+xAdd,y2-yAdd]]
        elif x1 >= x2 and y1 < y2:
            return [[x1-xAdd,y1-yAdd],[x2-xAdd,y2-yAdd]]
        elif x1 < x2 and y1 < y2:
            return [[x1-xAdd,y1+yAdd],[x2-xAdd,y2+yAdd]]
    #''' #reverse signs for diff case 
    #hull uses this one
    elif mode == 'hull':
        if x1< x2 and y1 >= y2:
            return [[x1-xAdd,y1-yAdd],[x2-xAdd,y2-yAdd]]
        elif x1 >= x2 and y1 >= y2:
            return [[x1-xAdd,y1+yAdd],[x2-xAdd,y2+yAdd]]
        elif x1 >= x2 and y1 < y2:
            return [[x1+xAdd,y1+yAdd],[x2+xAdd,y2+yAdd]]
        elif x1 < x2 and y1 < y2:
            return [[x1+xAdd,y1-yAdd],[x2+xAdd,y2-yAdd]]
    #'''
def getTanPolyPoints(centerList,r,mode='ccw'):
    points = []  
    for i in range((len(centerList)-1)):
        results = getTanPoints(centerList[i],centerList[i+1],r,mode=mode)
        points.append(results[0])
        points.append(results[1])
    last = getTanPoints(centerList[-1],centerList[0],r,mode=mode)
    points.append(last[0])
    points.append(last[1])
    return points 


##----------------bringing Hek Mucous all together-------------------------------

def addBlobs(plotName,mask,xData,yData,color,r,cutoff=4.6,mode='ccw'):
    '''adds hulls to a graph based on OTU's of proximity, when given coordsList'''
    coordList=unScattify(xData,yData)
    OTUs = makeOTUCoordGroups(coordList,cutoff)
    for i in OTUs:
        #print(i)
        if len(i)>=3:
            if mode == 'hull':
                points = getTanPolyPoints(convexHull(i),r,mode=mode)
            elif mode == 'ccw':
                points = getTanPolyPoints(ccw_sort(i),r,mode=mode) #(1.2,700),(.65,200) (1.2375,750), (2.015,2000)
            #print(points)
            poly = plt.Polygon(points,facecolor =color)
            plotName.add_patch(poly)
            poly.set_clip_path(mask)


#------Adds bile around Ecoli---------------

def genHaloData(xData,yData,s,c,sMult=18.0,a=1):
    '''generates additionally scatter plot data to add color change halo around
  points fed in as x and y datasets '''
    xOut = []
    yOut = [] 
    sOut = []
    cOut = []
    aOut = []
    for i in range(len(xData)):
        xOut.append(xData[i])
        yOut.append(yData[i])
        sOut.append(s[i]*sMult)
        cOut.append(c)
        aOut.append(a)
    return [xOut,yOut,sOut,cOut,aOut]

def addHalo(plotName,mask,xData,yData,sIn,c,sMult,a=1):
    '''adds a halo to plotname, masked by mask, of color c generating dataset using
    genHaloData'''
    phData = genHaloData(xData,yData,sIn,c,sMult,a)
    phChange = plotName.scatter(phData[0],phData[1],s=phData[2],c=phData[3],alpha=phData[4],linewidths=0)
    phChange.set_clip_path(mask)

def addBoth(plotName,mask,xData,yData,sIn,c,sMult,a=1,cutoff=4.6):
    '''adds both a halo and blob at the same time'''
    sOut = [] 
    for i in sIn:
        sOut.append(i*sMult)
    r = -2.52+.583*math.log(sOut[0]) #this formula still needs to be adjusted 
    addBlobs(plotName,mask,xData,yData,c,r,cutoff,mode='hull')
    addHalo(plotName,mask,xData,yData,sIn,c,sMult,a)

def addBile(plotName,mask,xData,yData,s):
    '''Adds bile for ecoli on hek'''
    
    #addHalo(plotName,mask,xData,yData,s,'#4C6964',120.0,.45)
    #addHalo(plotName,mask,xData,yData,s,'#5B8159',92.0,.50)
    #addHalo(plotName,mask,xData,yData,s,'#57893B',90.0,.55)
    '''
    addHalo(plotName,mask,xData,yData,s,'#BE7403',15.0,1)
    addBlobs(plotName,mask,xData,yData,'#BE7403',1.25,6)
    '''
    '''
    #addHalo(plotName,mask,xData,yData,s,'#C6C53F',40.0,.65)
    addHalo(plotName,mask,xData,yData,s,'#B9A34A',35.0,.7)
    addHalo(plotName,mask,xData,yData,s,'#D9BC4B',30.0,.75)
    addHalo(plotName,mask,xData,yData,s,'#FF9B00',20.0,.80)
    addHalo(plotName,mask,xData,yData,s,'#FF7E00',18.0,.82)
    addHalo(plotName,mask,xData,yData,s,'#FF5100',16.0,.84)
    '''
    '''Ok so background hek color is #08272c so we will blend from this 
    '''

    addBoth(plotName,mask,xData,yData,s,'#08272c',12.0,cutoff=4)
    addBoth(plotName,mask,xData,yData,s,'#142e28',11.0,cutoff=4)
    addBoth(plotName,mask,xData,yData,s,'#203625',10.0,cutoff=4)
    addBoth(plotName,mask,xData,yData,s,'#2c3d21',9.0,cutoff=4)
    addBoth(plotName,mask,xData,yData,s,'#38451e',8.0,cutoff=4)
    #addHalo(plotName,mask,xData,yData,s,'#444c1b',7.0,1)
    addBoth(plotName,mask,xData,yData,s,'#444c1b',7.0,cutoff=4)
    addBoth(plotName,mask,xData,yData,s,'#515417',6.0,cutoff=4)
    addBoth(plotName,mask,xData,yData,s,'#5d5b14',5.0,cutoff=4)
    addBoth(plotName,mask,xData,yData,s,'#696210',4.0,cutoff=4)
    addBoth(plotName,mask,xData,yData,s,'#756a0c',3.0,cutoff=4)
    addBoth(plotName,mask,xData,yData,s,'#817109',2.5,cutoff=4)
    addBoth(plotName,mask,xData,yData,s,'#8d7905',2,1,cutoff=4)
    addBoth(plotName,mask,xData,yData,s,'#998002',1.5,cutoff=4)


    #addHalo(plotName,mask,xData,yData,s,'#FCFF24',40.0,.35)
    #addBlobs(plotName,mask,xData,yData,'#BE8F03',2.015,8)
    #addHalo(plotName,mask,xData,yData,s,'#BE8F03',40.0,1)
    #addBlobs(plotName,mask,xData,yData,'#BE8F03',2.015,8)
    #addHalo(plotName,mask,xData,yData,s,'#BE7403',15.0,1)
    #addBlobs(plotName,mask,xData,yData,'#BE7403',1.2375,6)
    #addHalo(plotName,mask,xData,yData,s,'#EA6400',4.0,1)
    #addBlobs(plotName,mask,xData,yData,'#EA6400',.63,6)
    
    addHalo(plotName,mask,xData,yData,s,'#EA5400',3.0,1)
    addBlobs(plotName,mask,xData,yData,'#EA5400',.55,4.0)
    
    #addHalo(plotName,mask,xData,yData,s,'',.0,1)
    #addHalo(plotName,mask,xData,yData,s,'',.0,1)

###------------------------------Other aesthetic additions--------------------------------------------------

#----Creates highlights-------------

def addRealisticPlate(plotName,center=[0,0],r=10):
    '''easy place to contain all the artists I created to get good
    shading on the plate, i.e. making oo into fo. Make sure plotName is global 
    variable name of already created subplot, center and radius are parameters of colored gel 
    circle used as clip mask for scatter plot ''' 
    #-Reference variables
    x = center[0]
    y = center[1]
    #-Creates elements
    circle2 = plt.Circle((x,y+.025),r+.65,ec = 'white', lw = 3,fill = False,alpha= .45 )#fc ='#929292',alpha= .35,)
    circle5 = plt.Circle((x,y+.025),r+.65,ec = 'black', lw = 1,fill = False,alpha= .25 ) #highlights on rim of dish
    #- goes center (,) radius(s), ec = 'edge color' lw = line width, alpha = opacity
    #arcs work by angle, 4th var setting start angle of arc, and theta2 = end angle counterclockwise from start 
    arc1 = patch.Arc((x,y+0.001),(r*2)+.05,(r*2)+.05,30,theta1=0,theta2=60,linewidth=.85,ec='w',capstyle='round',alpha=.55) #small bright weight arc near gel surface
    arcDark = patch.Arc((x,y+.020),(r*2)+.75,(r*2)+.75,110,theta1=0,theta2=360,linewidth=.85,ec='black',capstyle='round',alpha=.25) #black ring all the way around
    arc2 = patch.Arc((x,y+0.025),(r*2)+1.3,(r*2)+1.3,0,theta1=0,theta2=120,linewidth=1.25,ec='w',capstyle='round') #rim highlighting top 
    arc3 = patch.Arc((x,y+0.020),(r*2)+1,(r*2)+1,0,theta1=0,theta2=360,linewidth=6,ec='w',capstyle='round',alpha=.25) #fill rim glass color
    #-Fuzzy highlight on bottom side
    arc8 = patch.Arc((x,y-0.05),(r*2)+.5,(r*2)+.5,220,theta2=90,lw=5,ec='w',capstyle='round',alpha=.15) 
    arc4 = patch.Arc((x,y-0.05),(r*2)+.5,(r*2)+.5,180,theta2=120,lw=6,ec='w',capstyle='round',alpha=.15)
    arc5 = patch.Arc((x,y-0.05),(r*2)+.5,(r*2)+.5,140,theta2=180,lw=7,ec='w',capstyle='round',alpha=.15)
    #-Fuzzy highlight on top side
    arc6 = patch.Arc((x,y+.025),(r*2)+.5,(r*2)+.5,345,theta2=145,lw=7,ec='w',capstyle='round',alpha=.10)
    arc7 = patch.Arc((x,y+.025),(r*2)+.5,(r*2)+.5,0,theta2=100,lw=6,ec='w',capstyle='round',alpha=.10)
    arc9 = patch.Arc((x,y+.025),(r*2)+.5,(r*2)+.5,15,theta2=60,lw=5,ec='w',capstyle='round',alpha=.10)
    #angle sets loation of theta1, theta1 and 2 set bounds of arc len    
    #----------K then add them to the graph
    #circle2.set_clip_path(circle1)
    plotName.add_artist(arc1)
    plotName.add_artist(arc2)
    plotName.add_artist(arc3)
    plotName.add_artist(arc4)
    plotName.add_artist(arc5)
    plotName.add_artist(arc6)
    plotName.add_artist(arc7)
    plotName.add_artist(arc8)
    plotName.add_artist(arc9)
    plotName.add_artist(arcDark)
    plotName.add_artist(circle2)
    plotName.add_artist(circle5)

#------Creating a control plate that was not innoculated------------

def addControlPlate(plotName,gelColor,center,r=10):
    '''adds a control plate without any colonies on plotname
    of specified parameters. Make sure plotname is global variable of 
    already created subplot.'''
    x = center[0]
    y = center[1]
    circle3 = plt.Circle((x,y-.05),r-.5,ec = 'white', lw = 2,fill = False,alpha= .25 )#fc ='#929292',alpha= .35,)
    circle4 = plt.Circle((x,y-.05),r-.5,ec = 'black', lw = 1,fill = False,alpha= .35 )
    plotName.add_artist(circle3)
    plotName.add_artist(circle4)
    #--Show growth or not
    circle1 = plt.Circle((x,y),r,facecolor=gelColor,alpha=.35,edgecolor='white',linewidth = 3,)  # basic media circle
    plotName.add_artist(circle1)
    plotName.set_xlim(-12,36)
    addRealisticPlate(plotName,[x,y],r)  

###----------------------------Bringing it all together---------------------

#Plate it up is where all the magic happens

'''Any constants in plateItUp functon are across all plates, 
consider adding more to ListIn from dictionaries to further tailor appearances 
to specific strains/ media. Currently dictionary decides growth or no growth (listIn[0]),
plate color (listIn[1]), colony color (listIn[2]),and colony size range (listIn[3]).
'''

def plateItUp(listIn,controlPlate=True):
    '''generates a plate graphic from the outputs of getbach stats, 1 or 0 for growth or not,
    then plate color, and colony color'''
    #print(listIn)
    #--Genrating figure
    if controlPlate == True:
        fig = plt.figure(figsize=(8,4))
    else:
        fig = plt.figure()
    ax = fig.add_subplot()
    #-Setting Graph Attributes 
    fig.set_facecolor('black')
    ax.axis('off') #hide axes 
    ax.set_aspect(1) #make square
    #-Defining bounds of graph()
    ax.set_xlim(-12,12)
    ax.set_ylim(-12,12)   
    #--Adding Plate details below gel before scatter
    circle3 = plt.Circle((0,-.05),9.5,ec = 'white', lw = 2,fill = False,alpha= .25 )#fc ='#929292',alpha= .35,)
    circle4 = plt.Circle((0,-.05),9.5,ec = 'black', lw = 1,fill = False,alpha= .35 )
    ax.add_artist(circle3)
    ax.add_artist(circle4)
    #--Show growth or not                                    #usually a = .35 
    circle1 = plt.Circle((0,0),10,facecolor=listIn[1],alpha=0.55,edgecolor='white',linewidth = 3,)  # basic media circle
    maskCircle = plt.Circle((0,0),9.86,ec='black',lw=0,fill=False) #crop slightly before edge 
    ax.add_artist(maskCircle)
    ax.add_artist(circle1)
    if listIn[0] == 1:
        #-Genrate Scatter Data for colonies
        inocData = genInocPlate(9.5,[0,0],45,listIn[3],[listIn[2]]) #'#E36C7A','#F4F2E6'
        #print(inocData)
    
        
        highlightData = genColHighlights(inocData[0],inocData[1],inocData[2],'w')
        #-Use Data to graph scatter plots 
        if plateIn == 'hek' and bacIn == 'eColi':
          addBile(ax,maskCircle,inocData[0],inocData[1],inocData[2])
        
        #----adding colonies using ScatterPlot 
        scatter = ax.scatter(inocData[0],inocData[1],s=inocData[2],c = inocData[3]) #colonies 
        
        #--------testing scaling--------
        #ax.scatter([0],[0],s=[700])
        #testCirc = plt.Circle((0,0),1.235,alpha=.3,facecolor='y') #1.235 to 700 ratio 
        #ax.add_artist(testCirc)

        ax.scatter(highlightData[0],highlightData[1],s=highlightData[2],c=highlightData[3],alpha=highlightData[4],linewidths=0) #highlights
        scatter.set_clip_path(circle1)  
    #-Add plate shading
    addRealisticPlate(ax,[0,0],10)
    if controlPlate == True:
       addControlPlate(ax,listIn[1],[24,0],10)
    
    
###---------testing vars go in here---------------------------------------------------

plateItUp(getBacStats(plateIn,bacIn),False)

#----------------------------Show graph------------

#plt.show(block=False)
plt.savefig('C:\\Users\\lqmey\\OneDrive\\Desktop\\Python Code\\Projects Lab\\plate_sim.svg',format='svg')
plt.pause(45)
#plt.close()
