### About the datset
> this dataset is a collection of data of COVID-19 cases that is arranged country-wise. it has data from 188 countries. it has the columns : Country/Region, Confirmed, Deaths, Recovered, Active, New cases, New deaths, New recovered, Deaths / 100 Cases, Recovered / 100 Cases, Deaths / 100 Recovered, Confirmed last week, 1 week change, 1 week % increase, WHO Region. 

> we can gain a great amount of insights from this data like total case count all over the world, geographical distribtion of cases like in which general region the cases are more or in which region there are very few cases. we can make predictions of how many new cases might come in the future in the regions and if we are working with government, we can make arrangements and take precautions accordingly. we can make interesting observations like if after a specific event in a specific region or country cases have jumped, or cases have plummeted. We can make many types of visualizations from this data, like i have created a bar graph of countries and their number of daily cases.

> in the streamlit dashboard, you can view plots of different countries and top 10 countries with highest cases. it also filters by type of case : recovered, confirmed, death

### How to run
>> Steps :
1) download the files: "analysis.py", "file_handling.py", "data_cleaning.py", "exceptions.py", "visualization.py", "dashboard.py" "country_wise_latest.csv".
2) make a seperate folder(preferably) and place them in it. make sure all the files are in the same directory(folder).
3) open "analysis.py" file and execute it.
4) you will see insights printed on your screen and a new "clean_covid_data.csv" file created in the same directory.
5) now open the directory in your command prompt, one of the methods of doing this is to type cd folderpath in the command prompt.
6) make sure you have all the necessary modules installed like streamlit, matplotlib, pandas, numpy, then type "streamlit run dashboard.py" in the command prompt.
7) now it will automatically take you to your browser where a new tab will be opened of the streamlit interface in dashboard.py.
8) after applying whatever filters you want, click on generate plot button to see the graphs of it.

## Data cleaning (datacleaning.py)
>> Steps taken :
1) imported pandas and exceptions.
2) defined a new function clean_data(df) which accepts dataset as an argument.
3) checks if dataset is empty and if it is, it raises custom data cleaning exception that says data is empty.
4) duplicate values are removed from the dataset.
5) created a list called numeric_columns which stores names of all columns which are supposed to have numeric type data.
6) all missing values (if any) in numeric_columns columns are filled with zero.
7) active cases are calculated by subtracting deaths and recovered from confirmed cases.
8) confirmed last week cases are calculated by subtracting 1 week change from confirmed cases.
9) converted all string values to Title Case and striped whitespace (if any).
10) return dataset.

## File handling (file_handling.py)
>> Steps taken :
1) imported pandas.
2) defined function to save the data to a csv file (no index row).
3) defined function to load(read) the clean data saved for further analysis.
4) applied exception handling to handle potential errors or issues.

## Exception handling (exceptions.py)
>> Steps taken : 
1) defined a CustomDataCleaningError deriving it from Exception class for it to be an exception that can be raised.
2) defined a MissingColumnError deriving it from CustomDataCleaningError because this error comes under data cleaning error. it is more specific.
3) defined a CustomFileHandlingError that can be raised at any file handling error.

## Analysis (analysis.py)
>> Steps taken : 
1) imported pandas and all necessary exceptions.
2) defined a function "load_data" to load raw data from the csv file saved to clean it.
3) defined "analyze_data" function that calculates all the analysis values like sum of things and the highest/lowest cases countries. it also prints all of it in a neat format.
4) defined the last function "analyze()" that does the work of calling other functions for loadind, cleaning, saving and printing the analysis.
5) added bar graph plotting with countries on x axis and daily cases on y.
6) applied necessary exceptions. 
7) invoked "analyze" function.

## Visualization (visualization.py)
>> Steps taken :
1) imported all necessary modules like pandas, matplotlib, numpy and other custom modules.
2) loaded the clean data from a function imported from file_handling file.
3) defined a function plot_total_cases that accepted dataframe and case_type as arguments. it creates a graph of total cases.
4) defined another function plot_top_countries that takes dataframe and number of top countries as argument. it plots graph for highest cases in top n number of countries (argument given as 10).
5) function plot_daily_cases does exactly what it says which is plot the daily number of cases in a graph. it accepts dataframe as argument.
6) added feature to save the plotted graphs as png in another ("plots") in the same directory as this file to avoid mess in the main folder.
7) defined function to ensure that the images are being saved in the correct path.

## Streamlit Dashboard (dashboard.py)
>> Steps taken :
1) imported all modules required.
2) defined the main function that will do all the work.
3) in the main function, title was added.
4) loaded the clean data with function from file_handling.
5) made sidebar title.
6) added filters selectboxes, first of choosing global or a specific country to show info and graph on, and second to choose type of case.
7) created Generate Plot button and then a conditional loop to plot appropriate graph based on what filters are put.
8) appropriate error handling applied.

### Exceptions
i have made 3 custom exceptions in this project : 
1) CustomDataCleaningError
>> a specific type of exception that can be raised when any error related to data cleaning occurs. helps in differentiating data cleaning errors from other types of errors(inbuilt errors).

>> code snippet where it can be raised :

    def clean_data(df): # function to perform the data cleaning
        if df.empty:
            raise CustomDataCleaningError("Data is empty.") 

2) MissingColumnError - derived from CustomDataCleaningError
>> handles situations where a column is missing from a dataset. inherits from the CustomDataCleaningError class, which makes it a type of data cleaning error. 

>> code snippet where it can be raised :

    required_columns = ["Country/Region", "Confirmed", "Deaths", "Recovered", "Active", "New cases",
                        "New deaths", "New recovered", "Deaths / 100 Cases", "Recovered / 100 Cases",
                        "Deaths / 100 Recovered", "Confirmed last week", "1 week change", "1 week % increase",
                        "WHO Region"]
    for col in required_columns:
        if col not in df.columns:
            raise MissingColumnError(col)

3) CustomFileHandlingError
>> can be raised when any error related to file handling occurs.

>> code snippet where it can be raised :

    try:
        df = pd.read_csv(filename)
        if df.empty:
            raise ValueError("The .csv file is empty.")
        return df 
    except FileNotFoundError as e: 
        raise CustomFileHandlingError(f"File {filename} not found: {str(e)}")
    except Exception as e:
        raise CustomFileHandlingError(f"Error loading data from {filename}: {str(e)}")