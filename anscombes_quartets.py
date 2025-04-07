# Author:- Anurag Gupta  ## E-mail 999.anuraggupta@gmail.com
# The script can be downloaded from:- 
# https://github.com/ag999git/jupyter_notebooks/blob/master/anscombes_quartets
import pandas as pd
# ----- STEP 1:- Read the data set from Wikipedia page
# You can see signature of pandas.read_html() at link in next line
# https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.read_html.html
url = r'https://en.wikipedia.org/wiki/Anscombe%27s_quartet'
df = pd.read_html(url)
# This wikipedia page has 2 tables.
# First table (index 0) has summary stastics
# Second table (index 1) has the 4 data sets
print(df[0])  # prints summary statistics of the data set
df2 = df[1]  # df2 is simply an alias for df[1]
print(df2)  # Prints the 4 data sets in from of a DataFrame

# ----- STEP 2:- Clean the data 
# Step 2(1) -- Change the column names
df2.columns = ['X1', 'Y1', 'X2', 'Y2', 'X3', 'Y3', 'X4', 'Y4']
# print(df2)  ## Uncomment to check that column names changed
# Step 2(2) -- Remove row containing x and y at index 0
df2.drop([0], axis = 0, inplace = True)  
# print(df2)  ## Uncomment to confirm that row with x and y removed
# Step 2(3) -- convert all columns of DataFrame to numeric values
df2 = df2.apply(pd.to_numeric) 
# print (df2.dtypes)  ## Uncomment to confirm that all cells of DataFrame have numerics

# ----- STEP 3:- Plot the 4 data sets
%matplotlib inline
import matplotlib.pyplot as plt
# --- Step 3(1): Create 4 subplots
fig, ax = plt.subplots(nrows=2, ncols=2, figsize = (30, 30), 
                       sharex = 'col', sharey = 'row')
# --- Step 3(2):- Create 4 Scatter Plots
ax[0][0].scatter(df2.X1, df2.Y1, s = 200) 
ax[0][1].scatter(df2.X2, df2.Y2, s = 200) 
ax[1][0].scatter(df2.X3, df2.Y3, s = 200) 
ax[1][1].scatter(df2.X4, df2.Y4, s = 200) 

# ----- STEP 4:- Plot the linear regression lines for the 4 plots
# Use numpy.polyfit() method. Signature is at link on next line
# https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html
import numpy as np
# Use polyfit() to get slope and intercept
m1, b1 = np.polyfit(df2.X1, df2.Y1, deg = 1)
print('First dataset->', round(m1, 2), round(b1, 2))
# m2 and b2 are same as m1 and b1
m2, b2 = np.polyfit(df2.X2, df2.Y2, deg = 1)
print('Second dataset->', round(m2, 2), round(b2, 2))
# m3 and b3 are same as m1 and b1
m3, b3 = np.polyfit(df2.X3, df2.Y3, deg = 1)
print('Third dataset->', round(m3, 2), round(b3, 2))
# m4 and b4 are same as m1 and b1
m4, b4 = np.polyfit(df2.X4, df2.Y4, deg = 1)
print('Fourth dataset->', round(m4, 2), round(b4, 2))
# Infact the slopes and intercepts of all 4 graphs is same.
# So we can add this best fit line to all 4 graphs as below:-
x = np.array(range(16))
print(x)
ax[0][0].plot(x, m1 * x + b1)
ax[0][1].plot(x, m2 * x + b2)
ax[1][0].plot(x, m3 * x + b3)
ax[1][1].plot(x, m4 * x + b4)
fig

# ----- STEP 5:- Plot the degree 2 polyfit for the second data set
z = np.polyfit(df2.X2, df2.Y2, deg = 2)
print(z) 
ax[0][1].plot(x, z[0] * x**2 + z[1] * x + z[2]) 
fig
