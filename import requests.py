import requests
import pandas as pd
import numpy as np
import datetimestatic_json_url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/API_call_spacex_api.json'
response.status_code
json_data = response.json()
df = pd.json_normalize(json_data)
print(df)

Lab1_data= pd.DataFrame(df)

# Save the DataFrame to an Excel file
Lab1_data.to_excel('output.xlsx', index=False)