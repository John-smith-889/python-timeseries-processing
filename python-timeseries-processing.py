
"""
The file contains methods' applications useful for timeseries processing.
"""

#=============================================================================#
# Operations using dates #
#========================#

#==================#
# datetime objects #
#==================#

import datetime

# Create datetime object from integers
datetime_obj = datetime.datetime(2019, 4, 13)
datetime_obj

# Create datetime object from string
datetime_str = '18/09/93'
datetime_obj_02 = datetime.datetime.strptime(datetime_str, '%d/%m/%y')

# Get current time 
datetime.datetime.now()


#==========================#
# DatetimeIndex generation #
#==========================#

import pandas as pd
dti_01 = pd.date_range('2020-01-01', periods=4, freq='D') 


#======================#
# Generate random data #
#======================#

import pandas as pd

rows_01 = 4

dict_01 = {'A': [1, 2, 3, 4],
           'B': [2, 4, 6, 8], 
           'C': [10, 20, 30, 40]}

# Create DateTimeIndex
dti_01 = pd.date_range('2020-01-01', periods=rows_01, freq='D') 

# freq='MS'set the frequency in months 
df_01 = pd.DataFrame(dict_01, index=dti_01) # index arg is optional
df_01


#=============================#
# Select rows between 2 dates # use strings
#=============================#
# (closed interval)

df_01
df_01.loc['2020-01-01' : '2020-01-02'] 


#=============================#
# Select rows between 2 dates # use datatime objects
#=============================#
# (closed interval)

import datetime

# Create datetime object from string
start_date_datatime = datetime.datetime.strptime('2020-01-01','%Y-%m-%d')
end_date_datatime = datetime.datetime.strptime('2020-01-02','%Y-%m-%d')

# select rows with 
df_01.loc[start_date_datatime : end_date_datatime] # (closed interval)


#==================#
# Dates comparison #
#==================#

import datetime
datetime_obj = datetime.datetime.strptime('18/09/94', '%d/%m/%y')
datetime_obj2 = datetime.datetime.strptime('18/09/93', '%d/%m/%y')

# Compare dates
datetime_obj > datetime_obj2


#============================================#
# Assign value to certain series index value #
#============================================#

import pandas as pd
list_01 = [1, 2, 3, 4]
dti_01 = pd.date_range('2020-01-01', periods=4, freq='D') 
series_01 = pd.Series(list_01, index=dti_01) # index arg is optional

series_01.loc['2020-01-03'] = 10


#=============================================================================#
# Operations across rows #
#========================#

import pandas as pd
dict_01 = {'A': [1, 2, 3, 4],
           'B': [2, 4, 6, 8], 
           'C': [10, 20, 30, 40]}
dti_01 = pd.date_range('2020-01-01', periods=4, freq='D') 
df_01 = pd.DataFrame(dict_01, index=dti_01)
df_01

#==================#
# Rows subtraction #
#==================#

# Compute differance between '0' row and '3' row and insert result to '3' row
df_01.diff(3)


#================================#
# The percent change computation #
#================================#
# aka C-RET - Cumulative Return Value (for ascending order timeseries)
# Note: pct change use shift under the hood, and shift use much computation
#   resources because it shifts the whole df instead of using 
#   first and last values
df_01.pct_change(1)

#or (for ascending order timeseries)
(df_01 - df_01.shift(1) ) / df_01.shift(1)
#or
(df_01 / df_01.shift(1) ) - 1

#or (for descending order timeseries)
(df_01.shift(1) / df_01) - 1

#============================#
# Rolling window calculation #
#============================#
# moving average

# Compute moving average for all columns
df_01.rolling(window = 2, win_type='triang').mean()
# TODO why sum works like mean there?

# Compute moving average for particular column
df_01.rolling(window = 2, win_type='triang')['A'].mean()

# Add particular column with moving average
import copy
df_mow_avg = copy.deepcopy(df_01)
df_mow_avg['MA'] = df_mow_avg.rolling(window = 2, win_type='triang')['A'].mean()
df_mow_avg



#=============================================================================#
# Operations across columns #
#===========================#

#====================================#
# Sort columns by certain row values #
#====================================#

# Creating the dataframe  
import pandas as pd
dict_01 = {'A': [1, 2, 3, 4],
           'B': [2, 4, 6, 8], 
           'C': [10, 20, 30, 40]}
dti_01 = pd.date_range('2020-01-01', periods=4, freq='D') 
df_01 = pd.DataFrame(dict_01, index=dti_01)
df_01


# sort columns by value in choosen row
df_01.sort_values(by='2020-01-04', axis=1, ascending=False)

# sort columns by value in the table with only 1 row
start_date = '2020-01-02'
end_date = '2020-01-02'
df_01.loc[start_date : end_date].sort_values(by=df_01 \
         .loc[start_date : end_date].index[0], axis=1, ascending=False)


#====================================#
# get top fraction of sorted columns #
#====================================#

# (highest values on the left)
fraction = 0.3
cols = df_01.columns[: round(fraction * len(df_01.columns))]
top_fraction = df_01[cols]


#=============#
# Sum columns #
#=============#
import pandas as pd

# Creating the dataframe  
rows_03 = 4
dict_03 = {'A': [1, 2, 3, 4], 'B': [2, 4, 6, 8], 'C': [10, 20, 30, 40]}
dti_03 = pd.date_range('2020-01-01', periods=rows_03, freq='D') 
df_03 = pd.DataFrame(dict_03, index=dti_03) # index arg is optional
df_03

df_04 = df_03.sum(axis=1, skipna=True)
df_04


#====================================#
# Normalize values to certain number #
#====================================#
# Normalize values to first value as a certain number 

number = 100
(df_04/df_04[0])*number


#=============================================================================#
# Missing data handling #
#=======================#

# Create dataframe  
import pandas as pd 
dict_02 = {'A': [1, 2, None, 4],
           'B': [None, None, 6, 8], 
           'C': [None, None, None, None]}
DateTimeIndex_02 = pd.date_range('2020-01-01', periods=4, freq='D') 
df_02 = pd.DataFrame(dict_02, index=DateTimeIndex_02)  # index arg is optional
df_02 

#=====================#
# forward fill method #
#=====================#
# Fill NA 

# applying forward fill method to fill the missing values 
df_02.ffill(axis = 0) 
# apply forward fill and backwardfill in case of some 
df_02.ffill(axis = 0).bfill(axis = 0)

# pct_change with forward fill method as parameter
df_02.pct_change(fill_method='ffill', periods=1)


#=======================================#
# Number of columns with all NaN values #
#=======================================#

df_02.isna().all().sum()


#========================================#
# Show which column has at least one NaN #
#========================================#

df_02.isna().any()


#=======================================#
# drop columns where all column is NaNs #
#=======================================#
        
df_02.dropna(axis=1, how='all')


#==============================================#
# drop columns where are below 2 non-NA values #
#==============================================#
        
df_02.dropna(axis=1, thresh=2)




