""" import matplotlib.pyplot as plt
import seaborn as sns

sns.displot([0,1,2,3,4,5])
plt.show() """

#Set a background as white
""" import seaborn as sns
import matplotlib.pyplot as plt

tips=sns.load_dataset('tips')
sns.set_style('darkgrid')

sns.countplot(x='sex',data=tips)

plt.show()
 """
#Seaborn color palette
""" import seaborn as sns
import matplotlib.pyplot as plt

c=sns.color_palette()
sns.palplot(c)
plt.show() """

#
import numpy as nd
import seaborn as sn
import matplotlib.pyplot as plt

d=nd.random.randint(low=1,high=100,size=(10,10))
print("Thejnmh ")
print(d)
hm=sn.heatmap (data=d)
plt.show()