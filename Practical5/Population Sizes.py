# Project Plan:
# 1. The purpose of this code is to create a pie chart showing the population distribution in the UK and some of the China provinces.
# 2. Create two lists: one for the UK countries and their populations, and another for the Chinese provinces and their populations.
# 3. Sort the populations and print the sorted lists.
# 4. Create a pie chart for the UK populations, highlighting England.
# 5. Create a pie chart for the Chinese provinces, highlighting Zhejiang.
# 6. Use different colors for each slice of the pie chart.

# import necessary libraries
import matplotlib.pyplot as plt

# create two lists: one for the UK countries and their populations, and another for the Chinese provinces and their populations
uk_countries = ['England', 'Wales', 'Northern Ireland', 'Scotland'] # uk countries'list
uk_populations = [57.11, 3.13, 1.91, 5.45] # uk populations'list

china_provinces = ['Zhejiang', 'Fujian', 'Jiangxi', 'Anhui', 'Jiangsu'] # china provinces'list
china_populations = [65.77, 41.88, 45.28, 61.27, 85.15] # china populations'list

# sort the populations
uk_populations_sorted = sorted(uk_populations) 
china_populations_sorted = sorted(china_populations)
# print sorted list
print("sorted UK populations:", uk_populations_sorted)
print("sorted China populations:", china_populations_sorted)

# create a pie chart for UK populations
explode_uk = [0.1, 0, 0, 0]  # highlight England
colors_uk = ['red', 'blue', 'green', 'yellow']
plt.pie(uk_populations, labels=uk_countries, autopct='%1.1f%%', startangle=90, explode=explode_uk, colors=colors_uk)
plt.title('population distribution in UK Countries')
# show the pie chart of UK countries population
plt.show()

# create a pie chart for Chinese provinces
explode_china = [0.1, 0, 0, 0, 0]  # highlight Zhejiang
colors_china = ['red', 'orange', 'yellow', 'green', 'blue']
plt.pie(china_populations, labels=china_provinces, autopct='%1.1f%%', startangle=90, explode=explode_china, colors=colors_china)
plt.title('population distribution in Zhejiang-neighbouring Provinces')
# show the pie chart of China provinces population
plt.show()