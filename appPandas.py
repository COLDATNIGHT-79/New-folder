""" import pandas as pd
from pandas import Series
ser_1=Series([1,2,3,4,-6,-8,13])
print(ser_1) """

#Create data frame
""" import pandas as pd
my={'cars':['BMW','VOLVO','AUDI'],'passings':[3,7,9]}
n=pd.DataFrame(my)
print(n)
 """

#Pandas import
""" import pandas as pd

df= pd.read_csv('data1.csv')
print(df.to_string()) """

#BY default printing first five and last five
""" import pandas as pd
df=pd.read_csv('data1.csv')
print(df)
print
 """

#displaying rows
""" import pandas as pd
pd.options.display.max_rows=999
df=pd.read_csv('data1.csv')
print(df) """

#Return a data frame with no empty cells
""" import pandas as pd
df=pd.read_csv('data1.csv')
new_df=df.dropna()
print(new_df.to_string())
 """

#Remove all the rows and the null value
""" import pandas as pd
df=pd.read_csv('data1.csv')
df.dropna(inplace=True)
print(df.to_string()) """

#Replacing the null value with number
""" import pandas as pd
df=pd.read_csv('data1.csv')
df.fillna(130,inplace = True)
print(df.to_string()) """

#Series
""" from pandas import Series
s=Series([1,2,2,3,-3,-5,8,13])
print(s) """

#Arrays representation of series
""" from pandas import Series
d=Series([1,3,4,5,6,7,8,-1,-2,-3,-19])
print(d.values) """

#TP get the index of series
""" from pandas import Series
d=Series([1,3,4,5,6,7,8,-1,-2,-3,-19])
print(d.index) """

#Create a series with custom index:
""" from pandas import Series
d=Series([1,3,4,5,6],index=['a','b','c','d','e'])
print(d) """

#GET A VALUE FROM SERIES
""" from pandas import Series
d=Series([1,3,4,5,6],index=['a','b','c','d','e'])
print(d[4]==d['c']) """

#To get a value from the index
""" from pandas import Series
d=Series([1,3,4,5,6],index=['a','b','c','d','e'])
print(d[['c','a','d']])
 """

#Get the values greater than zero
""" from pandas import Series
d=Series([0,3,4,5,-6],index=['a','b','c','d','e'])
print(d[d > 0]) """

#Scalar multipy
""" from pandas import Series
d=Series([1,3,4,5,6],index=['a','b','c','d','e'])
print(d*2) """

#Apply numpy function
""" from pandas import Series
d=Series([1,3,4,5,6],index=['a','b','c','d','e'])
import numpy as np
b=np.exp(d)
print(b) """

#Creating a series by passing in a dictionary
""" from pandas import Series
r={'ghee':100, 'choco':50,'biere': 600}
d= Series(r)
print(d)
print(d['ghee']) """

#RE order a series by passing in an index
""" from pandas import Series,DataFrame
import pandas as pd
dict_1 = {'foo' : 100, 'bar' : 200, 'baz' : 300}
index = ['foo', 'bar', 'baz', 'qux']
ser_4 = Series(dict_1, index=index)
print(ser_4)
print(ser_4.isnull()) """ #gives true or false value

#Series automatically aligns differently indexed data in arthematic operations:
""" from pandas import Series,DataFrame
import pandas as pd
dict_1 = {'foo' : 100, 'bar' : 200, 'baz' : 300}
ser_3 = Series(dict_1)
index = ['foo', 'bar', 'baz', 'qux']
ser_4 = Series(dict_1, index=index)
print(ser_4+ser_3) """

#naming a series
""" from pandas import Series,DataFrame
import pandas as pd
dict_1 = {'foo' : 100, 'bar' : 200, 'baz' : 300}
index = ['foo', 'bar', 'baz', 'qux']
ser_4 = Series(dict_1, index=index)
ser_4.name='crazy as heck'
ser_4.index.name = 'label'
print(ser_4) """

#Data Frame Creation
""" from pandas import Series,DataFrame
import pandas as pd
data_1={'State': ['va','va','va','md','md'],'Year':[2011,2012,2013,2014,2015],'Popu.':[5.0,5.1,5.2,5.3,5.4]}
df_1=DataFrame(data_1)
print(df_1) """

#Create a Dataframe specifying a sequence of colums
""" from pandas import Series,DataFrame
import pandas as pd
data_1={'State': ['va','va','va','md','md'],'Year':[2011,2012,2013,2014,2015],'Popu.':[5.0,5.1,5.2,5.3,5.4]}
df_1=DataFrame(data_1)
df_2=DataFrame(data_1,columns=['Year','State','Pop'])
print(df_2)
 """

#Making null which are not present in the data given

""" from pandas import Series,DataFrame
import pandas as pd
data_1={'State': ['va','va','va','md','md'],'Year':[2011,2012,2013,2014,2015],'Popu.':[5.0,5.1,5.2,5.3,5.4]}
df_1=DataFrame(data_1)
df_2=DataFrame(data_1,columns=['Year','State','Pop'])
df_3 = DataFrame(data_1, columns=['year', 'state', 'pop', 'unempl'])
print(df_2)
print(df_3) """

