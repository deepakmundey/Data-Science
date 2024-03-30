# Pandas is a software library written for the Python programming language for data manipulation and analysis.
import pandas as pd
#NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays
import numpy as np
df=pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_1.csv")
df.head(10)
df.dtypes
# Apply value_counts() on column LaunchSite
# Assuming 'df' is your DataFrame containing the data
orbit_counts = df['Orbit'].value_counts()

# Now, you can check the count of 'GTO' orbit
gto_count = orbit_counts['GTO']

print("The value for Orbit with the column name GTO is:", gto_count)