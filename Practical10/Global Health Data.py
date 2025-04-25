import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# set the working directory to where the dataset is located
os.chdir("c:/Users/HUAWEI/Desktop/IBI/IBI1_2024-25/Practical10")
print(os.getcwd())  # check current working directory
print(os.listdir())  # check if the dataset exists

# Check if the file exists
file_path = "dalys-rate-from-all-causes.csv"
if not os.path.exists(file_path):
    raise FileNotFoundError(f"The file '{file_path}' does not exist in the directory '{os.getcwd()}'.")

# Load the dataset
dalys_data = pd.read_csv(file_path)
print(dalys_data.head(5))

print(dalys_data.info())
print(dalys_data.describe())

# check for missing values
years_column = dalys_data.iloc[0:10, 2]  
print(years_column)

# Boolean Filtering for 1990 Data 
is_1990 = dalys_data['Year'] == 1990
dalys_1990 = dalys_data.loc[is_1990, ['Entity', 'DALYs']]
print("\nall countries'DALYs in 1990：")
print(dalys_1990)

# compare DALYs between UK and France in 1990
uk_data = dalys_data[dalys_data['Entity'] == 'United Kingdom']
uk_mean = uk_data['DALYs'].mean()
france_data = dalys_data[dalys_data['Entity'] == 'France']
france_mean = france_data['DALYs'].mean()
print(f"\nUK Mean DALYs: {uk_mean:.2f}")
print(f"France Mean DALYs: {france_mean:.2f}")
# UK trend visualization
plt.figure(figsize=(10, 6))
plt.plot(uk_data['Year'], uk_data['DALYs'], 'b-', label='UK')
plt.title('UK DALYs Trend (1990-2019)')
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('uk_dalys.png')
plt.close()

# self-defined question: How does the DALYs trend in China compare to that in the UK?
china_data = dalys_data[dalys_data['Entity'] == 'China']
plt.figure(figsize=(12, 6))
plt.plot(uk_data['Year'], uk_data['DALYs'], 'b-', label='UK')
plt.plot(china_data['Year'], china_data['DALYs'], 'r--', label='China')
plt.title('comparison of trend between China and UK')
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('china_uk_comparison.png')
plt.close()