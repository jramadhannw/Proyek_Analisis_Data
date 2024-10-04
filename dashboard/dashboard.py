import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('dashboard/day.csv')

# Set the title of the dashboard
st.title("Bike Sharing Data Analysis")

# Display dataset information
st.write("### Dataset Overview")
st.write(data.head())

# Group data by weather and aggregate rental count
weatherRental = data.groupby('weathersit')['cnt'].sum().reset_index()

# Visualization for rentals by weather
st.write("### Bike Rentals by Weather Condition")
fig, ax = plt.subplots()
sns.barplot(x='weathersit', y='cnt', data=weatherRental, ax=ax)
ax.set_xlabel('Weather Condition')
ax.set_ylabel('Total Rentals')
ax.set_title('Bike Rentals by Weather')
ax.set_xticks([0, 1, 2, 3])  
ax.set_xticklabels(['Clear', 'Mist', 'Light Rain', 'Heavy Rain'])
st.pyplot(fig)

# Group data by season and aggregate rental count
seasonRental = data.groupby('season')['cnt'].sum().reset_index()

# Visualization for rentals by season
st.write("### Bike Rentals by Season")
fig, ax = plt.subplots()
sns.barplot(x='season', y='cnt', data=seasonRental, ax=ax)
ax.set_xlabel('Season')
ax.set_ylabel('Total Rentals')
ax.set_title('Bike Rentals by Season')
ax.set_xticks([0, 1, 2, 3])  
ax.set_xticklabels(['Spring', 'Summer', 'Fall', 'Winter'])
st.pyplot(fig)

# Correlation Matrix feature
st.write("### Correlation Matrix of Key Features")

# Generate the correlation matrix
plt.figure(figsize=(12, 8))
correlation = data[['temp', 'atemp', 'hum', 'windspeed', 'cnt']].corr()

# Create the heatmap
fig, ax = plt.subplots()
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
ax.set_title('Correlation Matrix')
st.pyplot(fig)

# Filter data by weather and season
st.sidebar.header("Filter Options")
selectedWeather = st.sidebar.multiselect('Select Weather Condition', data['weathersit'].unique())
selectedSeason = st.sidebar.multiselect('Select Season', data['season'].unique())

filteredData = data.copy()

if selectedWeather:
    filteredData = filteredData[filteredData['weathersit'].isin(selectedWeather)]

if selectedSeason:
    filteredData = filteredData[filteredData['season'].isin(selectedSeason)]

# Display filtered data
st.write("### Filtered Data")
st.write(filteredData.head())
