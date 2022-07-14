#Last Updated By Luke Meyers 5/11/22

#Luke Meyers 
# Creating Differential and Selective Media Sim
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

import random
import sys

#sys.path.insert(0,"C:\\Users\\lqmey\\OneDrive\\Desktop\\Python Code\\Bioinfo") 
#make bioinfo functions available for import 

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
#bacIn = 'myco'
#bacIn = 'pseudomonas'
#bacIn = 'salmonella'
#bacIn = #ADD NEW OPTIONS W/ DATA 


##---------- Set of dictionaries for adding Plate outcomes----------

#MacConkey agar is a selective and differential media that is used to idenity gram-negative bacteria and lactose-fermenting or non-lactose fermenting
mac = {'staphEp':[0,'#E36C7A'],
            'staphAur':[0,'#E36C7A'], 
            'eColi': [1,'#E36C7A','#E4A7B9'],
            'myco':[0,'#E36C7A'],
            'pseudomonas':[1,'#E36C7A','#F4F2E6'],
            'salmonella':[1,'#E36C7A', '#FDD999']}
#could use random choice function to distniguish between pseudomonas and salmonella

#gets a 1 if it will grow, need to go back and add hex color

#add other dicts here

#Mannitol Salt Agar is differential media that is used to idenify staph auerus (yellow colonies) from other forms of staph (pink/light red colonies)
msa = {'staphEp':[1,'#E90E0E','#E36C7A'],
           'staphAur':[1, '#E90E0E', '#F6B900'],
           'eColi': [0,'#E90E0E'],
           'myco':[0,'#E90E0E'],
           'pseudomonas':[0,'#E90E0E'],
           'salmonella':[0,'#E90E0E']}

#Nutrient Agar is a non-selective media that can grow all of the strains of bacteria we have selected for the simulation
nutrient = {'staphEp':[1,'#F2DF61','#F1E59D'],
                'staphAur':[1,'#F2DF61', '#F3D41B'],
                'eColi': [1,'#F2DF61', '#F3F377'],
                'myco': [1,'#F2DF61', '#F6F2DA'],
                'pseudomonas':[1,'#F2DF61','#EDF7E3'],
                'salmonella':[1,'#F2DF61','#FAE9AB'],
                }
#could use random choice function here to pic the colony colors to get variation on white color

#Hektoen eneteric agar is a selective and differential media used to identify and isolate salmonella, looks for lactose fermenting bacteria, hydorgen sulfide
#production as well as inhibit the growth of gram-positive bacteria 
hek = {'staphEp':[0,'#FF4E00'],
       'staphAur':[0,'#FF4E00'],
       'eColi':[1, '#FF4E00', '#FFDB00'],
        #plate is blue but ecoli turn plate red/orange color due to bile production
       'myco':[0,'#FF4E00'],
       'pseudomonas':[1,'#14707F', '#EDF7E3'],
       #check with Dr. R on pseudomonas for this media
       'salmonella':[1,'#14707F','#97CF5A']}

        

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
    addRealisticPlate(plotName,[x,y],r)  





#-------Bringing it all together---------------------

def plateItUp(listIn):
    '''generates a plate graphic from the outputs of getbach stats, 1 or 0 for growth or not,
    then plate color, and colony color'''
    print(listIn)
    #--Genrating figure
    fig = plt.figure(figsize=(8,4))
    ax = fig.add_subplot()
    #-Setting Graph Attributes 
    fig.set_facecolor('black')
    ax.axis('off') #hide axes 
    ax.set_aspect(1)
    #-Defining bounds of graph()
    ax.set_xlim(-12,36)
    #ax.set_xlim(-12,12)
    ax.set_ylim(-12,12)   
    #--Adding Plate details below gel before scatter
    circle3 = plt.Circle((0,-.05),9.5,ec = 'white', lw = 2,fill = False,alpha= .25 )#fc ='#929292',alpha= .35,)
    circle4 = plt.Circle((0,-.05),9.5,ec = 'black', lw = 1,fill = False,alpha= .35 )
    ax.add_artist(circle3)
    ax.add_artist(circle4)
    #--Show growth or not
    circle1 = plt.Circle((0,0),10,facecolor=listIn[1],alpha=.35,edgecolor='white',linewidth = 3,)  # basic media circle
    ax.add_artist(circle1)
    if listIn[0] == 1:
        #-Genrate Scatter Data for colonies
        inocData = genInocPlate(9.5,[0,0],45,[45,50],[listIn[2]]) #'#E36C7A','#F4F2E6'
        highlightData = genColHighlights(inocData[0],inocData[1],inocData[2],'w')
        #-Use Data to graph scatter plots 
        scatter = ax.scatter(inocData[0],inocData[1],s=inocData[2],c = inocData[3]) #colonies 
        ax.scatter(highlightData[0],highlightData[1],s=highlightData[2],c=highlightData[3],alpha=highlightData[4]) #highlights
        scatter.set_clip_path(circle1)  
    #-Add plate shading
    addRealisticPlate(ax,[0,0],10)
    addControlPlate(ax,listIn[1],[24,0],10)
    



###---------testing vars go in here---------------------------------------------------


plateItUp(getBacStats(plateIn,bacIn))


#----------------------------Show graph------------

plt.show(block=False)
plt.savefig('C:\\Users\\lqmey\\OneDrive\\Desktop\\Python Code\\Projects Lab\\plate_sim.svg',format='svg')
plt.pause(45)
#plt.close()
