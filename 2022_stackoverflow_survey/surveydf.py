import pandas as pd
from path import survey_path

# raw copy of the survey
surveydf_raw = pd.read_csv(survey_path)

# filter out the columns that should be included in the analysis
relevant_columns = [
    'Employment', 'DevType', 'RemoteWork', # employment
    'Country', 'Age', 'Gender', 'EdLevel', # demographics
    'YearsCode', 'LanguageHaveWorkedWith', 'DatabaseHaveWorkedWith' # programming
]

surveydf_prep = surveydf_raw[relevant_columns]
