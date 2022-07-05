# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 15:46:17 2022

@author: chery
"""

import pandas as pd 


# file_name = pd.read_csv('file.csv') <-- format of read_csv
data = pd.read_csv('transaction.csv')
data = pd.read_csv('transaction.csv', sep=';')

#summary of the data
data.info()

#working with calculation
   
#defining vaiables
CostperItem = 11.73
SellingPriceItem = 21.11
NumberofItemsPurchased = 6

#mathematical Operation on tableau
ProfitPerItem =21.11 - 11.73
ProfitPerItem = SellingPriceItem  - CostperItem

ProfitPerTransaction = NumberofItemsPurchased * ProfitPerItem
CostPerTransaction = NumberofItemsPurchased * CostperItem
SellingPriceTransaction = NumberofItemsPurchased * SellingPriceItem

#CostPerTransaction column calculation

#CostPerTransaction = NumberofItemsPurchased * CostperItem
# Variable = dataframe['column_name']
CostperItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = NumberofItemsPurchased * CostperItem

#adding new column to a dataframs
data['CostPerTransaction'] =  data['CostPerItem'] * data['NumberOfItemsPurchased']

#sales per transaction
data['SalesPerTransaction'] =  data['SellingPricePerItem'] * data['NumberOfItemsPurchased']

#profit calculation = Sales - cost 
data['ProfitPerTransaction'] =  data['SalesPerTransaction'] - data['CostPerTransaction']

#markup = (Sales - Cost)/Cost
data['Markup'] =  ( data['SalesPerTransaction'] - data['CostPerTransaction'] ) / data['CostPerTransaction']
data['Markup'] =  ( data['ProfitPerTransaction'] ) / data['CostPerTransaction']

#rounding marking 
data['Markup']  = round(data['Markup'], 2)

#checking column data type
print(data['Day'].dtype)


#change column type
day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(day.dtype) 
print(year.dtype) 

my_date = day+'_' + data['Month']+'_'+year

data['date'] =  my_date

#using iloc to view specific column/rows
data.iloc[0] #view the row with index 0
data.iloc[0:3] #first 3 rows
data.iloc[-5] #last 5 rows

data.head(5) #brings in first 5 rows

data.iloc[:,2] #brings in all rows on the 2nd column
data.iloc[4,2] ##brings in 4th row, 2nd column


# using split to split the client keyword field
# new_var = column.str.split('sep', expand = true)

split_col = data['ClientKeywords'].str.split(',', expand = True)


#creating new columns for solits column in client keywords

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthofContract'] = split_col[2]

#using replace function 

data['ClientAge'] = data['ClientAge'].str.replace('[', '')
data['LengthofContract'] = data['LengthofContract'].str.replace(']', '')


#using the lower function to change item to lowercase
data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files
 
#bringing in a new dataset
seasons = pd.read_csv('value_inc_seasons.csv', sep=';')

#merging files : merge_df = pd.merge(df_old, df_new, on = 'key')
data = pd.merge(data, seasons, on = 'Month')


#dropping columns
# df = df.drop('columname', axis = 1)

data = data.drop('ClientKeywords', axis = 1)
data = data.drop('Day', axis = 1)
data = data.drop(['Year', 'Month'], axis = 1)




#export in CSV

data.to_csv('ValueInc_Cleaned.csv', index = False)































