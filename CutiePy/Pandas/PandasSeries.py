# Here we are practicing complete python pandas but only Series part

# imports
import pandas as pd
import numpy as np


# literals

index = [   
            'Alice', 
            'Bob', 
            'Charlie', 
            'David', 
            'Eve', 
            'Frank', 
            'Grace', 
            'Heidi', 
            'Ivan', 
            'Judy',         
            'Kenny', 
            'Laura', 
            'Mallory', 
            'Nina', 
            'Oscar', 
            'Peggy', 
            'Quinn', 
            'Rupert', 
            'Sybil', 
            'Trent'     
]

data = [
            85, 
            np.nan, 
            92, 
            78, 
            85, 
            90, 
            np.nan, 
            88, 
            94, 
            78, 
            np.nan, 
            85, 
            90, 
            88, 
            92, 
            100, 
            85, 
            78, 
            94, 
            85          
]


# defined

def series_1():                                                                                 # Basic attributes
    '''This function demonstrates the usage of index, values, dtype name, shape'''
    print("Index:", mySeries.index, "\n\n")
    print("Values:", mySeries.values, "\n\n")
    print("Data Type:", mySeries.dtype, "\n\n")
    print("Name:", mySeries.name, "\n\n")
    print("Shape:", mySeries.shape, "\n\n")


def series_2():                                                                                 # Basic Attributes
    '''This function demonstrates the usage of size, nbytes, is_unique, empty, hasnans'''
    print("Size:", mySeries.size, "\n\n")
    print("Bytes Consumed:", mySeries.nbytes, "\n\n")
    print("Is Unique:", mySeries.is_unique, "\n\n")
    print("Is Empty:", mySeries.empty, "\n\n")
    print("Has NaNs:", mySeries.hasnans, "\n\n")


def series_3():                                                                                 # Index Attributes
    '''This function demonstrates the usage of index.name'''
    print("Axes:", mySeries.axes, "\n\n")
    mySeries.index.name = 'Students'
    print("Index Name:", mySeries.index.name, "\n\n")
    print(mySeries, "\n\n")


def series_4():                                                                                 # Data and Statistics
    '''This function demonstrates the usage of unique(), nunique(), count(), sum(), mean(), median()'''
    print("Unique Values:", mySeries.unique(), "\n\n")
    print("Number of Unique Values:", mySeries.nunique(), "\n\n")
    print("Count:", mySeries.count(), "\n\n")
    print("Sum:", mySeries.sum(), "\n\n")
    print("Mean:", mySeries.mean(), "\n\n")
    print("Median:", mySeries.median(), "\n\n")


def series_5():                                                                                 # Data and Statistics
    '''This function demonstrates the usage of min(), max(), std(), var(), mode(), describe()'''
    print("Min:", mySeries.min(), "\n\n")
    print("Max:", mySeries.max(), "\n\n")
    print("Standard Deviation:", mySeries.std(), "\n\n")
    print("Variance:", mySeries.var(), "\n\n")
    print("Mode:", mySeries.mode(), "\n\n\n")
    print("Description of mySeries:",mySeries.describe(), sep= "\n\n", end= "\n\n")


def series_6():                                                                                 # Handling missing data
    '''This function demonstrates the usage of isnull(), notnull(), fillna(), dropna()'''
    print("Is Null:\n", mySeries.isnull(), "\n\n")
    print("Not Null:\n", mySeries.notnull(), "\n\n")
    print("Filled NaNs:\n", mySeries.fillna(0), "\n\n")
    print("Dropped NaNs:\n", mySeries.dropna(), "\n\n")

def series_7():                                                                                 # Value Manipulation
    '''This function demonstrates the usage of apply(), map(), replace(), sort_values(), sort_index(), append()'''
    print("Applied Function (x^2):\n", mySeries.apply(lambda x: x**2 if pd.notnull(x) else x), "\n\n")
    print("Mapped Values (Increase by 10):\n", mySeries.map(lambda x: x + 10 if pd.notnull(x) else x), "\n\n")
    print("Replaced Values (85 with 100):\n", mySeries.replace(85, 100), "\n\n")
    print("Sorted Values:\n", mySeries.sort_values(), "\n\n")
    print("Sorted Index:\n", mySeries.sort_index(), "\n\n")
    print("Appended Series:\n", mySeries.append(pd.Series([95, 80], index=['Uma', 'Vera'])), "\n\n")

