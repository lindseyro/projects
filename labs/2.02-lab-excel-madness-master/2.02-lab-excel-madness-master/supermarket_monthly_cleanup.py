import numpy as np
import pandas as pd
import os

# Create an output folder.
try:
    os.mkdir('output')
except:
    pass

# Create a files variable that contains all of our data files.
files = os.listdir('./data')

# Read in file containing actual product names matched up against their price lookup (PLU) codes.
plu = pd.read_csv("plu-codes.csv")
plu.rename(columns = {'plu_code': 'prodcode'}, inplace = True)

# Function to import filename and city name and return a fully processed DataFrame:
# 1. Read in the data from the given file and city.
# 2. Create USD and pound columns.
# 3. Merge in product names.
# 4. Drop unnecessary columns.
# 5. Add a date column
def process_data(file, city):
    """Function to clean up each date/city tab and go through all of step 2."""
    
    df = pd.read_excel(file, city)
    df['price_usd'] = df['price_eu'] * 1.1
    df['weight_lb'] = df['weight_kg'] * 2.2
    df = pd.merge(
        left = df,
        right = plu,
        how = 'left',
        on = 'prodcode')
    df.drop(['weight_kg', 'price_eu'], axis = 'columns', inplace = True)
    df['date'] = file[7:-5]
    return df

# Dictionary of city name to desired output file name.
city_dict = {
    "Atlanta": "atl.csv",
    "Austin": "atx.csv",
    "Boston": "bos.csv",
    "Chicago": "chi.csv",
    "Denver": "den.csv",
    "Los Angeles": "lax.csv",
    "New York": "nyc.csv",
    "San Francisco": "sf.csv",
    "Seattle": "sea.csv",
    "Washington, DC": "dc.csv"
}

# Concatenate all days of month into one dataframe for each city.
# Add a `city` column.
# Reorder the columns.
# Loop through city_dict and write the data to our `output` folder.
for k, v in city_dict.items():
    df_city = pd.concat([process_data('./data/' + file, k) for file in files])
    df_city['city'] = k
    df_city = df_city[['city', 'date', 'product', 'prodcode', 'quantity', 'weight_lb', 'price_usd']]
    df_city.to_csv('./output/' + v, index = False)

# To combine into one dataframe:
city_files = os.listdir('./output')
city_files = city_files[1:]
combined_df = pd.concat([pd.read_csv('./output/' + file) for file in city_files])
