##Luke Meyers 4/13/22
#Animation test on matplotlib 

from turtle import circle
from matplotlib import pyplot as plt 
from matplotlib.animation import FuncAnimation
import random 
import numpy as np 

x = []
y = []
colors = []



#fig = plt.figure(figsize=(5,5))
fig, ax=plt.subplots()
ax.set_aspect(1)
circle = plt.Circle((50,50),50,facecolor='#ECE0A1',alpha=.3,edgecolor='black',linewidth = 2)


def myAnimation(i):
    x.append(random.randint(0,100))
    y.append(random.randint(0,100))
    #colors.append(((230+random.choice(range(25)),(180+random.choice(range(75))),(60+random.choice(range(195))))))
    colors.append(random.choice(['#FFE6B6','#F9D38A','#F7E6C3'])) #.choice needs []
    area = random.randint(0,20)*random.randint(0,20 )
    plt.xlim(-1,101)
    plt.ylim(-1,101)
    myScatter = plt.scatter(x,y,c=colors,s=area,alpha=.5) #
    myScatter.set_clip_path(circle)
   
ax.axis('off')



ax.add_artist(circle)
animation = FuncAnimation(fig,myAnimation,interval=100) #changing interval makes growth faster or slower?
'''so it does it also just makes it choppy, better to find away to insert smaller growth intervals'''

plt.show()
print('shown')
plt.pause(40)
plt.close()