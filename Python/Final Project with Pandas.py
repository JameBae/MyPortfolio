# -*- coding: utf-8 -*-

# -- Project --

# # Final Project - Analyzing Sales Data
# 
# **Date**: 26 June 2023
# 
# **Author**: Pisitpon Techathammawat (Jame)
# 
# **Course**: `Pandas Foundation`


# import data
import pandas as pd
df = pd.read_csv("sample-store.csv")

# preview top 5 rows
df.head(5)

# shape of dataframe
df.shape

# see data frame information using .info()
df.info()

# We can use `pd.to_datetime()` function to convert columns 'Order Date' and 'Ship Date' to datetime.


# example of pd.to_datetime() function
pd.to_datetime(df['Order Date'].head(), format='%m/%d/%Y')

# TODO - convert order date and ship date to datetime in the original dataframe
df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%Y')
df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True)
df.head()

# TODO - count nan in postal code column
df['Postal Code'].isna().sum()

# TODO - filter rows with missing values
df[df['Postal Code'].isna()]

# TODO - Explore this dataset on your owns, ask your own questions
# What city make highest profit ?
df.groupby('City')['Profit'].sum().sort_values(ascending=False)

# ## Data Analysis Part
# 
# Answer 10 below questions to get credit from this course. Write `pandas` code to find answers.


# TODO 01 - how many columns, rows in this dataset
df.shape

# TODO 02 - is there any missing values?, if there is, which colunm? how many nan values?
df.isna().sum()

# TODO 03 - your friend ask for `California` data, filter it and export csv for him
california = df[df['State'] == 'California']
california.to_csv('california.csv')

# TODO 04 - your friend ask for all order data in `California` and `Texas` in 2017 (look at Order Date), send him csv file
df_2017 = df[df['Order Date'].dt.year == 2017]
cali_tex_2017 = df_2017.query("State == 'California' | State == 'Texas'")
cali_tex_2017.to_csv('cali_tex_2017.csv')

# TODO 05 - how much total sales, average sales, and standard deviation of sales your company make in 2017
# Result 1
df_2017.agg({'Sales' : ['sum','mean','std']})

#--------------------------------------
# Result 2
#import numpy as np
#total_sales = np.sum(df_2017['Sales'])
#avg_sales = np.average(df_2017['Sales'])
#std_sales = np.std(df_2017['Sales'])
#print(f"Total Sales : {total_sales} \nAverage Sales : {avg_sales} \nStandard Deviation of Sales : {std_sales}")

# TODO 06 - which Segment has the highest profit in 2018
df_2018 = df[df['Order Date'].dt.year == 2018]
df_2018.groupby('Segment')['Profit'].sum()

# TODO 07 - which top 5 States have the least total sales between 15 April 2019 - 31 December 2019
betw_apr_dec = df[(df['Order Date'] >= '2019-04-15') & (df['Order Date'] <= '2019-12-31')]
betw_apr_dec.groupby('State')['Sales'].sum().sort_values(ascending=False).tail(5)

# TODO 08 - what is the proportion of total sales (%) in West + Central in 2019 e.g. 25% 
df_2019 = df[df['Order Date'].dt.year == 2019]
region_2019 = df_2019.groupby('Region')['Sales'].sum().reset_index()

wc_filter = region_2019[(region_2019['Region'] == 'West') | (region_2019['Region'] == 'Central')]['Sales'].sum()
proportion = (wc_filter / region_2019['Sales'].sum()*100).round(2)
print(f"Proportion of Total Sales(%) in West and Central in 2019 : {proportion}")

# TODO 09 - find top 10 popular products in terms of number of orders vs. total sales during 2019-2020
# Quantities 2019 - 2020 by Product
df_20192020 = df[(df['Order Date'].dt.year == 2019) | (df['Order Date'].dt.year == 2020)]
quan = df_20192020.groupby('Product Name')['Quantity'].sum().sort_values(ascending= False).reset_index().head(10)
quan

# Sales 2019 - 2020 by Product
sales = df_20192020.groupby('Product Name')['Sales'].sum().round(2).sort_values(ascending = False).reset_index().head(10)
sales

# TODO 10 - plot at least 2 plots, any plot you think interesting :)
import seaborn as sns
import matplotlib.pyplot as plt
plt_segments = df.groupby('Segment')['Profit'].sum().reset_index()
sns.catplot(data = plt_segments, x = 'Segment', y = 'Profit', kind = 'bar').set(title = 'Sales Seperate By Segment')
plt.show()

sns.lmplot(x = 'Sales', y = 'Profit', hue = 'Region', data = df).set(title = 'Relationship Between Sales and Profit Seperate By Region ')
plt.show()

# TODO Bonus - use np.where() to create new column in dataframe to help you answer your own questions
import numpy as np
df['Net Profit'] = np.where(df['Profit'] > 0, 'Profit', 'Loss')
df['Net Profit'].value_counts().plot(kind = 'pie', legend=False, autopct='%.f%%', title = 'Overall Net Profit (%)');



