# importing all the necessary modules
import streamlit as st
import matplotlib.pyplot as plt
from visualization import plot_total_cases, plot_top_countries, plot_daily_cases
from exceptions import CustomFileHandlingError
from file_handling import load_clean_data

# the function that will do everything
def main():
    st.title('COVID-19 Data Dashboard') # prints the string in big big letters on top of streamlit app

    # loading the data with nice error handling
    try:
        df = load_clean_data('clean_covid_data.csv')  
        st.subheader("File loaded.")
    except CustomFileHandlingError as e:
        st.error(f"Error loading data: {e.message}")
        st.stop()

    st.sidebar.title('Choose your filters') # again, prints the message in big big letters but only in sidebar this time 

    countries = ['Global'] + list(df['Country/Region'].unique()) # gets all the country names from the dataset
    selected_country = st.sidebar.selectbox('Select a Country/Region', countries) # creates a selectbox with all the country names

    if selected_country != 'Global': # if a country name is selected then plot the graph for that specific country only
        selected_country_data = df[df['Country/Region'] == selected_country].iloc[0] # displays all the data about that country from the dataset in form of a table
        st.subheader(f"Selected Country Data: {selected_country}")
        st.write(selected_country_data)

    case_types = ['Confirmed', 'Deaths', 'Recovered'] # list to store case types 
    selected_case_type = st.sidebar.selectbox('Select Case Type', case_types) # case types sidebox made

    # generating the plots here, calling the appropriate functions for specific filers
    if st.sidebar.button('Generate Plot'): 
        try:
            if selected_country == 'Global':
                filtered_df = df.groupby('Country/Region').sum().reset_index()
            else:
                filtered_df = df[df['Country/Region'] == selected_country]

            if selected_case_type == 'Confirmed':
                st.subheader("COVID-19 cases : Confirmed")
                fig = plot_total_cases(filtered_df, 'Confirmed')
                st.pyplot(fig)

            elif selected_case_type == 'Deaths':
                st.subheader("COVID-19 cases : Deaths")
                fig = plot_total_cases(filtered_df, 'Deaths')
                st.pyplot(fig)

            elif selected_case_type == 'Recovered':
                st.subheader("COVID-19 cases : Recovered")
                fig = plot_total_cases(filtered_df, 'Recovered')
                st.pyplot(fig)

            fig_top = plot_top_countries(df, 10)
            st.pyplot(fig_top)

            fig_daily = plot_daily_cases(filtered_df)
            st.pyplot(fig_daily)

        except CustomFileHandlingError as e: # error handling
            st.error(f"Error: {e.message}")
        except ValueError as e:
            st.error(f"Empty file error: {str(e)}")

main() # invoking the function to do the its thing