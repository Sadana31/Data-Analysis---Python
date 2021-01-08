import pandas as pd
import csv
import plotly.express as px

df = pd.read_csv("data.csv")

mean = df.groupby(["studentID", "Level"], as_index=False)["Attempt"].mean()

fig = px.scatter(mean, x="studentID", y="Level", size="Attempt", color="Attempt")
fig.show()