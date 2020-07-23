from collections import Counter
import nltk
import string
from nltk.tokenize import word_tokenize
import pandas as pd
import data_preprocessing
import word_setting


def find_tools_skills_degrees(df):
    tool_list = []
    skill_list = []
    degree_list = []
    num_postings = len(df)
    for i in range(num_postings):
        try:
            job_desc = df.iloc[i]['job_description'].lower()
            job_desc_set = data_preprocessing.prepare_job_desc(job_desc)
            # print(job_desc_set)
            # print(str(i) + '  ===========================================')

            # check if the keywords are in the job description. Look for exact match by token.
            tool_words = data_preprocessing.tool_keywords1_set.intersection(job_desc_set)
            skill_words = data_preprocessing.skill_keywords1_set.intersection(job_desc_set)
            degree_words = data_preprocessing.degree_keywords1_set.intersection(job_desc_set)

            # check if longer keywords (more than one word) are in the job description. Match by substring.
            j = 0
            for tool_keyword2 in word_setting.tool_keywords2:
                # tool keywords.
                if tool_keyword2 in job_desc:
                    tool_list.append(tool_keyword2)
                    j += 1

            k = 0
            for skill_keyword2 in word_setting.skill_keywords2:
                # skill keywords.
                if skill_keyword2 in job_desc:
                    skill_list.append(skill_keyword2)
                    k += 1

            # search for the minimum education.
            min_education_level = 999
            for degree_word in degree_words:
                level = word_setting.degree_dict[data_preprocessing.degree_keywords1_dict[degree_word]]
                min_education_level = min(min_education_level, level)

            for degree_keyword2 in word_setting.degree_keywords2:
                # longer keywords. Match by substring.
                if degree_keyword2 in job_desc:
                    level = word_setting.degree_dict2[degree_keyword2]
                    min_education_level = min(min_education_level, level)

            # label the job descriptions without any tool keywords.
            if len(tool_words) == 0 and j == 0:
                tool_list.append('nothing specified')

            # label the job descriptions without any skill keywords.
            if len(skill_words) == 0 and k == 0:
                skill_list.append('nothing specified')

            # If none of the keywords were found, but the word degree is present, then assume it's a bachelors level.
            if min_education_level > 500:
                if 'degree' in job_desc:
                    min_education_level = 1

            tool_list += list(tool_words)
            skill_list += list(skill_words)
            degree_list.append(min_education_level)
        except UnicodeEncodeError:
            print('UnicodeEncodeError')
            continue
    return (tool_list, skill_list, degree_list)



