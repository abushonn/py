# https://plotly.com/python/getting-started/
# Plotly in Python

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import numpy as np

def fig01():
    fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
    fig.show()

def fig02():
    df = px.data.gapminder().query("country=='Canada'")
    fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
    print(df)
    fig.show()

def fig03():
    df = px.data.gapminder().query("continent=='Europe'")
    fig = px.line(df, x="year", y="lifeExp", color='country')
    fig.show()


def fig04():
    x = np.arange(10)

    fig = go.Figure(data=go.Scatter(x=x, y=x ** 2))
    fig.show()

np.random.seed(1)


def fig05():
    N = 20
    random_x = np.linspace(0, 1, N)
    random_y0 = np.random.randn(N) + 5
    random_y1 = np.random.randn(N)
    random_y2 = np.random.randn(N) - 5
    # Create traces
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=random_x, y=random_y0,
                             mode='lines',
                             name='lines'))
    fig.add_trace(go.Scatter(x=random_x, y=random_y1,
                             mode='lines+markers',
                             name='lines+markers'))
    fig.add_trace(go.Scatter(x=random_x, y=random_y2,
                             mode='markers', name='markers'))
    fig.show()


def fig06():
    # Add data
    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
             'August', 'September', 'October', 'November', 'December']
    high_2000 = [32.5, 37.6, 49.9, 53.0, 69.1, 75.4, 76.5, 76.6, 70.7, 60.6, 45.1, 29.3]
    low_2000 = [13.8, 22.3, 32.5, 37.2, 49.9, 56.1, 57.7, 58.3, 51.2, 42.8, 31.6, 15.9]
    high_2007 = [36.5, 26.6, 43.6, 52.3, 71.5, 81.4, 80.5, 82.2, 76.0, 67.3, 46.1, 35.0]
    low_2007 = [23.6, 14.0, 27.0, 36.8, 47.6, 57.7, 58.9, 61.2, 53.3, 48.5, 31.0, 23.6]
    high_2014 = [28.8, 28.5, 37.0, 56.8, 69.7, 79.7, 78.5, 77.8, 74.1, 62.6, 45.3, 39.9]
    low_2014 = [12.7, 14.3, 18.6, 35.5, 49.9, 58.0, 60.0, 58.6, 51.7, 45.2, 32.2, 29.1]

    zipped_2000=[(g + h) / 2 for g, h in zip(high_2000, low_2000)]
    zipped_2007=[(g + h) / 2 for g, h in zip(high_2007, low_2007)]
    zipped_2014=[(g + h) / 2 for g, h in zip(high_2014, low_2014)]

    fig = go.Figure()
    # Create and style traces
    # fig.add_trace(go.Scatter(x=month, y=high_2014, name='High 2014',
    #                          line=dict(color='firebrick', width=4)))
    # fig.add_trace(go.Scatter(x=month, y=low_2014, name='Low 2014',
    #                          line=dict(color='royalblue', width=4)))
    # fig.add_trace(go.Scatter(x=month, y=high_2007, name='High 2007',
    #                          line=dict(color='firebrick', width=4,
    #                                    dash='dash')  # dash options include 'dash', 'dot', and 'dashdot'
    #                          ))
    # fig.add_trace(go.Scatter(x=month, y=low_2007, name='Low 2007',
    #                          line=dict(color='royalblue', width=4, dash='dash')))
    # fig.add_trace(go.Scatter(x=month, y=high_2000, name='High 2000',
    #                          line=dict(color='firebrick', width=4, dash='dot')))
    # fig.add_trace(go.Scatter(x=month, y=low_2000, name='Low 2000',
    #                          line=dict(color='royalblue', width=4, dash='dot')))

    fig.add_trace(go.Scatter(x=month, y=zipped_2000, name='2014', line=dict(color='firebrick', width=4)))
    fig.add_trace(go.Scatter(x=month, y=zipped_2007, name='2007',line=dict(color='firebrick', width=4, dash='dash')))
    fig.add_trace(go.Scatter(x=month, y=zipped_2014, name='2000',line=dict(color='firebrick', width=4, dash='dot')))

    # Edit the layout
    fig.update_layout(title='Average High and Low Temperatures in New York',
                      xaxis_title='Month',
                      yaxis_title='Temperature (degrees F)')
    fig.show()


def fig07():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    y1 = [10, 20, None, 15, 10, 5, 15, None, 20, 10, 10, 15, 25, 20, 10]
    y2 = [5, 15, None, 10, 5, 0, 10, None, 15, 5, 5, 10, 20, 15, 5]

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x,
        y=y1,
        name='<b>No</b> Gaps',  # Style name/legend entry with html tags
        connectgaps=True  # override default to connect the gaps
    ))
    fig.add_trace(go.Scatter(
        x=x,
        y=y2,
        name='Gaps',
    ))
    fig.show()


def fig08():
    title = 'Main Source for News'
    labels = ['Television', 'Newspaper', 'Internet', 'Radio']
    colors = ['rgb(67,67,67)', 'rgb(115,115,115)', 'rgb(49,130,189)', 'rgb(189,189,189)']
    mode_size = [8, 8, 12, 8]
    line_size = [2, 2, 4, 2]
    x_data = np.vstack((np.arange(2001, 2014),) * 4)
    y_data = np.array([
        [74, 82, 80, 74, 73, 72, 74, 70, 70, 66, 66, 69],
        [45, 42, 50, 46, 36, 36, 34, 35, 32, 31, 31, 28],
        [13, 14, 20, 24, 20, 24, 24, 40, 35, 41, 43, 50],
        [18, 21, 18, 21, 16, 14, 13, 18, 17, 16, 19, 23],
    ])
    fig = go.Figure()
    for i in range(0, 4):
        fig.add_trace(go.Scatter(x=x_data[i], y=y_data[i], mode='lines',
                                 name=labels[i],
                                 line=dict(color=colors[i], width=line_size[i]),
                                 connectgaps=True,
                                 ))

        # endpoints
        fig.add_trace(go.Scatter(
            x=[x_data[i][0], x_data[i][-1]],
            y=[y_data[i][0], y_data[i][-1]],
            mode='markers',
            marker=dict(color=colors[i], size=mode_size[i])
        ))

    annotations = []

    # Adding labels
    for y_trace, label, color in zip(y_data, labels, colors):
        # labeling the left_side of the plot
        annotations.append(dict(xref='paper', x=0.05, y=y_trace[0],
                                xanchor='right', yanchor='middle',
                                text=label + ' {}%'.format(y_trace[0]),
                                font=dict(family='Arial',
                                          size=16),
                                showarrow=False))
        # labeling the right_side of the plot
        annotations.append(dict(xref='paper', x=0.95, y=y_trace[11],
                                xanchor='left', yanchor='middle',
                                text='{}%'.format(y_trace[11]),
                                font=dict(family='Arial',
                                          size=16),
                                showarrow=False))

    # Title
    annotations.append(dict(xref='paper', yref='paper', x=0.0, y=1.05,
                            xanchor='left', yanchor='bottom',
                            text='Main Source for News',
                            font=dict(family='Arial',
                                      size=30,
                                      color='rgb(37,37,37)'),
                            showarrow=False))
    # Source
    annotations.append(dict(xref='paper', yref='paper', x=0.5, y=-0.1,
                            xanchor='center', yanchor='top',
                            text='Source: PewResearch Center & ' +
                                 'Storytelling with data',
                            font=dict(family='Arial',
                                      size=12,
                                      color='rgb(150,150,150)'),
                            showarrow=False))

    fig.update_layout(annotations=annotations)
    fig.show()


fig08()
