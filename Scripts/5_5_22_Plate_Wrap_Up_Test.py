## Luke Meyers 5/2/22
# testing a scatterplot with shadows on the points 

import matplotlib as mpl 
import matplotlib.pyplot as plt 
import matplotlib.patches as patch
import numpy as np 
import math
import random


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

def revPythag(len,angle):
    '''does the trig to get x and y lens of a 
    triangle using len of hypotnuse and angle at bottom'''
    



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
        
#-----------functions for shading?--------------------------

def addCircle(plotName,circleName): #really just a test function
    '''Adds a circle defned by circleName to plotName'''
    plotName.add_artist(circleName) #ok so supposedly this works too 

def addRealisticPlate(plotName):
    '''easy place to contain all the artists I created to get good
    shading on the plate, i.e. making oo into fo. Make sure plotName is global 
    variable name of already created subplot ''' 
    #------First creates elements-------------
    circle2 = plt.Circle((0,.025),10.65,ec = 'white', lw = 3,fill = False,alpha= .45 )#fc ='#929292',alpha= .35,)
    circle5 = plt.Circle((0,.025),10.65,ec = 'black', lw = 1,fill = False,alpha= .25 ) #highlights on rim of dish
    #- goes center (,) radius(s), ec = 'edge color' lw = line width, alpha = opacity
    #arcs work by angle, 4th var setting start angle of arc, and theta2 = end angle counterclockwise from start 
    arc1 = patch.Arc((0,0.001),20.05,20.05,30,theta1=0,theta2=60,linewidth=.85,ec='w',capstyle='round',alpha=.55) #small bright weight arc near gel surface
    arcDark = patch.Arc((0,.020),20.75,20.75,110,theta1=0,theta2=360,linewidth=.85,ec='black',capstyle='round',alpha=.25) #black ring all the way around
    arc2 = patch.Arc((0,0.025),21.3,21.3,0,theta1=0,theta2=120,linewidth=1.25,ec='w',capstyle='round') #rim highlighting top 
    arc3 = patch.Arc((0,0.020),21,21,0,theta1=0,theta2=360,linewidth=6,ec='w',capstyle='round',alpha=.25) #fill rim glass color
    #-Fuzzy highlight on bottom side
    arc8 = patch.Arc((0,-0.05),20.5,20.5,220,theta2=90,lw=5,ec='w',capstyle='round',alpha=.15) 
    arc4 = patch.Arc((0,-0.05),20.5,20.5,180,theta2=120,lw=6,ec='w',capstyle='round',alpha=.15)
    arc5 = patch.Arc((0,-0.05),20.5,20.5,140,theta2=180,lw=7,ec='w',capstyle='round',alpha=.15)
    #-Fuzzy highlight on top side
    arc6 = patch.Arc((0,.025),20.5,20.5,345,theta2=145,lw=7,ec='w',capstyle='round',alpha=.10)
    arc7 = patch.Arc((0,.025),20.5,20.5,0,theta2=100,lw=6,ec='w',capstyle='round',alpha=.10)
    arc9 = patch.Arc((0,.025),20.5,20.5,15,theta2=60,lw=5,ec='w',capstyle='round',alpha=.10)
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



##--------Points along circle for testing------------

#pointIn = [-3.686,9.295] #ok got it working with (-,+) quadrant 
#pointIn = [3.800,9.249]#set point for quad 1 
coordIn = getRandCircPoint(9.5) #Seed point for entire streak generator #add circle radius here 


