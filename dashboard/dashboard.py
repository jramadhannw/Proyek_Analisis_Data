import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('dashboard/day.csv')

# Set the title for the Streamlit app
st.title("Analysis of Bike Sharing Data")

# Display an overview of the dataset
st.write("### Overview of the Dataset")
st.write(data.head())

# Group the data by weather conditions and calculate total rentals
weather_rentals = data.groupby('weathersit')['cnt'].sum().reset_index()

# Show bike rentals categorized by weather conditions
st.write("### Total Bike Rentals by Weather Condition")
fig, ax = plt.subplots()
sns.barplot(x='weathersit', y='cnt', data=weather_rentals, ax=ax)
ax.set_xlabel('Weather Condition')
ax.set_ylabel('Total Rentals')
ax.set_title('Bike Rentals by Weather Conditions')
ax.set_xticks([0, 1, 2, 3])  
ax.set_xticklabels(['Clear', 'Mist', 'Light Rain', 'Heavy Rain'])
st.pyplot(fig)

# Group the data by season and compute total rentals
season_rentals = data.groupby('season')['cnt'].sum().reset_index()

# Display bike rentals by season
st.write("### Total Bike Rentals by Season")
fig, ax = plt.subplots()
sns.barplot(x='season', y='cnt', data=season_rentals, ax=ax)
ax.set_xlabel('Season')
ax.set_ylabel('Total Rentals')
ax.set_title('Bike Rentals by Season')
ax.set_xticks([0, 1, 2, 3])  
ax.set_xticklabels(['Spring', 'Summer', 'Fall', 'Winter'])
st.pyplot(fig)

# Show the correlation matrix for key features
st.write("### Correlation Matrix of Important Features")

plt.figure(figsize=(12, 8))
correlation_matrix = data[['temp', 'atemp', 'hum', 'windspeed', 'cnt']].corr()

# Create and display the heatmap for the correlation matrix
fig, ax = plt.subplots()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
ax.set_title('Correlation Matrix')
st.pyplot(fig)
