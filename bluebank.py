#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 18:07:42 2022

@author: rabiahlewis
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Method 1 for Reading Json Data

json_file = open('loan_data_json.json')
data = json.load(json_file)

# Method 2 for Reading Json Data

with open('loan_data_json.json') as json_file:
    data = json.load(json_file)

# Transform from List to Dataframe
loandata = pd.DataFrame(data)

# To Find Unique Values in Column
loandata['purpose'].unique()

# Describe the Data
loandata.describe()

# Describe the Data for Specific Column
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

# Using Exp Function to Calculate Annual Income
income = np.exp(loandata['log.annual.inc'])
loandata['annualincome'] = income

# Working w/ IF Statements

a = 40
b = 500

if b > a:
    print('b is greater than a')

# With Additional Conditions

a = 40
b = 500
c = 1000

if b > a and b < c:
    print('b is greater than a but less than c')

# When a Condition is not Met

a = 40
b = 500
c = 20

if b > a and b < c:
    print('b is greater than a but less than c')
else:
    print('Conditions Not Met')

# Conditions w/ Different Metrics

a = 40
b = 500
c = 30

if b > a and b < c:
    print('b is greater than a but less than c')
elif b > a and b > c:
    print('b is greater than a and c')
else:
    print('Conditions Not Met')

# Using OR

a = 40
b = 500
c = 30

if b > a or b < c:
    print('b is greater than a or less than c')
elif b > a and b > c:
    print('b is greater than a and c')
else:
    print('Conditions Not Met')

# FICO Score

fico = 350

if fico >= 300 and fico < 400:
    ficocat = 'Very Poor'
elif fico >= 400 and fico < 600:
    ficocat = 'Poor'
elif fico >= 600 and fico < 660:
    ficocat = 'Fair'
elif fico >= 660 and fico < 780:
    ficocat = 'Good'
elif fico >= 780:
    ficocat = 'Excellent'
else:
    ficocat = 'Unknown'
print(ficocat)

# For Loops based on Values

fruits = ['apple', 'pear', 'banana', 'cherry']
for x in fruits:
    print(x)
    y = x + ' fruit'
    print(y)

# Loops based on Position

for x in range(0,4):   # "4" does not print, stops at preceding digit. Makes sense as Index starts at "0"
    y = fruits[x] + ' for sale'
    print(y)

# Applying For Loops to Loan Data

# First 10 Values
length = len(loandata)
ficocat = []
for x in range(0,length):
    category = loandata['fico'][x]
    
    try:
        if category >= 300 and category < 400:
            cat = 'Very Poor'
        elif category >= 401 and category < 600:
            cat = 'Poor'
        elif category >= 601 and category < 660:
            cat = 'Fair'
        elif category >= 661 and category < 780:
            cat = 'Good'
        elif category >= 781:
            cat = 'Excellent'
        else:
            cat = 'Unknown'
    except:
        cat = 'Error'
        
        
    ficocat.append(cat)

ficocat = pd.Series(ficocat)

loandata['fico.category'] = ficocat

# More Conditional Statements: df.loc
# df.loc[df[columnname] condition, newcolumnname] = 'value if condition is met'
# for interest rates, a new column is wanted. rate . 0.12 then high, else low

loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] < 0.12, 'int.rate.type'] = 'Low'


# Number of Loans/Rows by fico.category

catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color = 'green', width = 0.1)
plt.show()

purposecount = loandata.groupby(['purpose']).size()
purposecount.plot.bar(color = 'orange', width = 0.5)
plt.show()

# Scatter Plots (Correlations Between Columns/Categories)

ypoint = loandata['annualincome']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint)
plt.show()

# Writing to CSV
loandata.to_csv('loan_cleaned.csv', index = True)




































































