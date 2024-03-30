# Pandas is a software library written for the Python programming language for data manipulation and analysis.
import pandas as pd
#NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays
import numpy as np
df=pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_1.csv")
df.head(10)

landing_outcomes = {
    'Failure (drone ship)': 0,
    'Success (drone ship)': 0,
    'Success (ground pad)': 0,
    'Failure (parachute)': 0,
    'None': 0
}

# Assuming 'df' is your DataFrame containing the data
landing_outcomes = df['Outcome'].value_counts()

# Print the number and occurrence of each mission outcome
for i, outcome in enumerate(landing_outcomes.keys()):
    print(i, outcome)