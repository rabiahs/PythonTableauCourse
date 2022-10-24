#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 10:03:33 2022

@author: rabiahlewis
"""

import pandas as pd

# file_name = pd.read_csv('file.csv') <--- format of read_csv

data = pd.read_csv('transaction.csv')

data = pd.read_csv('transaction.csv', sep=';')

# Summary of data
# data.info()

# Working w/ calculations

# Defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberofItemsPurchased = 6

# Mathematical Operations on Tableau

ProfitPerItem = 21.11 - 11.73
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberofItemsPurchased * ProfitPerItem
CostPerTransaction = NumberofItemsPurchased * CostPerItem
SalesPerTransaction = NumberofItemsPurchased * SellingPricePerItem

# CostPerTransaction Column Calculation

# CostPerTransaction = CostPerItem * NumberofItemsPurchased
# variable = dataframe['column_name']

CostPerItem = data['CostPerItem']
NumberofItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberofItemsPurchased

# Adding New Column to Dataframe

# Cost Per Transaction Calculation

data['CostPerTransaction'] = data['CostPerItem'] * data['NumberOfItemsPurchased']

# Sales Per Transaction Calculation

data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

# Profit Calculation = Sales - Cost

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

# Markup Calculation = (Sales - Cost)/Cost

# (data['SalesPerTransaction'] - data['CostPerTransaction']) / data['CostPerTransaction']
# Same result with below:
#      data['Markup'] = (data['ProfitPerTransaction']) / data['CostPerTransaction']

data['Markup'] = (data['SalesPerTransaction'] - data['CostPerTransaction']) / data['CostPerTransaction']

# Round Function

roundMarkup = round(data['Markup'],2)

data['Markup'] = round(data['Markup'],2)

# Combining Data Fields

my_name = 'Rabiah' + 'Lewis'

my_date = 'Day'+'-'+'Month'+'-'+'Year'

# Checking Column Data Type

print(data['Day'].dtype)

# Change Column Data Type

day = data['Day'].astype(str)
year = data['Year'].astype(str)
print (day.dtype)
print (year.dtype)

my_date = day+'-'+ data['Month']+'-'+year

data['Date'] = my_date

# Using iloc to View Specific Column/Row

data.iloc[0] # Views the row with index = 0
data.iloc[0:3]  # First 3 rows
data.iloc[-5:]  # Last 5 rows

data.head(5)  # First 5 rows

data.iloc[:,2]  # All rows from 2nd column

data.iloc[4,2]  # 4th row, 2nd column

# Using Split to split the Client Keywords Field
# new_var = column.str.split('sep', expand = True)

split_col = data['ClientKeywords'].str.split(',' , expand = True)

# data['ClientKeywords'].str.split(',' , expand = True)

# Creating New Columns for Split Columns

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]

# Using the Replace Function
# Replaces a specif phrase w/ another specific phrase. For example:
# data['ClientAge'] = data['ClientAge'].str.replace('[','')

data['ClientAge'] = data['ClientAge'].str.replace('[','')
data['LengthofContract'] = data['LengthofContract'].str.replace(']','')

# Using the Lower Function to Change Item to Lowercase

data [ 'ItemDescription' ] = data['ItemDescription'].str.lower()

# -------------------   Merging Files  ----------------------

# 1. Introduce New Dataset

# file_name = pd.read_csv('file.csv' , sep = ';') <--- format of read_csv

seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

# Merge Statement
# merge_df = pd.merge (df_old, df_new, on = 'key')

data = pd.merge (data, seasons, on = 'Month')

# -----------------------------------------------------------

# Deleting Columns w/ Drop Function
# Statement: df = df.drop('columnname' , axis = 1)
# Statement for 2+ column drop: df = df.drop (['ColName1', 'ColName2'], axis = 1)

data = data.drop ('ClientKeywords', axis = 1)
data = data.drop ('Day', axis = 1)
data = data.drop (['Year', 'Month'], axis = 1)

# Export into CSV

data.to_csv('ValueInc_Cleaned.csv' , index = False) # <---- Excludes Index Column from Export




























