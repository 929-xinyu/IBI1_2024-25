import matplotlib.pyplot as plt

# create initial list
uk_countries = ['England', 'Wales', 'Northern Ireland', 'Scotland']
uk_populations = [57.11, 3.13, 1.91, 5.45]

china_provinces = ['Zhejiang', 'Fujian', 'Jiangxi', 'Anhui', 'Jiangsu']
china_populations = [65.77, 41.88, 45.28, 61.27, 85.15]

# sorting
uk_populations_sorted = sorted(uk_populations)
china_populations_sorted = sorted(china_populations)

# Print sorted list
print("sorted UK populations:", uk_populations_sorted)
print("sorted China populations:", china_populations_sorted)

# Create a pie chart for UK populations
plt.figure(figsize=(8, 8))
explode_uk = [0.1, 0, 0, 0]  # Highlight England
colors_uk = ['red', 'blue', 'green', 'yellow']
plt.pie(uk_populations, labels=uk_countries, autopct='%1.1f%%', startangle=90, explode=explode_uk, colors=colors_uk)
plt.title('population Distribution in UK Countries')
plt.show()

# Create a pie chart for Chinese provinces
plt.figure(figsize=(8, 8))
explode_china = [0, 0, 0, 0.1, 0]  # Highlight Anhui
colors_china = ['red', 'orange', 'yellow', 'green', 'blue']
plt.pie(china_populations, labels=china_provinces, autopct='%1.1f%%', startangle=90, explode=explode_china, colors=colors_china)
plt.title('population Distribution in Zhejiang-neighbouring Provinces')
plt.show()