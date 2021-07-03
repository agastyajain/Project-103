import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
fig = px.scatter(df,x='Country',y='Per capita',size='Percentage',color="Country",size_max=60)
#fig = px.line(df,x='Country',y='Per capita')
#fig = px.bar(df,x='Country',y='Per capita')
fig.show()