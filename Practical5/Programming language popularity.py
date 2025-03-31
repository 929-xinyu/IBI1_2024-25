# Import required libraries
import matplotlib.pyplot as plt

# Create the dictionary
language_popularity = {"JavaScript": 62.3,"HTML": 52.9,"Python": 51,"SQL": 51,"TypeScript": 38.5}

# Retrieve and print the percentage
percentage = language_popularity.get("Python", "Language not found")
print(f"{percentage}% of developers use {"Python"}")

# Create the bar plot
plt.figure(figsize=(10, 6))
bars = plt.bar(language_popularity.keys(), language_popularity.values(), color='skyblue')

# Customize the plot
plt.title('Programming Language Popularity (February 2024)')
plt.xlabel('Programming Languages')
plt.ylabel('Percentage of Developers')

# Add percentage labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height}%',
             ha='center', va='bottom')
# Show the plot
plt.show()