""" import plotly.express as px
fig=px.line(x=[1,2,3],y=[1,2,3])
fig.show() """

#A bar chart using a plotly
""" import plotly.express as px
df=px.data.iris()
fig=px.bar(df,x="sepal_width",y="sepal_length")
fig.show() """

#An histogram
""" import plotly.express as px
df=px.data.iris()
fig=px.histogram(df,x="sepal_length",y="sepal_width")
fig.show() """

#Scatter plots and bubble charts
""" import plotly.express as px
df=px.data.iris()

fig=px.scatter(df,x="species",y="petal_width")
fig.show() """

#Adding the color in the scatter chart an example of an bubble plot
""" import plotly.express as px
df=px.data.iris()

fig=px.scatter(df,x="species",y="petal_width",color="species")
fig.show() """

#Making an pie chart in plotly
""" import plotly.express as px
df=px.data.tips()
fig=px.pie(df, values="total_bill" , names="day")
fig.show() """

#Heatmap
import plotly.graph_objects as go
import numpy as np
feature_x=np.arange(0,50,2)
feature_y=np.arange(0,50,3)

[X,Y] = np.meshgrid(feature_x, feature_y)
Z=np.cos(X/2) + np.sin(Y/4)

fig=go.Figure(data=go.Heatmap(x=feature_x,y=feature_y,z=Z))
fig.show()
