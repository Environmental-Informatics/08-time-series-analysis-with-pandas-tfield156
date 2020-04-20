# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 19:42:11 2020
This script loads in Daily Discharge for the Wabash River from 3/17/2015 to
3/24/2016. the data is resampled for daily and monthly averages and the ten
highest daily flow days are determined. Plots are then generated to show this
data graphically
@authors: tfield
@github: tfield156
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import Series, DataFrame, Panel


# Load data and create dataframe
# skip 25 header lines, use names provided,
# combine datetime and timezone into single column
nameList = ['datetime','agency_cd','site_no','01_00060','01_00060_cd'] #Combined date and timezone, moved to first index
wb = pd.read_table('WabashRiver_DailyDischarge_20150317-20160324.txt', header=25, parse_dates=[[2,3]])
wb.columns=nameList

# Change indices to datetimes
wb.index = wb['datetime']

# Series with discharge in ft3/s
flow = wb['01_00060']

# Daily average flow
avgFlowD = flow.resample("D").mean()

# Daily average flow plot
plt.figure(figsize=(9,6.5))
avgFlowD.plot(style = 'r')
plt.grid(True)
plt.xlabel('Date')
plt.ylabel('Daily Average Streamflow (ft3/s)')
plt.title('Daily Average Streamflow for the Wabash River - Field')
plt.savefig('DailyAverageStreamflow_Field.pdf')

# 10 Highest Flow Days
maxflow10 = avgFlowD.sort_values(ascending=False).head(10)

# Daily flow plot with 10 highest days indicated
plt.figure(figsize=(9,6.5))
avgFlowD.plot(style = 'r')
maxflow10.plot(style = 'ok')
plt.grid(True)
plt.xlabel('Date')
plt.ylabel('Daily Average Streamflow (ft3/s)')
plt.title('Daily Average Streamflow for the Wabash River - Field')
plt.legend(['Daily Average Flow', '10 Highest Flow Days'])
plt.savefig('DailyAverageStreamflow10Max_Field.pdf')

# Monthly average flow
avgFlowM = flow.resample("M").mean()

# Daily average flow plot
plt.figure(figsize=(9,6.5))
avgFlowM.plot(style = 'r')
plt.grid(True)
plt.xlabel('Month')
plt.ylabel('Monthly Average Streamflow (ft3/s)')
plt.title('Monthly Average Streamflow for the Wabash River - Field')
plt.savefig('MonthlyAverageStreamflow_Field.pdf')

