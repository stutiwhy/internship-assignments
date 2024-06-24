# importing all the necessary modules
import os
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
from exceptions import CustomFileHandlingError
from file_handling import load_clean_data

# loading clean data with imported function from file_handling
try:
    df = load_clean_data('clean_covid_data.csv')
except CustomFileHandlingError as e: # exception handling
    print(f"Error while handling file: {e}")

# function to plot bar graph of total cases
def plot_total_cases(df, case_type):
    plt.figure(figsize=(12, 8)) # figure size
    plt.bar(df['Country/Region'], df[case_type], color='blue')

    plt.title(f'Total {case_type} COVID-19 Cases by Country/Region')
    plt.xlabel('Country/Region')
    plt.ylabel(f'Number of {case_type} Cases')
    plt.xticks(rotation=90) # text is rotated 90 degrees and looks standing
    plt.tight_layout()

    # we are saving the figure as an image in a folder called "plots" because i don't want the directory to become messy with too many plot images
    plot_filename = f'plots/total_{case_type.lower()}_cases.png' # deciding appropriate file name for pic to be saved as
    ensure_directory('plots')
    plt.savefig(plot_filename)

    return plt # returning the plotted figure

# function to plot graph of top n number of countries with highest cases
def plot_top_countries(df, top_n):
    plt.figure(figsize=(12, 8))
    top_countries = df.groupby('Country/Region')[['Confirmed', 'Deaths', 'Recovered']].max().sum(axis=1).nlargest(top_n)
    plt.bar(top_countries.index, top_countries.values, color='blue')

    plt.title(f'Top {top_n} Countries with Highest Number of COVID-19 Cases')
    plt.xlabel('Country/Region')
    plt.ylabel('Number of Cases')
    plt.xticks(rotation=45)
    plt.tight_layout()

    plot_filename = f'plots/top{top_n}_countries_cases.png'
    ensure_directory('plots')
    plt.savefig(plot_filename)

    return plt

# function to plot graph for daily cases
def plot_daily_cases(df):
    plt.figure(figsize=(12, 8))
    plt.bar(df['Country/Region'], df['New cases'], color='orange')

    plt.title('Daily New COVID-19 Cases')
    plt.xlabel('Country/Region')
    plt.ylabel('Number of New Cases')
    plt.xticks(rotation=90)
    plt.tight_layout()

    plot_filename = f'plots/daily_new_cases.png'
    ensure_directory('plots')
    plt.savefig(plot_filename)

    return plt

# function to ensure that that we are saving the plot imaged in plots file only
def ensure_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)