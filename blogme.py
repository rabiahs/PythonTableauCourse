#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 17:05:02 2022

@author: rabiahlewis
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Reading Excel or .XLSX files
data = pd.read_excel('articles.xlsx')

# Data Summary
data.describe()

# Column Summary
data.info()

# Counting the Number of Articles per Source
# Groupby format: df.groupby(['column_to_group'])['column_to_count'].count()

data.groupby(['source_id'])['article_id'].count()

# Number of Reactions by Publisher
data.groupby(['source_id'])['engagement_reaction_count'].sum()

# Dropping a Column
data = data.drop('engagement_comment_plugin_count' , axis = 1)

# Functions in Python

def thisFunction():
    print('1st FUNCTION!!')
    
thisFunction()

# Functions w/ Variables

def aboutMe(name, surname, location):
    print('This is '+name+' My surname is '+surname+' I am from '+location)
    return name, surname, location
    
a = aboutMe('Rabiah','Lewis','United States')

# Using For Loops in Functions

def favfood(food):
    for x in food:
        print('Top food is ' + x)

fastfood = ['burgers', 'pizza', 'pie']

favfood(fastfood)

# Creating a Keyword Flag

keyword = 'crash'

# Isolate Each Title Using For Loop

# length = len(data)
# keyword_flag = []
# for x in range (0,length):
#     heading = data['title'][x]
#     if keyword in heading:
#         flag = 1
#     else:
#         flag = 0
#     keyword_flag.append(flag)

# Creating a Function

def keywordflag(keyword):
    length = len(data)
    keyword_flag = []
    for x in range (0,length):
        heading = data['title'][x]
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        keyword_flag.append(flag)
    return keyword_flag

keywordflag = keywordflag('murder')

# Creating a New Column

data['keyword_flag'] = pd.Series(keywordflag)

# SentimentIntensityAnalyzer

sent_int = SentimentIntensityAnalyzer()

text = data['title'][16]
sent = sent_int.polarity_scores(text)

# Extracting Sentiment into Fields

neg = sent['neg']
pos = sent['pos']
neu = sent['neu']

# Using a For Loop to Extract Sentiment

title_neg_sentiment = []
title_pos_sentiment = []
title_neu_sentiment = []

length = len(data)

for x in range (0,length):
    try:
        text = data['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg = 0
        pos = 0
        neu = 0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)

title_neg_sentiment = pd.Series(title_neg_sentiment)
title_pos_sentiment = pd.Series(title_pos_sentiment)
title_neu_sentiment = pd.Series(title_neu_sentiment)

data['title_neg_sentiment'] = title_neg_sentiment
data['title_pos_sentiment'] = title_pos_sentiment
data['title_neu_sentiment'] = title_neu_sentiment

# Writing to Excel

data.to_excel('blogme_clean.xlsx', sheet_name='blogmedata', index = False)










































