import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load data
hour_df = pd.read_csv('hour.csv')
day_df = pd.read_csv('day.csv')

# Ubah dteday ke tipe datetime
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
day_df['dteday'] = pd.to_datetime(day_df['dteday'])

# Page title
st.title("Krismantoro's Bike Rentals Dashboard")

# Sidebar for dataset selection
st.sidebar.title("Pilihan Data")
dataset = st.sidebar.selectbox('Pilih Dataset', ['Hourly Data', 'Daily Data'])

# Select dataset based on user input
df = hour_df if dataset == 'Hourly Data' else day_df
st.write(f"### Data yang digunakan: {dataset}")

# 1. Correlation Matrix
st.header('Correlation Matrix')
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 12))
sns.heatmap(hour_df.corr(), annot=True, cmap='coolwarm', fmt='.2f', ax=ax1)
ax1.set_title('Correlation Matrix for Hourly Data')
sns.heatmap(day_df.corr(), annot=True, cmap='coolwarm', fmt='.2f', ax=ax2)
ax2.set_title('Correlation Matrix for Daily Data')
plt.tight_layout()
st.pyplot(fig)

# 2. Distribution of Rentals per Hour/Day
st.header('Distribution of Rentals')
plt.figure(figsize=(6, 4))
if dataset == 'Hourly Data':
    sns.histplot(df['cnt'], bins=30, kde=True)
    plt.title('Distribusi Jumlah Rental Sepeda per Jam')
    plt.xlabel('Jumlah Rental Sepeda')
else:
    sns.histplot(df['cnt'], bins=30, kde=True)
    plt.title('Distribusi Jumlah Rental Sepeda per Hari')
    plt.xlabel('Jumlah Rental Sepeda')
plt.ylabel('Frekuensi')
st.pyplot(plt)

# 3. Rentals per Hour by Season (for Hourly Data)
if dataset == 'Hourly Data':
    st.header('Bike Rentals per Hour by Season')
    plt.figure(figsize=(8, 6))  
    color_palette = ['cyan', 'black', 'green', 'red']
    sns.lineplot(x='hr', y='cnt', hue='season', data=df, palette=color_palette)
    plt.title('Rental Sepeda per Jam berdasarkan Musim')
    plt.xlabel('Jam')
    plt.ylabel('Rental Sepeda')
    plt.legend(title='Season', labels=['Spring', 'Summer', 'Fall', 'Winter'])
    st.pyplot(plt)

# 4. Rentals by Month (for Daily Data)
if dataset == 'Daily Data':
    st.header('Bike Rentals by Month')
    plt.figure(figsize=(10, 6))
    sns.barplot(x='mnth', y='cnt', data=df, palette='rocket')
    plt.title('Rental Sepeda berdasarkan Bukan')
    plt.xlabel('Bulan')
    plt.ylabel('Rental Sepeda')
    st.pyplot(plt)

# 5. Temperature vs Rentals
st.header('Temperature vs Bike Rentals')
plt.figure(figsize=(8, 6))
sns.scatterplot(x='temp', y='cnt', hue='season', data=df)
plt.title(f'Temperature vs Rental Sepeda ({dataset})')
plt.xlabel('Temperature')
plt.ylabel('Rental Sepeda')
st.pyplot(plt)

# 6. Humidity vs Rentals
st.header('Humidity vs Bike Rentals')
plt.figure(figsize=(8, 6))
sns.scatterplot(x='hum', y='cnt', hue='season', data=df)
plt.title(f'Humidity vs Rental Sepeda ({dataset})')
plt.xlabel('Humidity')
plt.ylabel('Rental Sepeda')
st.pyplot(plt)

# 7. Weather Conditions vs Rentals (only for hourly data)
if dataset == 'Hourly Data':
    st.header('Weather Conditions vs Bike Rentals')
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='weathersit', y='cnt', hue='season', data=df)
    plt.title('Kondisi Cuaca vs Rental Sepeda (Hourly Data)')
    plt.xlabel('1=Clear, 2=Mist, 3=Light Snow/Rain, 4=Heavy Rain')
    plt.ylabel('Rental Sepeda')
    st.pyplot(plt)

# Additional visualizations for Hourly Data
if dataset == 'Hourly Data':
    # 8. Rentals by Month (Hourly Data)
    st.header('Bike Rentals by Month')
    plt.figure(figsize=(10, 6))
    sns.barplot(x='mnth', y='cnt', data=hour_df, palette='rocket')
    plt.title('Rental Sepeda berdasarkan Bulan')
    plt.xlabel('Bulan')
    plt.ylabel('Rental Sepeda')
    st.pyplot(plt)

# Additional visualizations for Daily Data
if dataset == 'Daily Data':
    # 9. Weather Conditions vs Rentals (Daily Data)
    st.header('Kondisi Cuaca vs Rental Sepeda')
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='weathersit', y='cnt', hue='season', data=day_df)
    plt.title('Kondisi Cuaca vs Rental Sepeda')
    plt.xlabel('1=Clear, 2=Mist, 3=Light Snow/Rain, 4=Heavy Rain')
    plt.ylabel('Rental Sepeda')
    st.pyplot(plt)

    # 10. Rentals by Month (Daily Data)
    st.header('Bike Rentals by Month')
    plt.figure(figsize=(10, 6))
    sns.barplot(x='mnth', y='cnt', data=day_df, palette='rocket')
    plt.title('Rental Sepeda berdasarkan Bulan')
    plt.xlabel('Bulan')
    plt.ylabel('Rental Sepeda')
    st.pyplot(plt)