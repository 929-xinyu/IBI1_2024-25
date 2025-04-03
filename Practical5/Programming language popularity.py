# Project Plan:
# 1. The purpose of this code is to create a bar plot showing the popularity of different programming languages among developers.
# 2. Use a dictionary to store the programming languages and popularity percentages.
# 3. Find the popularity percentage of Python and print it. In case no one uses Python, it will print "Language not found".
# 4. Create a bar plot by using plt and define it as "bars" to help me realize the "text" function.
# 5. Name the plot, the x-axis and y-axis.
# 6. Show the percentage on the top of each bar and language on the bottom of bars for better readability and use the "text" function to display
# 7. Output the bar plot.

# import necessary libraries
import matplotlib.pyplot as plt

# create the dictionary
language_popularity = {"JavaScript": 62.3,"HTML": 52.9,"Python": 51,"SQL": 51,"TypeScript": 38.5}
print(language_popularity) #show the dictionary
# find and print the percentage of "Python"
percentage = language_popularity.get("Python", "Language not found")
print(f"{percentage}% of developers use {"Python"}")

# create the bar plot
# I could have written it directly"plt.bar(language_popularity.keys(), language_popularity.values(), color='skyblue')", but I want to use "bars" that help me later to realize the "text" function.
bars=plt.bar(language_popularity.keys(), language_popularity.values(), color='skyblue')
# name bar, the x-axis and y-axis
plt.title('Programming Language Popularity (February 2024)')
plt.xlabel('Programming Languages')
plt.ylabel('Percentage of Developers')
# show x-axis labels and y-axis number for better readability. I want a better readability, so I use "text" to help me realize this and I learnt it by asking AI what should I use to show the percentage on the top of each bar and language on the bottom of bars.
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height, f'{height}%', ha='center', va='bottom')
# set the y-axis limit
plt.ylim(0, 70)
# show the plot
plt.show()