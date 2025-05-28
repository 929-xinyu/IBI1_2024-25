# Project Plan:
# 1. The purpose of the program is to find genes that contain both a TATA box and a specific splice site in a given FASTA file.
# 2. The program reads a FASTA file, extracts gene names and sequences, and checks for the presence of a TATA box and a specified splice site.
# 3. If a gene contains at least one TATA box and the specified splice site, it is added to the results.
# 4. The program counts the number of TATA boxes in each gene and outputs the results to the console.

# Import necessary libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set working directory
os.chdir("/Desktop/IBI/IBI_2024-25/Practical10")  # Replace with actual path
print(os.getcwd())  # Verify current path
print(os.listdir())  # Check if files exist

# Load data
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# Data inspection
dalys_data.head(5)      # View first 5 rows
dalys_data.info()       # Data types and column names
dalys_data.describe()   # Statistical summary

# Data filtering
print(dalys_data.iloc[0, 3])       # 1st row, 4th column
print(dalys_data.iloc[0:10, 2])    # First 10 rows, 3rd column (Year)

# Filter DALYs data for 1990
data_1990 = dalys_data.loc[dalys_data["Year"] == 1990, "DALYs"]

# Compare country data
uk = dalys_data.loc[dalys_data["Entity"] == "United Kingdom", ["Year", "DALYs"]]
france = dalys_data.loc[dalys_data["Entity"] == "France", ["Year", "DALYs"]]

# Plot UK trend
plt.plot(uk["Year"], uk["DALYs"], "b-", label="UK")
plt.xticks(rotation=90)  # Rotate x-axis labels
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title("DALYs in the UK Over Time")
plt.legend()
plt.show()

# Compare China and UK
china = dalys_data.loc[dalys_data["Entity"] == "China", ["Year", "DALYs"]]
plt.plot(china["Year"], china["DALYs"], "g-", label="China")
plt.plot(uk["Year"], uk["DALYs"], "b-", label="UK")
plt.legend()
plt.show()