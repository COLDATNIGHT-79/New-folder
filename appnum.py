""" import numpy as np
a=np.zeros(12)
print(a)
print(type(a))
print(type(a[0]))

b=np.zeros(3,dtype=int)
print(b[0])
print(a.shape) """

# import numpy as np
""" z=np.zeros(10)
print(z)
print(z.shape)

z.shape=(10,1)
print(z)

k=np.zeros(4)
k.shape=(2,2)
print(k)

p=np.zeros((4,5))
print(p)

c=np.ones((2,5))
print(c)

m=np.empty(3)
print(m) """

""" z=np.array([[1,2],[3,4]])
print(z)

n=np.array([10,20,30,40,50])
print(n)

t=np.array([[1,2],[3,4]])
print(t)

r=np.array([[[1,2,3],[2,3,4]],[[4,6,7],[3,4,6]]])
print(r) """

#For checking the dimensions of numpy
""" import numpy as np
t=np.array([[[1,2,3],[2,3,4]],[[1,2,3],[2,3,5]]])
print(t.ndim)
 """
#Array indexing
""" import numpy as np
d=np.array([1,2,3,4,5,6])
print(d[2]) """

#Adding the numbers using the indexing
""" import numpy as np
j=np.array([23,45,67,89,78,78])
print(j[2]+j[4]) """

#Array indexing in the 2d array
""" import numpy as np
h=np.array([[1,2,3,4,5],[2,3,4,5,6]])
print('2nd element on 2nd row: ',h[1,1]) """

#Array indexing of the 3d array
""" import numpy as np
k=np.array([[[1,2,3],[2,3,4]],[[3,4,5],[10,6,8]]])
print(k[1,1,0]) """

#Sciling in the numpy array
""" import numpy as np
l=np.array([10,23,45,67,89,90,78,90,56])
print(l[1:7:2])
 """

#Sciling the 2d arrays
""" import numpy as np
n=np.array([[1,2,3],[2,5,7]])
print(n[1,1:2]) """

#How to check the datatype of the array
""" import numpy as np
r=np.array(['apple','a','fgh','jkn'])
print(r.dtype) """

#For integer datatype
""" import numpy as np
e=np.array([1,2,3,4,5,6],dtype='i4')
print(e)
print(e.dtype) """

#print shape of 2d array
""" import numpy as np
h=np.array([[[1,2,3],[2,3,4]],[[1,2,3],[4,5,6]]])
print(h.shape) """

#Reshaping an array
""" import numpy as np
c=np.array([1,2,3,4,5,6,7,8,9,2,34,67])
newarr=c.reshape(4,3)
print(newarr)
print(c.shape) """

#Converting 1d array inton 3d array
""" import numpy as np
x=np.array([1,2,3,4,5,6,7,8,12,3,4,23])
f=x.reshape(2,3,2)
print(f)
 """

#Iterating 1d array
""" import numpy as np
d=np.array([1,2,3,4,5,6])
for i in d:
    print(i) """

#Iterating in 2d array
import numpy as np
h=np.array([[1,2,3,4],[2,5,6,7]])
for i in h:
    for j in i:
        print(j)