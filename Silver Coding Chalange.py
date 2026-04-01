# Importing required library
import pandas as pd
import numpy as np
import json
import os
filename = "loans.json"
with open(filename) as f:
    data = json.load(f)
    df = pd.DataFrame(data)

# For calcuating sum, mean, median, min, max
def for_calculation(df):
  needed_columns = {'LoanAmountSummary':{},'SubjectAppraisedAmountSummary':{},'InterestRateSummary':{}}
  for colns in ['LoanAmount','SubjectAppraisedAmount','InterestRate']:
    columns = colns+ 'Summary' 
    needed_columns[columns]['Sum'] = np.sum(df[colns])
    needed_columns[columns]['Average'] = np.mean(df[colns])
    needed_columns[columns]['Median'] = np.median(df[colns])
    needed_columns[columns] ['Minimum'] = np.min(df[colns])
    needed_columns[columns]['Maximum'] = np.max(df[colns])
  return needed_columns
# Task 1:
monthlySummary = for_calculation(df)
with open('monthlySummary.json','w') as output:
  json.dump(monthlySummary, output)

# Task 2:
gb_SubjectState = df.groupby(["SubjectState"])
monthlyByState = dict.fromkeys(gb_SubjectState.groups.keys())
for states in monthlyByState:
  temp = gb_SubjectState.get_group(states).reset_index(drop = True)
  final_output = for_calculation (temp)
  monthlyByState[states]= final_output
with open ("monthlyByState.json","w") as output:
  json.dump(monthlyByState, output)