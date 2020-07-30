import find_criteria
import load_data
import visualize
from plotly.offline import init_notebook_mode
import data_preprocessing
import pandas as pd

init_notebook_mode(connected=True)


df = load_data.load_data()

tool_list = []
skill_list = []
degree_list = []

(tool_list, skill_list, degree_list) = find_criteria.find_tools_skills_degrees(df)

# print('========= tool_list ============')
# print(tool_list)
# print('========= skill_list ============')
# print(skill_list)
# print('========= degree_list ============')
# print(degree_list)
#
# visualize.visualize_tools(df, tool_list)
# visualize.visualize_skils(df, skill_list)
# visualize.visualize_education(df, degree_list)

