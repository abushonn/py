import pandas as pd
import data_preprocessing
import pandas as pd
from plotly.offline import init_notebook_mode

#init_notebook_mode(connected=True)


def load_data():
    # pd.set_option('display.max_columns', None)
    # load in the data.
    df_list = []
    # cities = ['boston', 'chicago', 'la', 'montreal', 'ny', 'sf', 'toronto', 'vancouver']
    cities = ['toronto', 'vancouver']
    # cities = ['toronto']
    for city in cities:
        df_tmp = pd.read_pickle('data_scientist_{}.pkl'.format(city))
        df_tmp['city'] = city

        res = data_preprocessing.prepare_job_desc(df_tmp['job_description'].iloc[0])

        # print(res)

        df_list.append(df_tmp)
    df = pd.concat(df_list).reset_index(drop=True)
    # print(df)
    # If it's the same job description in the same city, for the same job title, we consider it duplicate.
    df = df.drop_duplicates(subset=['job_description', 'city', 'job_title'])

    return df

