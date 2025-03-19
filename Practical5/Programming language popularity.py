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
plt.title('Programming Language Popularity (February 2024)', fontsize=14)
plt.xlabel('Programming Languages', fontsize=12)
plt.ylabel('Percentage of Developers', fontsize=12)
plt.ylim(0, 70)  # Set y-axis limit for better visualization

# Add percentage labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height}%',
             ha='center', va='bottom')

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()  # Adjust layout to prevent label cutoff
plt.show()