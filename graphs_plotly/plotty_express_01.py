# https://h1ros.github.io/posts/visualization-samples-by-plotly-express/
# Visualization Samples by Plotly Express
import plotly_express as px
import plotly.io as pio
pio.renderers.default = "browser"

df = px.data.gapminder()
# fig = px.scatter(df, x='gdpPercap', y='lifeExp', width=900, height=400)
# fig.show()

fig = px.scatter(df, x='gdpPercap', y='lifeExp', size='pop', color='country', animation_frame='year', width=900, height=400)
fig.show()