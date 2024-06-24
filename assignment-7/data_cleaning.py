import pandas as pd
from exceptions import CustomDataCleaningError, MissingColumnError  # importing custom errors

def clean_data(df): # function to perform the data cleaning
    if df.empty:
        raise CustomDataCleaningError("Data is empty.") # exception handling for if the data is empty.

    # list with names of required columns so we can raise exception if all columns are not there
    required_columns = ["Country/Region", "Confirmed", "Deaths", "Recovered", "Active", "New cases",
                        "New deaths", "New recovered", "Deaths / 100 Cases", "Recovered / 100 Cases",
                        "Deaths / 100 Recovered", "Confirmed last week", "1 week change", "1 week % increase",
                        "WHO Region"]
    for col in required_columns:
        if col not in df.columns:
            raise MissingColumnError(col)

    df.drop_duplicates(inplace=True) # removing all the redundant data from the dataset

    # this is a list with the names of all columns which are supposed to have a numeric value 
    numeric_columns = ["Confirmed", "Deaths", "Recovered", "Active", "New cases",
                       "New deaths", "New recovered", "Deaths / 100 Cases",
                       "Recovered / 100 Cases", "Deaths / 100 Recovered",
                       "Confirmed last week", "1 week change", "1 week % increase"] 

    # we are making sure that all the values in the numeric columns have values of numeric type only
    df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors="coerce")

    # this is a list of names of columns in which missing value will be filled as zero
    fill_zero_columns = ["Confirmed", "Deaths", "Recovered", "New cases", "New deaths",
                         "New recovered", "Deaths / 100 Cases", "Recovered / 100 Cases",
                         "Deaths / 100 Recovered", "1 week change", "1 week % increase"]

    # assuming missing values to be zero
    df[fill_zero_columns] = df[fill_zero_columns].fillna(0)

    # calculating missing values (if any) that shouldn't be assumed to be zero
    df["Active"] = df["Active"].fillna(df["Confirmed"] - df["Deaths"] - df["Recovered"])  # active cases are calculated by subtracting deaths and recovered from confirmed cases
    df["Confirmed last week"] = df["Confirmed last week"].fillna(df["Confirmed"] - df["1 week change"])  # confirmed last week cases are calculated by subtracting 1 week change from confirmed cases

    # we are converting all string values to Title Case and stripping whitespace
    df["Country/Region"] = df["Country/Region"].str.title().str.strip()
    df["WHO Region"] = df["WHO Region"].str.title().str.strip()

    print("Data cleaned successfully!")

    return df # returning dataset