# Here we are fabricating complete python pandas but only DataFrame part

# imports
import numpy as np
import pandas as pd


# literals

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Heidi', 'Ivan', 'Judy', 'Kenny', 'Laura', 'Mallory', 'Nina', 'Oscar', 'Peggy', 'Quinn', 'Rupert', 'Sybil', 'Trent'],
    'Age': [25, np.nan, 23, 40, 22, 35, np.nan, 29, 41, 30, np.nan, 27, 34, 28, 33, 22, 37, 26, 32, 24],
    'Score': [85, np.nan, 92, 78, 85, 90, np.nan, 88, 94, 78, np.nan, 85, 90, 88, 92, 100, 85, 78, 94, 85]
}


# defined
def dataFrame_1():                                                                      # Basic Attributes
    '''This function demonstrates the usage of index, columns, dtypes, shape, size, empty, values'''
    print("Index:", df.index, "\n\n")
    print("Columns:", df.columns, "\n\n")
    print("Data Types:", df.dtypes, "\n\n")
    print("Shape:", df.shape, "\n\n")
    print("Size:", df.size, "\n\n")
    print("Is Empty:", df.empty, "\n\n")
    print("Values:", df.values, "\n\n")

def dataFrame_2():                                                                      # Index Attributes
    '''This function demonstrates the usage of axes, index.name, columns.name'''
    df.index.name = 'kya pata'                 # Set names for index and columns
    df.columns.name = 'kuch bhi'

    print("Index:", df.axes, "\n\n")
    print("Columns:", df.index.name, "\n\n")
    print("Data Types:", df.columns.name, "\n\n")

    
def dataFrame_3():                                                                      # Data & Statistics
    '''This function demonstrates the usage of head(n=5), tail(n=5), describe(), info(), mean(), sum()'''
    print("Head (first 5 rows):\n", df.head(5), "\n\n")
    print("Tail (last 5 rows):\n", df.tail(5), "\n\n")
    print("Descriptive Statistics:\n", df.describe(), "\n\n")
    print("Information about the DataFrame:\n", df.info(), "\n\n")
    print("Mean of the Age in DataFrame:", df['Age'].mean(), "\n\n")       # We niether can get mean nor sum for non-numeric/ Alphabetical values
    print("Sum of the Score of all students in the DataFrame: ", df['Score'].sum(), "\n\n")


    
def dataFrame_4():                                                                      # Data & Statistics
    '''This function demonstrates the usage of min(), max(), std(), var(), count()'''
    print("Minimum Values:\n", df['Score'].min(), "\n\n")
    print("Maximum Values:\n", df['Score'].max(), "\n\n")
    print("Standard Deviation:\n", df['Age'].std(), "\n\n")
    print("Variance:\n", df['Age'].var(), "\n\n")
    print("Count of Non-NA/Null Observations:\n", df.count(), "\n\n")


def dataFrame_5():                                                                      # Handling Missing Data
    '''This function demonstrates the usage of isnull(), notnull(), fillna(), dropna()'''

    print("Detecting Missing Values (isnull):\n", df.isnull(), "\n\n")
    print("Detecting Non-Missing Values (notnull):\n", df.notnull(), "\n\n")
    
    df_filled = df.fillna(0)   # Fill missing values with a specified value (e.g., 0)
    print("Filling Missing Values with 0 (fillna):\n", df_filled, "\n\n")
    
    df_dropped = df.dropna()   # Drop rows with any missing values
    print("Dropping Rows with Missing Values (dropna):\n", df_dropped, "\n\n")


def dataFrame_6(df):                                                                      # Data Manipulation
    '''This function demonstrates the usage of apply(), map(), replace(), rename(), sort_values(by, ascending=True)'''

    # global df - this is different method if not want to use df in function itself

    
    df['Age'] = df['Age'].apply(lambda x: x + 1 if pd.notnull(x) else x)        # Apply a function to the 'Age' column to add 1 to each value
    print("Using apply() to increment Age by 1:\n", df, "\n\n")
    
    
    df['Name Length'] = df['Name'].map(len)     # Map values in the 'Name' column to their lengths
    print("Using map() to get the length of each Name:\n", df, "\n\n")
    
    
    df['Score'] = df['Score'].replace(85, 90)       # Replace values in the 'Score' column (e.g., replace 85 with 90)
    print("Using replace() to change Score 85 to 90:\n", df, "\n\n")
    
    
    df = df.rename(columns={'Name': 'Student Name', 'Age': 'Student Age', 'Score': 'Test Score'})       # Rename columns
    print("Using rename() to rename columns:\n", df, "\n\n")
    
   
    df = df.sort_values(by='Test Score', ascending=False)       # Sort values by 'Test Score' in descending order
    print("Using sort_values() to sort by Test Score in descending order:\n", df, "\n\n")



