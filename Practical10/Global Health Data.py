
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 设置工作目录
os.chdir("/Desktop/IBI/IBI_2024-25/Practical10")  # 替换为实际路径
print(os.getcwd())  # 验证当前路径
print(os.listdir())  # 检查文件是否存在

# 加载数据
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# 数据检查
dalys_data.head(5)      # 查看前5行
dalys_data.info()       # 数据类型和列名
dalys_data.describe()   # 统计摘要

# 数据筛选
print(dalys_data.iloc[0, 3])       # 第1行第4列
print(dalys_data.iloc[0:10, 2])    # 前10行的第3列（年份）

# 筛选1990年的DALYs数据
data_1990 = dalys_data.loc[dalys_data["Year"] == 1990, "DALYs"]

# 比较国家数据
uk = dalys_data.loc[dalys_data["Entity"] == "United Kingdom", ["Year", "DALYs"]]
france = dalys_data.loc[dalys_data["Entity"] == "France", ["Year", "DALYs"]]

# 绘制英国趋势图
plt.plot(uk["Year"], uk["DALYs"], "b-", label="UK")
plt.xticks(rotation=90)  # 旋转x轴标签
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title("DALYs in the UK Over Time")
plt.legend()
plt.show()

# 比较中国和英国
china = dalys_data.loc[dalys_data["Entity"] == "China", ["Year", "DALYs"]]
plt.plot(china["Year"], china["DALYs"], "g-", label="China")
plt.plot(uk["Year"], uk["DALYs"], "b-", label="UK")
plt.legend()
plt.show()