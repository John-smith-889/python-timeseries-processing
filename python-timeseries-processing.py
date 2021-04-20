
#==================#
# datetime objects #
#==================#

# Create datetime object from string
import datetime
date_time_str = '18/09/93'
date_time_obj = datetime.datetime.strptime(date_time_str, '%d/%m/%y')


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

df_01
start_date_01 = '2020-01-01'
end_date_01 = '2020-01-02'
df_01.loc[start_date_01 : end_date_01] # (closed interval)


#=============================#
# Select rows between 2 dates # use datatime objects
#=============================#
# (closed interval)

import datetime

# Create datetime object from string
start_date_02 = '2020-01-01'
start_date_datatime = datetime.datetime.strptime(start_date_02, '%Y-%m-%d')
end_date_02 = '2020-01-02'
end_date_datatime = datetime.datetime.strptime(end_date_02, '%Y-%m-%d')

# select rows with 
df_01.loc[start_date_datatime : end_date_datatime] # (closed interval)


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


#====================================#
# Sort columns by certain row values #
#====================================#
import pandas as pd

# Creating the dataframe  
rows_02 = 4
dict_02 = {'A': [1, 2, 3, 4],
           'B': [2, 4, 6, 8], 
           'C': [10, 20, 30, 40]}
dti_02 = pd.date_range('2020-01-01', periods=rows_02, freq='D') # DatetimeIndex
df_02 = pd.DataFrame(dict_02, index=dti_02) # index arg is optional
df_02

# sort columns by value in choosen row
df_02.sort_values(by='2020-01-04', axis=1, ascending=False)

# sort columns by value in the table with only 1 row
start_date = '2020-01-02'
end_date = '2020-01-02'
df_02.loc[start_date : end_date].sort_values(by=df_01 \
         .loc[start_date : end_date].index[0], axis=1, ascending=False)


#====================================#
# get top fraction of sorted columns #
#====================================#

# (highest values on the left)
fraction = 0.3
cols = df_02.columns[: round(fraction * len(df_02.columns))]
top_fraction = df_02[cols]


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

