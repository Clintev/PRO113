import pandas as pd
import plotly.express as px

reader = pd.read_csv("Copy+of+data+-+data.csv")

scatter_read = px.scatter(reader, x = "date", y = "cases", color="country")
scatter_read.show()




#date,cases,country