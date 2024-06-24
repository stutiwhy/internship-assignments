# importing all necessary modules
import pandas as pd
from exceptions import CustomDataCleaningError, CustomFileHandlingError
from file_handling import save_clean_data
from data_cleaning import clean_data
import matplotlib.pyplot as plt

# function to load raw data from the csv file saved to clean it
def load_data(filename): 
    try:
        return pd.read_csv(filename)
    except FileNotFoundError as e: # exception handling
        raise CustomFileHandlingError(f"File '{filename}' not found.") from e
    except Exception as e:
        raise CustomFileHandlingError(f"Error loading file '{filename}': {e}") from e

# function to analyze raw data loaded and print the insights 
def analyze_data(df): 
    try:
        # sum of the numeric values of the specific columns mentioned
        confirmed = df["Confirmed"].sum() 
        deaths = df["Deaths"].sum()
        recovered = df["Recovered"].sum()

        # idxmax() finds the index of the row with the max value and loc finds the value based on its index
        highest_cases_country = df.loc[df["Confirmed"].idxmax(), "Country/Region"]
        lowest_case_country = df.loc[df["Confirmed"].idxmin(), "Country/Region"]

        # main analysis
        print("\n------ Data Analysis ------\n")
        print(f"Total confirmed cases: {confirmed}")
        print(f"Total deaths: {deaths}")
        print(f"Total recovered cases: {recovered}")
        print(f"Country with highest cases : {highest_cases_country}")
        print(f"Country with lowest cases : {lowest_case_country}")
        print("\n------ End Analysis ------\n")

    except KeyError as e: # exception handling
        raise CustomDataCleaningError(f"Missing key {e} in the dataset.") from e
    except Exception as e:
        raise CustomDataCleaningError(f"Error analyzing data: {e}") from e

# function that ties all other functions above together
def analyze():
    try:
        raw_data = load_data("country_wise_latest.csv")
        cleaned_dataset = clean_data(raw_data)
        save_clean_data(cleaned_dataset)
        analyze_data(cleaned_dataset)

        # plotting the data as a bar graph
        plt.figure(figsize=(15, 8))
        plt.bar(cleaned_dataset["Country/Region"], cleaned_dataset["New cases"], color="lightpink")
        plt.title("COVID-19 Cases")        
        plt.xlabel("Countries/Regions")
        plt.ylabel("Daily New Cases")
        plt.xticks(rotation=90) # rotates the text in the x axis by 90 degrees
        plt.tight_layout() # for better layout
        plt.show()

    # exception handling
    except CustomFileHandlingError as e:
        print(f"A file handling error occured: {e}")
    except CustomDataCleaningError as e:
        print(f"A data cleaning error occured: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")

analyze() # calling this function to start all the work