def dataFrame_7(df):                                                                      # Data Manipulation
    '''This function demonstrates the usage of sort_index(ascending=Falsee), merge(), join(), groupby()'''

    additional_data = {                                     # Sample DataFrame to demonstrate merge
        'Name': ['Charlie', 'Eve', 'Ivan', 'Mallory', 'Oscar'],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
    }
   
    additional_data_2 = {                                   # Sample DataFrame to demonstrate join
        'Name': ['Charlie', 'Eve', 'Ivan', 'Mallory', 'Oscar'],
        'Gender': ['M', 'F', 'M', 'F', 'M']
    }

    additional_df = pd.DataFrame(additional_data)
    additional_df_2 = pd.DataFrame(additional_data_2).set_index('Name')

   
    sorted_df = df.sort_index(ascending= False)         # Sort the DataFrame by its index in ascending order
    print("Using sort_index() to sort the DataFrame by its index in ascending order:\n", sorted_df, "\n\n")
    
    merged_df = pd.merge(df, additional_df, on='Name', how='left')      # Merge the original DataFrame with the additional DataFrame on 'Name'
    print("Using merge() to merge the DataFrames on 'Name':\n", merged_df, "\n\n")

    joined_df = df.set_index('Name').join(additional_df_2, how='left')      # Join the original DataFrame with the additional DataFrame
    print("Using join() to join the DataFrames on 'Name':\n", joined_df.reset_index(), "\n\n")

    # Group by 'Score' and calculate the mean of each group
    # grouped_df = df.groupby('Score').mean()                   # These ways are also appkucable
    # grouped_df = df.groupby('Score').mean('Score')
    grouped_df = df.groupby('Score').mean(numeric_only=True)
    print("Using groupby() to group by 'Score':\n", grouped_df, "\n\n")
    


def dataFrame_8(df):                                                                      # Selection
    '''This function demonstrates the usage of loc[], iloc[], at[], iat[}'''
    
    loc_selection = df.loc[0:3, ['Name', 'Age']]        # Using loc[] to select rows by label and columns by label
    print("Using loc[] to select rows 0 to 3 and columns 'Name' and 'Age':\n", loc_selection, "\n\n")
    
    iloc_selection = df.iloc[0:3, [0, 1]]       # Using iloc[] to select rows by position and columns by position
    print("Using iloc[] to select rows 0 to 3 and columns 0 and 1:\n", iloc_selection, "\n\n")
    
    at_value = df.at[0, 'Name']     # Using at[] to access a single value for a row/column label pair
    print("Using at[] to access the value at row 0 and column 'Name':\n", at_value, "\n\n")
    
    iat_value = df.iat[0, 0]        # Using iat[] to access a single value for a row/column position pair
    print("Using iat[] to access the value at row 0 and column 0:\n", iat_value, "\n\n")
    


    
# Main
df = pd.DataFrame(data)
print("\n\n")

# print(df, "\n\n")
# dataFrame_1()
# dataFrame_2()
# dataFrame_3()
# dataFrame_4()
# dataFrame_5()
# dataFrame_6(df)           #
# dataFrame_7(df)           # Bit different
# dataFrame_8(df)           #






'''

# Basic Attributes:
- index: The index (row labels) of the DataFrame.
- columns: The column labels of the DataFrame.
- dtypes: The data types of each column.
- shape: The shape of the DataFrame (number of rows, number of columns).
- size: The number of elements in the DataFrame.
- empty: Check if the DataFrame is empty.
- values: The underlying Numpy array of the DataFrame.

# Index Attributes:
- axes: Return a list of the row axis labels and column axis labels.
- index.name: Set the name of the index.
- columns.name: Set the name of the columns.

# Data and Statistics:
- head(n=5): Return the first `n` rows.
- tail(n=5): Return the last `n` rows.
- describe(): Generate descriptive statistics.
- info(): Print a concise summary of the DataFrame.
- mean(): Return the mean of the values.
- sum(): Return the sum of the values.

- min(): Return the minimum value.
- max(): Return the maximum value.
- std(): Return the standard deviation of the values.
- var(): Return the variance of the values.
- count(): Return the number of non-NA/null observations.

# Handling Missing Data:
- isnull(): Detect missing values.
- notnull(): Detect non-missing values.
- fillna(): Fill missing values.
- dropna(): Drop missing values.

# Data Manipulation:
- apply(): Apply a function along an axis of the DataFrame.
- map(): Map values using an input correspondence (use with Series).
- replace(): Replace values.
- rename(): Rename the labels of a DataFrame.
- sort_values(by, ascending=True): Sort the DataFrame by specified column(s).

- sort_index(ascending=True): Sort the DataFrame by its index.
- merge(): Merge DataFrame objects by columns or indexes.
- join(): Join columns with other DataFrame.
- groupby(): Group DataFrame using a mapper or by columns.

# Selection:
- loc[]: Access a group of rows and columns by labels or a boolean array.
- iloc[]: Access a group of rows and columns by position.
- at[]: Access a single value for a row/column label pair.
- iat[]: Access a single value for a row/column position pair.



@ Example of Using Attributes:

import pandas as pd

data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8]
}
df = pd.DataFrame(data)

# Basic attributes
print(df.index)
print(df.columns)
print(df.dtypes)
print(df.shape)
print(df.size)
print(df.empty)
print(df.values)

# Data and statistics
print(df.head())
print(df.tail())
print(df.describe())
print(df.info())
print(df.mean())
print(df.sum())
print(df.min())
print(df.max())
print(df.std())
print(df.var())
print(df.count())

'''