def plateItUp(listIn):
    '''generates a plate graphic from the outputs of getbach stats, 1 or 0 for growth or not,
    then plate color, and colony color'''
    #--Genrating figure
    fig = plt.figure()
    ax = fig.add_subplot()
    #-Setting Graph Attributes 
    fig.set_facecolor('black')
    ax.axis('off') #hide axes 
    ax.set_aspect(1)
    #-Defining bounds of graph()
    ax.set_xlim(-12,12)
    ax.set_ylim(-12,12)   
    #--Adding Plate details below gel before scatter
    circle3 = plt.Circle((0,-.05),9.5,ec = 'white', lw = 2,fill = False,alpha= .25 )#fc ='#929292',alpha= .35,)
    circle4 = plt.Circle((0,-.05),9.5,ec = 'black', lw = 1,fill = False,alpha= .35 )
    ax.add_artist(circle3)
    ax.add_artist(circle4)
    #-Genrate Scatter Data for colonies
    inocData = genInocPlate(9.5,[0,0],45,[45,50],[listIn[2]]) #'#E36C7A','#F4F2E6'
    highlightData = genColHighlights(inocData[0],inocData[1],inocData[2],'w')
    #--Show growth or not
    circle1 = plt.Circle((0,0),10,facecolor=listIn[1],alpha=.35,edgecolor='white',linewidth = 3,)  # basic media circle
    ax.add_artist(circle1)
    if listIn[0] == 1:
        scatter = ax.scatter(inocData[0],inocData[1],s=inocData[2],c = inocData[3]) #colonies 
        ax.scatter(highlightData[0],highlightData[1],s=highlightData[2],c=highlightData[3],alpha=highlightData[4]) #highlights
        scatter.set_clip_path(circle1)  
    #-Add plate shading
    addRealisticPlate(ax)
    



###------------------------------------------Input testing vars here---------------------------------------------------


plateItUp([1,'#E36C7A','#F4F2E6'])


#------Show graph------------

plt.show(block=False)
plt.savefig('C:\\Users\\lqmey\\OneDrive\\Desktop\\Python Code\\Projects Lab\\plate_sim.svg',format='svg')
plt.pause(45)
plt.close()


'''
#inocData = genInocPlate(9.5,[0,0],45,[45,50],['#FFF1C5']) Test model 
inocData = genInocPlate(9.5,[0,0],45,[45,50],['#F4F2E6']) #'#E36C7A','#F4F2E6'


#print(genColHighlights(inocData[0],inocData[1],inocData[2],'w'))
highlightData = genColHighlights(inocData[0],inocData[1],inocData[2],'w')


##----------------Generating the Figure-----------------------------------

fig = plt.figure()
ax = fig.add_subplot() #generate mpl figure 
fig.set_facecolor('black')


#'#FFCF55' Testing Colors I think 
#'#FFF1C5'

#-----Add highlights on bottom of gel below scatter first-------------
circle3 = plt.Circle((0,-.05),9.5,ec = 'white', lw = 2,fill = False,alpha= .25 )#fc ='#929292',alpha= .35,)
circle4 = plt.Circle((0,-.05),9.5,ec = 'black', lw = 1,fill = False,alpha= .35 )
ax.add_artist(circle3)
ax.add_artist(circle4)

#addCircle(ax,circle3)

#------------Actually add the scatter plot data----------------------------

scatter = ax.scatter(inocData[0],inocData[1],s=inocData[2],c = inocData[3]) #colonies 
ax.scatter(highlightData[0],highlightData[1],s=highlightData[2],c=highlightData[3],alpha=highlightData[4]) #highlights


#-----Manually testing highlights 
#scatter = ax.scatter([0,1,2,3],[0,2,4,6],s=[75,75,75,75],c=['#FFF1C5','#FFF1C5','#FFF1C5','#FFF1C5'])
#scatter = ax.scatter([0.07,1.07,2.07,3.07],[0.07,2.07,4.07,6.07],s=[50,50,50,50],c=['w','w','w','w'],alpha=[.25,.25,.25,.25])
#scatter = ax.scatter([0.1,1.1,2.1,3.1],[0.1,2.1,4.1,6.1],s=[25,25,25,25],c=['w','w','w','w'],alpha=[.5,.5,.5,.5])

##---------------------Defining Necessary Graph parameters-----------------------------

ax.axis('off') #hide axes 
ax.set_aspect(1)

##-----Defining bounds of graph()
ax.set_xlim(-12,12)
ax.set_ylim(-12,12)

##--------Add circle for plate--------------

circle1 = plt.Circle((0,0),10,facecolor='#E36C7A',alpha=.35,edgecolor='white',linewidth = 3,)  # basic media circle
#'#ECE0A1' #testing plate color 

##------Petri Dish Highighing--------------

addRealisticPlate(ax)


#scatter2.set_clip_path(circle) 

'''


