import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set the title of the dashboard
st.title("Bike Sharing Data Analysis")

# Load the dataset
@st.cache
def load_data():
    data = pd.read_csv('dashboard/data.csv')
    df_day = pd.read_csv(day_data)
    return df_day

df_day = load_data()

# Display dataset information
st.header("Dataset Information")
st.write(df_day.head())
st.write(df_day.describe())

# Group data by weather
st.header("Group Data by Weather")
weather_group = df_day.groupby('weathersit').agg({'cnt': 'sum'}).reset_index()
weather_labels = {1: 'Clear, Few clouds', 2: 'Mist + Cloudy', 3: 'Light Snow, Light Rain', 4: 'Heavy Rain, Ice Pallets'}
weather_group['weathersit'] = weather_group['weathersit'].map(weather_labels)
st.write(weather_group)

# Visualization for rentals by weather
st.header("Rentals by Weather")
plt.figure(figsize=(10, 5))
sns.barplot(data=weather_group, x='weathersit', y='cnt', palette='viridis')
plt.title('Total Rentals by Weather')
plt.xlabel('Weather')
plt.ylabel('Total Rentals')
st.pyplot(plt)

# Correlation matrix feature
st.header("Correlation Matrix")
correlation_matrix = df_day.corr()
st.write(correlation_matrix)

# Create the heatmap
st.header("Heatmap of Correlation Matrix")
plt.figure(figsize=(10, 5))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Heatmap of Correlation Matrix')
st.pyplot(plt)

# Filter the data by season and weather
st.header("Filter Data by Season and Weather")
season = st.selectbox("Select Season", options=[1, 2, 3, 4], format_func=lambda x: {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'}[x])
weather = st.selectbox("Select Weather", options=[1, 2, 3, 4], format_func=lambda x: weather_labels[x])

filtered_data = df_day[(df_day['season'] == season) & (df_day['weathersit'] == weather)]
st.write(filtered_data)

# Visualization of filtered data
st.header("Visualization of Filtered Data")
plt.figure(figsize=(10, 5))
sns.lineplot(data=filtered_data, x='dteday', y='cnt', marker='o')
plt.title('Rentals Over Time for Selected Season and Weather')
plt.xlabel('Date')
plt.ylabel('Total Rentals')
plt.xticks(rotation=45)
st.pyplot(plt)
