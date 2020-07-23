# How to use NLP in Python: a Practical Step-by-Step Example

A step-by-step NLP application on Indeed job postings in `https://il.indeed.com/?r=us` site.

see: https://towardsdatascience.com/how-to-use-nlp-in-python-a-practical-step-by-step-example-bd82ca2d2e1e

##Preparation: Scraping the Data

##Step #1: Loading and Cleaning the Data
- web_scraping_indeed.py

##Step #2: Forming the Lists of Keywords
- word_setting.py

##Step #3: Streamlining the Job Descriptions using NLP Techniques
Tokenizing the Job Descriptions.

Parts of Speech (POS) Tagging the Job Descriptions

- pos_tag_example.py
- find_criteria.py

##Step #4: Final Processing of the Keywords and the Job Descriptions
Stemming the Words

- data_preprocessing.py

##Step #5: Matching the Keywords and the Job Descriptions
To see if a job description mentions specific keywords, 
we match the lists of keywords and the final streamlined job descriptions.
Three sets: Tools/Skills/Educations

- find_criteria.py

##Step #6: Visualizing the Results
We summarize the results with bar charts. For each particular keyword of tools/skills/education levels, 
we count the number of job descriptions that match them. 
We calculate their percentage among all the job descriptions as well.
We are only presenting the top 50 most popular ones.


