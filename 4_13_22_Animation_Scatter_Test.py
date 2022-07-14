##Luke Meyers 4/13/22
#Animation test on matplotlib 

from matplotlib import pyplot as plt 
from matplotlib.animation import FuncAnimation
import random 
import numpy as np 

x = []
y = []
colors = []
tckr = 0


fig = plt.figure(figsize=(5,5))


def myAnimation(i):
    x.append(random.randint(0,100))
    y.append(random.randint(0,100))
    #colors.append(((230+random.choice(range(25)),(180+random.choice(range(75))),(60+random.choice(range(195))))))
    colors.append(random.choice(['#FFE6B6','#F9D38A','#F7E6C3'])) #.choice needs []
    area = random.randint(0,25)*random.randint(0,25)
    plt.xlim(0,100)
    plt.ylim(0,100)
    plt.scatter(x,y,c=colors,s=area,alpha=.5)
   


animation = FuncAnimation(fig,myAnimation,interval=100) #changing interval makes growth faster or slower?
'''so it does it also just makes it choppy, better to find away to insert smaller growth intervals'''

plt.show()
plt.wait(40)
plt.close()