def series_8():                                                                                 # Value Manipulation
    '''This function demonstrates the usage of drop(), clip(), cumsum(), cumprod(), cummix(), cummax()'''
    print("Dropped Elements (Alice and Bob):\n", mySeries.drop(['Alice', 'Bob']), "\n\n")
    print("Clipped Values (Min 80, Max 90):\n", mySeries.clip(80, 90), "\n\n")
    print("Cumulative Sum:\n", mySeries.cumsum(), "\n\n")                       ## search what cumulative means on internet
    print("Cumulative Product:\n", mySeries.cumprod(), "\n\n")
    print("Cumulative Min:\n", mySeries.cummin(), "\n\n")
    print("Cumulative Max:\n", mySeries.cummax(), "\n\n")


# Main
mySeries = pd.Series(data= data, index= index, name= "Student Scores")
print("\n\n")

# print(mySeries, "\n\n")
# series_1()
# series_2()
# series_3()
# series_4()
# series_5()
# series_6()
# series_7()
# series_8()






'''

@ Some Attributes and Functions for Quiver Plots:

Basic Attributes:
- index: The index (row labels) of the Series.
- values: The data values of the Series.
- dtype: The data type of the Series.
- name: The name of the Series.
- shape: The shape of the Series.

- size: The number of elements in the Series.
- nbytes: The number of bytes consumed by the data in the Series.
- is_unique: Check if the Series has unique values.
- is_monotonic: Check if the Series values are monotonically increasing.
- empty: Check if the Series is empty.
- hasnans: Check if the Series contains any NaN values.

Index Attributes:
- axes: Return a list of the row axis labels.
- index.name: Set the name of the index.
- index.names: Set the names of the index levels.
- index.levels: Get the levels of the index (for MultiIndex).
- index.labels: Get the integer labels of the index (for MultiIndex).

Data and Statistics:
- unique(): Return unique values.
- nunique(): Return the number of unique values.
- count(): Return the number of non-NA/null observations.
- sum(): Return the sum of the values.
- mean(): Return the mean of the values.
- median(): Return the median of the values.

- min(): Return the minimum value.
- max(): Return the maximum value.
- std(): Return the standard deviation of the values.
- var(): Return the variance of the values.
- mode(): Return the mode of the values.
- describe(): Generate descriptive statistics.

Handling Missing Data:
- isnull(): Detect missing values.
- notnull(): Detect non-missing values.
- fillna(): Fill missing values.
- dropna(): Drop missing values.

Value Manipulation:
- apply(): Apply a function to each element.
- map(): Map values using a function or dictionary.
- replace(): Replace values.
- sort_values(): Sort the values.
- sort_index(): Sort by index.
- append(): Append values.

- drop(): Remove elements.
- clip(): Trim values outside specified bounds.
- cumsum(): Cumulative sum.
- cumprod(): Cumulative product.
- cummin(): Cumulative minimum.
- cummax(): Cumulative maximum.



@ Example of Using Attributes

import pandas as pd

data = [10, 20, 30, 40]
series = pd.Series(data, index=['a', 'b', 'c', 'd'])

# Basic attributes
print(series.index)
print(series.values)
print(series.dtype)
print(series.name)
print(series.shape)
print(series.size)
print(series.nbytes)
print(series.is_unique)
print(series.is_monotonic)
print(series.empty)
print(series.hasnans)

# Index attributes
print(series.axes)
series.index.name = 'Labels'
print(series.index.name)

# Data and statistics
print(series.unique())
print(series.nunique())
print(series.count())
print(series.sum())
print(series.mean())
print(series.median())
print(series.min())
print(series.max())
print(series.std())
print(series.var())
print(series.mode())
print(series.describe())

'''