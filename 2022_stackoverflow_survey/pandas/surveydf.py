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

surveydf_prep = surveydf_raw[relevant_columns].copy()


# perform type conversion for columns that should hold numeric values
    # If 'coerce', then invalid parsing will be set as NaN.

surveydf_prep['YearsCode'] = pd.to_numeric(surveydf_prep['YearsCode'], errors='coerce')
