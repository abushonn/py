import data_preprocessing
import pandas as pd
import plotly.graph_objects as go
from plotly.offline import iplot


def visualize_tools(df, list):
    df_tool = pd.DataFrame(data={'cnt': list})
    df_tool = df_tool.replace(data_preprocessing.tool_keywords1_dict)
    df_tool_top50 = df_tool['cnt'].value_counts().reset_index().rename(columns={'index': 'tool'}).iloc[:50]

    num_postings = len(df)
    layout = dict(
        title='Tools For Data Scientists',
        yaxis=dict(
            title='% of job postings',
            tickformat=',.0%',
        )
    )
    fig = go.Figure(layout=layout)
    fig.add_trace(go.Bar(
        x=df_tool_top50['tool'],
        y=df_tool_top50['cnt'] / num_postings
    ))
    iplot(fig)

def visualize_skils(df, list):
    df_skills = pd.DataFrame(data={'cnt': list})
    df_skills = df_skills.replace(data_preprocessing.skill_keywords1_dict)
    df_skills_top50 = df_skills['cnt'].value_counts().reset_index().rename(columns={'index': 'skill'}).iloc[:50]

    num_postings = len(df)
    layout = dict(
        title='Skills For Data Scientists',
        yaxis=dict(
            title='% of job postings',
            tickformat=',.0%',
        )
    )

    fig = go.Figure(layout=layout)
    fig.add_trace(go.Bar(
        x=df_skills_top50['skill'],
        y=df_skills_top50['cnt'] / num_postings
    ))

    iplot(fig)

def visualize_education(df, list):
    df_degrees = pd.DataFrame(data={'cnt': list})
    df_degrees['degree_type'] = ''

    msk = df_degrees['cnt'] == 1
    df_degrees.loc[msk, 'degree_type'] = 'bachelors'

    msk = df_degrees['cnt'] == 2
    df_degrees.loc[msk, 'degree_type'] = 'masters'

    msk = df_degrees['cnt'] == 3
    df_degrees.loc[msk, 'degree_type'] = 'phd'

    msk = df_degrees['cnt'] == 4
    df_degrees.loc[msk, 'degree_type'] = 'postdoc'

    msk = df_degrees['cnt'] == 2.5
    df_degrees.loc[msk, 'degree_type'] = 'mba'

    msk = df_degrees['cnt'] > 500
    df_degrees.loc[msk, 'degree_type'] = 'not specified'

    df_degree_cnt = df_degrees['degree_type'].value_counts().reset_index().rename(columns={'index': 'degree'}).iloc[:50]

    num_postings = len(df)
    layout = dict(
        title='Minimum Education For Data Scientists',
        yaxis=dict(
            title='% of job postings',
            tickformat=',.0%',
        )
    )

    fig = go.Figure(layout=layout)
    fig.add_trace(go.Bar(
        x=df_degree_cnt['degree'],
        y=df_degree_cnt['degree_type'] / num_postings
    ))

    iplot(fig)