#ok lets actually get to work
#im ready to make this happen 

#Luke Meyers 
# Creatinf Differential and Selective Media Sim
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
from typing import List
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

import random
import sys

#sys.path.insert(0,"C:\\Users\\lqmey\\OneDrive\\Desktop\\Python Code\\Bioinfo") 
#make bioinfo functions available for import 

###------------------ADD INPUTS BELOW-----------------------------

##------------Input Plate Media Selection--------------
plateIn = 'mac'
#plateIn = 'msa'
#plateIn = 'blo'
#plateIn = 'hek'
#plateIn = 'emb'

##--------------Input Bacteria Selection-----------------

#bacIn = 'staphEp'
#bacIn = 'staphAur'
bacIn = 'eColi'
#bacIn = 'myco'
#bacIn = #ADD NEW OPTIONS W/ DATA


##---------- Set of dictionaries for adding Plate outcomes----------

mac = {'staphEp':[0], #wow ok crash course on syntax from this 
            'staphAur':[0], 
            'eColi': [1,'pink','white'],
            'myco':[0],}
#gets a 1 if it will grow, need to go back and add hex color

#add other dicts here


##----------Function to select dictionary to use-----

def getBacStats(media,bac):
    '''return the graph input list needed based on inputs'''
    if media == 'mac':
        return mac[bac]
    #elif media == 'msa':
        #return msa[bac] 
    #fill in with rest of dict options




##--------------Image Genration functions-----------------

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


##--------------------Bringing Everything Together----------------

def genScatterPlate(listIn,colonNum=30,duration=40):
    '''creates a plate like image using a random scatterplot masked
    with a circle to look like a petri dish. ColonNum sets num of 
    scatter data point'''
    if listIn[0] > 0:
        ax = plt.subplot()
        xData = genScatterData(colonNum)[0]
        yData = genScatterData(colonNum)[1]
            #generate datapoints for coloniy location
        centerX = avgList(xData)
        centerY = avgList(yData)
            #get averages for all poitns to center dish
        plt.xlim(getBound(xData,'lower')-stdev(xData),getBound(xData,'upper')+stdev(xData))
        plt.ylim(getBound(yData,'lower')-stdev(yData),getBound(yData,'upper')+stdev(yData))
            #plot graph around where data points got generated 
        ax.set_aspect(1) #sets aspect of graph view need to get square/circle not elipse 
        circle = plt.Circle((centerX,centerY),(getBound(xData,'upper')-centerX),facecolor=listIn[1],alpha=.3,edgecolor='black',linewidth = 1) 
            #pretty sure 2nd arg is radius #need to select for biggest radius 
        ax.add_artist(circle) #add circle
        #plt.figure(figsize=(7,5)) #this creates a new figure window 
        scatter = ax.scatter(xData,yData,color=listIn[2]) #need # to recognize Hex color 
        ax.axis('off') #hides axis and labels 
        scatter.set_clip_path(circle) 

        #k lets show the graph 
        plt.show(block=False) #cant find much on what block does but necessarty tpo close 
        plt.pause(duration) #keeps viewer open 
        plt.close() #closes viewer


##---------- K this is where the actual Code Happens------------------------

genScatterPlate(getBacStats(plateIn,bacIn))
#print(mac['eColi'])