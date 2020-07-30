from kaleido.scopes.plotly import PlotlyScope
import plotly.graph_objects as go
scope = PlotlyScope()

fig = go.Figure(data=[go.Scatter(y=[1, 3, 2])])
with open("figure.png", "wb") as f:
    f.write(scope.transform(fig, format="png"))