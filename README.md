# Environmental Informatics

## Assignment 08 - Time Series Analysis with Pandas

### Lab Objectives

On completion of this lab, students will be able to:

1. Use Time and Date functions with pandas DataFrames to conduct time series analysis of a dataset.
2. Import a data file into a Pandas DataFrame that uses Datetime as the index.
3. Use Pandas Datetime methods to summarize time series data.

### Reading Assignment

Data Analysis with Open Source Tools:

- Chapter 4: Two Variablesime as a Variable: Time Series Analysis

### The Lab Assignment

1. Start by cloning this assignment to the folder where you have been completing assignments.

2. Next, complete the tutorial [Time Series Analysis with Pandas](http://earthpy.org/pandas-basics.html), but include all of the tutorial code in a Python program called **PandasDatesDemo.py** that is included in this repository.

   - The "set_printoptions()" function does not appear to work with the current version of pandas.
   - Do not set your graphics to inline (see "ln[7]:"), graphics are already prepared in the spyder interface.
   - The `!wget` command will download the data file from within the console in spyder, but can also be run directly from the Linux prompt (drop the "!" from the start of the command, this is telling the Python interpretor that the command should be run at the Linux shell and not interpreted as a Python statement).
   - What dates should you use to define the correct record length?  From the Linux prompt, use "head" and "tail" to determine the start and end dates for your data file (the tutorial was written in 2013, but the data file continues to be updated).  
   - The length of record for the AO and NAO files may not be the same, despite what the tutorial document says.  If they are not the same length, what happens when they are combined into a single DataFrame?
   - Submit the following plots for evaluation: 
     - Daily Atlantic Oscillation (AO) plot (Out [23]:)
     - Annual median values for AO (Out [48]:)
     - Rolling mean for both AO and NAO (Out [52]:)
     
3. Once you have completed the tutorial, use your new skills to write a Python script called **program-08.py** that will do the following. 

   - Read the contents of the file **WabashRiver_DailyDischarge_20150317-20160324.txt** into a Pandas dataframe.
     - This file contains daily discharge for the Wabash River at the Lafayette, Indiana gauge from March 17, 2015 through March 24, 2016.
     - Use Columns 3 and 4 for a single Datetime element.
     - Use Column 6 (discharge in cubic feet per second) for the value.
     - For this process, the following additional information may prove useful:
       - The Pandas documentation on the [read_table](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_table.html) DataFrame method.
       - More information can also be found at the [IO Tools page](http://pandas.pydata.org/pandas-docs/stable/io.html), in particular help on how to get the read function to parse the date for you automatically can be found [here](http://pandas.pydata.org/pandas-docs/stable/io.html#datetime-handling).
       - Information on how to get read_tables to handle variable white space as a separator can be found at this [discussion page](http://stackoverflow.com/questions/12021730/can-pandas-handle-variable-length-whitespace-as-column-delimeters).
       - Also note that all of this does not have to all be done in a single line statement.  You may find it easier to import the data in a more raw format, and then work it into a usable final format.  I find this approach useful when datafile quality is suspect, as it provides more options to assess problems and catch errors.  The file I have given you is pretty clean, so not necessarily representative of the types of data you will find in real life. 
   - Create a plot of daily average streamflow for the period of record, written to a PDF or PS file.
   - Using the daily average flow data, identify and plot the 10 days with highest flow, written to a PDF or PS file.  Use symbols to represent the data on the same time axis used for the full daily flow record.
   - Create a plot of monthly average streamflow for the period of record, written to a PDF or PS file.

4. Be sure that the script has a complete header comment block, appropriate in-line comments, and runs without intervention relative to where the datafile is stored in the repository.

#### What to turn in...

The following should be included in your GitHub repository:

1. A working tutorial solution file called **PandasDatesDemo.py**.

2. The original data file, **WabashRiver_DailyDischarge_20150317-20160324.txt**, provided with the repository.

3. A working program called **program-08.py**.

4. Put your input file, output files, and processing script in the assignment repository and push to GitHub to submit.

#### Grading Rubric (50 pts Total)

| Question | Description | Score |
| -------- | ----------- | ----- |
| 1. |Complete the tutorial Time series analysis with Pandas, and submit the following for evaluation | (15 pts) |
| 1.1. | Daily Atlantic Oscillation (AO) plot (Out [23]:) | 5 pts |
| 1.2. | Annual median values for AO (Out [48]:) | 5 pts |
| 1.3. | Rolling mean for both AO and NAO (Out [52]:) | 5 pts |
| 2. | Write a Python script to complete the following analysis | (35 pts) |
| 2.1. | Read the contents of the file into a Pandas series using Columns 3 and 4 for a single Date-Time element, and Column 6 (discharge in cubic feet per second) for the value. | 10 pts |
| 2.2. | Create a plot of daily average streamflow for the period of record, written to a PDF or PS file. | 5 pts |
| 2.3. | Using the daily average flow data, identify and plot the 10 days with highest flow, written to a PDF or PS file.  Use symbols to represent the data on the same time axis used for the full daily flow record. | 5 pts |
| 2.4. | Create a plot of monthly average streamflow for the period of record, written to a PDF or PS file. | 5 pts |
| 3. | Submit all input and output files. | 5 pts |
| 4. | Program has complete header and adequate in-line comments. | 5 pts |
