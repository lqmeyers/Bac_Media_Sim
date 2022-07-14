##Luke Meyers 4/14/22 
#Piecewise function test 

#the usual 
import matplotlib as mpl
from matplotlib import pyplot as plt 
import numpy as np 

'''
xData = [] 
yData = []

xData = [1,2,3,4] #Test Data 
yData = [2,4,6,8]
'''
def pieceWise(x1,y1,x2,y2,x3=0,y3=0):#inputs need to be cooridinates 
    '''creates a peicewise function using inputs as coordinates of junctions'''
    xData = []
    yData = [] 
    piece1 = x2-x1
    m1 = ((y2-y1)/(x2-x1))
    for num in range(piece1):
        xData.append(x1+num)
        yData.append(y1+(m1*num))
    if x3 or y3 > 0:
        piece2 = x3-x2
        m2 = ((y3-y2)/(x3-x2))
        for num in range(piece2):
            xData.append(x2+num)
            yData.append(y2+(m2*num))
    return [xData,yData]

#print(pieceWise(0,4,8))
#x = pieceWise(0,5,4,4,8,8)[0]
#y = pieceWise(0,5,4,4,8,8)[1]

x = pieceWise(0,5,4,4)[0]
y = pieceWise(0,5,4,4)[1]

fig, ax = plt.subplots() 
ax.plot(x,y)

plt.show()
plt.pause(30)
plt.close
