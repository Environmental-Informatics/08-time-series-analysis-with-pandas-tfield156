# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 12:44:08 2020
This script works through the tutorial at http://earthpy.org/pandas-basics.html
and saves the required plots to PDF files
@authors: tfield
@github: tfield156
"""

# Import necessary libraries
import matplotlib.pyplot as plt #included so plots can show up separately
import pandas as pd
import numpy as np
from pandas import Series, DataFrame, Panel


# Load in the data file
ao = np.loadtxt("monthly.ao.index.b50.current.ascii.txt")

# Show a sample of data in file and overall dimensions of the data
print(ao[0:2])
print(ao.shape)

# Create a list of dates incremented by month that is the same length as the data
dates = pd.date_range(start='1950-01', periods=ao.shape[0], freq='M')

# Show what these dates look like
print(dates)

#Create a series with the dates and data, show it
AO = Series(ao[:,2], index=dates)
print(AO)

# Plot the timeseries data
plt.figure()
AO.plot()
plt.grid(True)
plt.xlabel('Month')
plt.ylabel('Arctic Oscillation')
plt.title('Arctic Oscillation Data - Field')
plt.savefig('Out23_DailyAO_Field.pdf')
# Plot a section of the timeseries data
plt.figure()
AO['1980':'1990'].plot()
plt.figure()
AO['1980-05':'1981-03'].plot()

# Output by index or date
print(AO[120])
print(AO['1960-01'])
print(AO['1960'])
print(AO[AO > 0])

#
#
# NEXT SECTION OF TUTORIAL (DATAFRAME)

# Load data and create series again
nao = np.loadtxt('norm.nao.monthly.b5001.current.ascii.txt')
dates_nao = pd.date_range(start='1950-01', periods=nao.shape[0], freq='M')
NAO = Series(nao[:,2], index=dates_nao)

# Same time period as before
print(NAO.index)

# Create dataframe
aonao = DataFrame({'AO' : AO, 'NAO' : NAO})

# Plot data
aonao.plot(subplots=True)

# Reference data by column name or method of dataframe variable
print(aonao['NAO'])
print(aonao.NAO)

# Add column to dataframe
aonao['Diff'] = aonao['AO'] - aonao['NAO']

# Show first several lines of new dataframe
print(aonao.head())

# Remove column from dataframe
del aonao['Diff']

# Show last few lines of dataframe
print(aonao.tail())

# Show slice from dataframe
print(aonao['1981-01':'1981-03'])


# Complex indexing example
import datetime
aonao.loc[(aonao.AO > 0) & (aonao.NAO < 0) & (aonao.index > datetime.datetime(1980,1,1)) & (aonao.index < datetime.datetime(1989,1,1)),'NAO'].plot(kind='barh')

#
#
# NEXT SECTION OF TUTORIAL (STATISTICS)

# Statistics for each variable in dataframe
print(aonao.mean())
print(aonao.max())
print(aonao.min())

# Row-wise statistic
print(aonao.mean(1))

# All statistics at once
print(aonao.describe())

#
#
# RESAMPLING

# Annual mean
AO_mm = AO.resample("A").mean()
plt.figure()
AO_mm.plot(style='g--')

# Annual median
AO_mm = AO.resample("A").median()
plt.figure()
AO_mm.plot()
plt.grid(True)
plt.xlabel('Year')
plt.ylabel('Arctic Oscillation')
plt.title('Arctic Oscillation Annual Median - Field')
plt.savefig('Out48_AnMedAO_Field.pdf')
# 3 year max resample
AO_mm = AO.resample("3A").apply(np.max)
plt.figure()
AO_mm.plot()

# multiple resamples based on different functions
AO_mm = AO.resample("A").apply(['mean', np.min, np.max])
AO_mm['1900':'2020'].plot(subplots=True)
plt.figure()
AO_mm['1900':'2020'].plot()

# Show resampled dataframe
print(AO_mm)

#
#
# MOVING STATISTICS

# Rolling mean
plt.figure()
aonao.rolling(window=12, center=False).mean().plot(style='-g')
plt.grid(True)
plt.xlabel('Month')
plt.ylabel('Artic Oscillation')
plt.title('Oscillation Rolling Means (Arctic, North Atlantic) - Field')
plt.savefig('Out52_RollingMeanAONAO_Field.pdf')
# Rolling correlation
plt.figure()
aonao.AO.rolling(window=120).corr(other=aonao.NAO).plot(style='-g')

# Corrrelation coefficients
print(aonao.corr())