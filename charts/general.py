# # 📊 Google Play Store Analytics Internship Project
# **Intern:** Ramesh Mallela  
# **Duration:** 10 May 2025 – 10 July 2025  
# **Organization:** NullClass (Remote)
# 
# This notebook contains data preprocessing and 5 interactive visualizations built using Plotly. Time-based filters are applied to display graphs within certain IST time ranges.

import pandas as pd
import plotly.express as px
from datetime import datetime, time
import pytz
from IPython.display import display


# Load the dataset
df = pd.read_csv("Play Store Data.csv")
df.head()

# ## 🔧 Data Preprocessing

# Clean up Installs column
df['Installs'] = df['Installs'].astype(str).str.replace('[+,]', '', regex=True)
df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')

# Clean up Size column
df['Size'] = df['Size'].replace('Varies with device', '0')
df['Size'] = df['Size'].astype(str).str.replace('M', 'e6').str.replace('k', 'e3')
df['Size'] = df['Size'].str.replace('[a-zA-Z]', '', regex=True)
df['Size'] = pd.to_numeric(df['Size'], errors='coerce')

# Clean up Rating column
df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
df.dropna(subset=['Rating'], inplace=True)

# Fill missing values
df['Type'].fillna('Free', inplace=True)

# Fix Price column safely (handles Free, $, float, NaN)
def clean_price(val):
    if pd.isnull(val):
        return 0.0
    val = str(val).replace('$', '').strip()
    if val.lower() == 'free':
        return 0.0
    try:
        return float(val)
    except ValueError:
        return 0.0

df['Price'] = df['Price'].apply(clean_price)

# Handle Category and drop remaining missing
df['Category'].fillna('Unknown', inplace=True)
df.dropna(subset=['Installs', 'Size'], inplace=True)
print("Shape of cleaned dataframe:", df.shape)
df.head()


# Get current IST time
tz_ist = pytz.timezone('Asia/Kolkata')
current_time = datetime.now(tz_ist).time()
print("Current IST Time:", current_time)


