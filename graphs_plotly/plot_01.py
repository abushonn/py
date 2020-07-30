
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

def fig01():
    fig = go.Figure()
    fig.add_trace(go.Bar(x=[1, 2, 3], y=[1, 3, 2]))
    fig.show()

def fig02():
    fig = make_subplots(rows=1, cols=2)

    fig.add_trace(go.Scatter(y=[4, 2, 1], mode="lines"), row=1, col=1)
    fig.add_trace(go.Bar(y=[2, 1, 3]), row=1, col=2)
    fig.show()

def fig03():
    df = px.data.iris()
    # print(len(px.data.iris()))
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", title="A Plotly Express Figure")
    fig.show()
