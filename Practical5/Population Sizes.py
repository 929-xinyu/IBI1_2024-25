import matplotlib.pyplot as plt

# 数据准备data preparation
uk_countries = ['England', 'Wales', 'Northern Ireland', 'Scotland']
uk_populations = [57.11, 3.13, 1.91, 5.45]

china_provinces = ['Zhejiang', 'Fujian', 'Jiangxi', 'Anhui', 'Jiangsu']
china_populations = [65.77, 41.88, 45.28, 61.27, 85.15]

# 排序sorting
uk_populations_sorted, uk_countries_sorted = zip(*sorted(zip(uk_populations, uk_countries)))
china_populations_sorted, china_provinces_sorted = zip(*sorted(zip(china_populations, china_provinces)))

# 打印排序后的列表Print sorted list
print("Sorted UK populations:", uk_populations_sorted)
print("Sorted China populations:", china_populations_sorted)

# 创建饼图Create a pie chart
fig, ax = plt.subplots(1, 2, figsize=(12, 6))

# 英国国家人口分布National Population Distribution in the UK
ax[0].pie(uk_populations_sorted, labels=uk_countries_sorted, autopct='%1.1f%%', startangle=90)
ax[0].set_title('Population Distribution in UK Countries')

# 中国省份人口分布Population distribution in Chinese provinces
ax[1].pie(china_populations_sorted, labels=china_provinces_sorted, autopct='%1.1f%%', startangle=90)
ax[1].set_title('Population Distribution in Zhejiang-neighbouring Provinces')

plt.show()