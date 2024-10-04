import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('dashboard/day.csv')

st.title("Bike Sharing Data Analysis")

st.write("### Dataset Overview")
st.write(data.head())

weatherRental = data.groupby('weathersit')['cnt'].sum().reset_index()

st.write("### Bike Rentals by Weather Condition")
fig, ax = plt.subplots()
sns.barplot(x='weathersit', y='cnt', data=weatherRental, ax=ax)
ax.set_xlabel('Weather Condition')
ax.set_ylabel('Total Rentals')
ax.set_title('Bike Rentals by Weather')
ax.set_xticks([0, 1, 2, 3])  
ax.set_xticklabels(['Clear', 'Mist', 'Light Rain', 'Heavy Rain'])
st.pyplot(fig)

seasonRental = data.groupby('season')['cnt'].sum().reset_index()

st.write("### Bike Rentals by Season")
fig, ax = plt.subplots()
sns.barplot(x='season', y='cnt', data=seasonRental, ax=ax)
ax.set_xlabel('Season')
ax.set_ylabel('Total Rentals')
ax.set_title('Bike Rentals by Season')
ax.set_xticks([0, 1, 2, 3])  
ax.set_xticklabels(['Spring', 'Summer', 'Fall', 'Winter'])
st.pyplot(fig)

st.write("### Correlation Matrix of Key Features")

plt.figure(figsize=(12, 8))
correlation = data[['temp', 'atemp', 'hum', 'windspeed', 'cnt']].corr()

# Create the heatmap
fig, ax = plt.subplots()
sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
ax.set_title('Correlation Matrix')
st.pyplot(fig)
