""" import matplotlib.pyplot as plt
plt.plot([1,2,4,7,8,6],[7,8,9,0,4,7]) #Here we are using the python list to make graph as well as making the array
print(plt.show()) """

#NumPy array in matplotlib
""" import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,78])
y=np.array([35,80])

print(plt.plot(x,y))
print(plt.show()) """

#Above part can be done in this manner also
""" import matplotlib.pyplot as plt
import numpy as np

x=np.array([2,56])
y=np.array([3,98])

plt.scatter(x,y,color=["r","b"]) #or plt.plot(x,y,'o')
print(plt.show()) """


#Multiple points
""" import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,3,56])
y=np.array([4,5,6,78])

plt.plot(x,y)
print(plt.show()) """

#Plotting without x axis
""" import matplotlib.pyplot as plt
import numpy as np
y=np.array([2,5,7,9,4,8,9,7,6,8])

plt.plot(y)
print(plt.show()) """

#Matplotlib markers
""" import matplotlib.pyplot as plt
import numpy as np

y=np.array([2,3,4,5,6,7,34,5])

plt.plot(y,marker='*')
print(plt.show()) """

#Matplotlib line charts
""" import matplotlib.pyplot as plt
import numpy as np

y=np.array([3,4,5,67,89,23,45,12,34,2,3])

plt.plot(y,linestyle='dotted',color='g',linewidth='20')
plt.show() """

#Draw two lines by specifying a plt.plot()
""" import matplotlib.pyplot as plt
import numpy as np

y=np.array([1,4,56,78,45,67,89])
y1=np.array([34,56,7,8,9,23,0])

plt.plot(y)
plt.plot(y1)

plt.show() """

#Add labels to the x axis and y axis using matplotlib
""" import matplotlib.pyplot as plt
import numpy as np

x=np.array([50,100,150,200,250,300,350,350,400])
y=np.array([20,40,60,80,100,120,140,160,180])
plt.plot(x,y)
plt.title("Sports watch data",loc='left')
plt.xlabel("Average pulse")
plt.ylabel("Calorie burned")
plt.show() """

#BAR Charts
""" import matplotlib.pyplot as plt
import numpy as np

x=np.array(["A","B","C","D"])
y=np.array([7,8,9,5]) #This gives vertical bar 

plt.bar(x,y)
plt.show() """

#Horizantal chart
""" import matplotlib.pyplot as plt
import numpy as np

x=np.array(["A","B","C","D"])
y=np.array([7,8,9,5]) #This gives vertical bar 

plt.barh(x,color='pink',width=0.1,height=0.7)
plt.show()
 """
#Histogram
""" import matplotlib.pyplot as plt
import numpy as np

x=np.random.normal(170,10,240)
print(plt.hist(x))
plt.show() """

#Pie charts
""" import matplotlib.pyplot as plt
import numpy as np
x=np.array([34,54,64,74])
plt.pie(x)
plt.show() """

#Naming in the pie chart
""" import matplotlib.pyplot as plt
import numpy as np
x=np.array([45,67,89,45,34])
d=["Apples","Cherry","Grapes","Berry","Lemon"]

plt.pie(x,labels=d)
plt.show() """

#Starting the angle
""" import matplotlib.pyplot as plt
import numpy as np

x=np.array([45,67,89,45,34])
d=["Apples","Cherry","Grapes","Berry","Lemon"]

plt.pie(x,labels=d,startangle=90)
plt.show() """

#pull the apple wedges
""" import matplotlib.pyplot as plt
import numpy as np

x=np.array([45,67,89,45,34])
d=["Apples","Cherry","Grapes","Berry","Lemon"]
m=[0.2,0,0,0,0]

plt.pie(x,labels=d,explode=m)
plt.show() """

#Addind the color
""" import matplotlib.pyplot as plt
import numpy as np

x=np.array([45,67,89,45,34])
d=["Apples","Cherry","Grapes","Berry","Lemon"]
m=["Black","Pink","c","Red","Grey"]

plt.pie(x,labels=d,colors=m)
plt.show() """

#Add a legend
""" import matplotlib.pyplot as plt
import numpy as np

x=np.array([45,67,89,45,34])
d=["Apples","Cherry","Grapes","Berry","Lemon"]

plt.pie(x,labels=d)
plt.legend()
plt.show() """

#Heading on the legends
import matplotlib.pyplot as plt
import numpy as np

x=np.array([45,67,89,45,34])
d=["Apples","Cherry","Grapes","Berry","Lemon"]

plt.pie(x,labels=d)
plt.legend(title="Some Fruits")
plt.show()