#Retriving a coloum key,returing a series
""" from pandas import Series,DataFrame
import pandas as pd
import numpy as np
data_1={'State': ['va','va','va','md','md'],'Year':[2011,2012,2013,2014,2015],'Pop.':[5.0,5.1,5.2,5.3,5.4]}
# df_1=DataFrame(data_1)
# df_2=DataFrame(data_1,columns=['Year','State','Pop'])
df_3 = DataFrame(data_1, columns=['Year', 'State', 'Pop', 'unempl'])
# print(df_2)
print(df_3['State']) """

#Retriving a column by attribute,returning a series
""" from pandas import Series,DataFrame
data_1={'State': ['va','va','va','md','md'],'Year':[2011,2012,2013,2014,2015],'Pop.':[5.0,5.1,5.2,5.3,5.4]}
df_3 = DataFrame(data_1, columns=['Year', 'State', 'Pop', 'unempl'])
print(df_3.Year) """

#Retriving a row by position
""" from pandas import Series,DataFrame
data_1={'State': ['va','va','va','md','md'],'Year':[2011,2012,2013,2014,2015],'Pop.':[5.0,5.1,5.2,5.3,5.4]}
df_3 = DataFrame(data_1, columns=['Year', 'State', 'Pop', 'unempl'])
print(df_3.iloc[0]) """

#Updating a column
""" from pandas import Series,DataFrame
import numpy as np
data_1={'State': ['va','va','va','md','md'],'Year':[2011,2012,2013,2014,2015],'Pop.':[5.0,5.1,5.2,5.3,5.4]}
df_3 = DataFrame(data_1, columns=['Year', 'State', 'Pop', 'unempl'])
df_3['unempl']=np.arange(5)
print(df_3) """

#Assigning a series to a column and assigning a new coloumn
""" from pandas import Series,DataFrame
import numpy as np
data_1={'State': ['va','va','va','md','md'],'Year':[2011,2012,2013,2014,2015],'Pop.':[5.0,5.1,5.2,5.3,5.4]}
df_3 = DataFrame(data_1, columns=['Year', 'State', 'Pop', 'unempl'])
unempl=Series([6.0, 6.0, 6.1], index=[2, 3, 4])
df_3['unempl']=unempl
df_3['state_dup']=df_3['State']
print(df_3) """

#Deleting a coloumn
""" from pandas import Series,DataFrame
import numpy as np
data_1={'State': ['va','va','va','md','md'],'Year':[2011,2012,2013,2014,2015],'Pop.':[5.0,5.1,5.2,5.3,5.4]}
df_3 = DataFrame(data_1, columns=['Year', 'State', 'Pop', 'unempl'])
unempl=Series([6.0, 6.0, 6.1], index=[2, 3, 4])
df_3['unempl']=unempl
df_3['state_dup']=df_3['State']
del df_3['state_dup']
print(df_3) """

#Create a dtaframe  from a nested list
""" from pandas import Series,DataFrame
import numpy as np
data_1={'State': ['va','va','va','md','md'],'Year':[2011,2012,2013,2014,2015],'Pop.':[5.0,5.1,5.2,5.3,5.4]}
df_3 = DataFrame(data_1, columns=['Year', 'State', 'Pop', 'unempl'])
unempl=Series([6.0, 6.0, 6.1], index=[2, 3, 4])
df_3['unempl']=unempl
df_3['state_dup']=df_3['State']
pop = {'VA' : {2013 : 5.1, 2014 : 5.2},
       'MD' : {2014 : 4.0, 2015 : 4.1}}
df_4 = DataFrame(pop)
print(df_4) """


#Creating a dataframe using the dictionarys
""" from pandas import Series,DataFrame
import numpy as np
data_1={'State': ['va','va','va','md','md'],'Year':[2011,2012,2013,2014,2015],'Pop.':[5.0,5.1,5.2,5.3,5.4]}
df_3 = DataFrame(data_1, columns=['Year', 'State', 'Pop', 'unempl'])
unempl=Series([6.0, 6.0, 6.1], index=[2, 3, 4])
df_3['unempl']=unempl
df_3['state_dup']=df_3['State']
pop = {'VA' : {2013 : 5.1, 2014 : 5.2},
       'MD' : {2014 : 4.0, 2015 : 4.1}}
df_4 = DataFrame(pop)
data_2 = {'VA' : df_4['VA'][1:],
          'MD' : df_4['MD'][2:]}
df_5 = DataFrame(data_2)
print(df_5) """

#Rendexing arow
from pandas import Series,DataFrame
import numpy as np
data_1={'State': ['va','va','va','md','md'],'Year':[2011,2012,2013,2014,2015],'Pop.':[5.0,5.1,5.2,5.3,5.4]}
df_3 = DataFrame(data_1, columns=['Year', 'State', 'Pop', 'unempl'])
unempl=Series([6.0, 6.0, 6.1], index=[2, 3, 4])
df_3['unempl']=unempl
df_3['state_dup']=df_3['State']
print(df_3.reindex(list(reversed(range(0, 6)))))

#Dropping Entries




