
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

rows = 4

dict_01 = {'A': [1, 2, 3, 4],
           'B': [2, 4, 6, 8], 
           'C': [10, 20, 30, 40]}

# Create DateTimeIndex
dti = pd.date_range('2020-01-01', periods=rows, freq='D') 
# freq='MS'set the frequency in months 

df_01 = pd.DataFrame(dict_01, index=dti) # index arg is optional
df_01
