import matplotlib.pyplot as plt
from collections import Counter

# List of responses
responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]

# Calculate frequencies and percentages
freq = Counter(responses)
total = len(responses)
percentages = {k: (v / total) * 100 for k, v in freq.items()}

# Plot the bar chart
plt.bar(freq.keys(), freq.values(), color='skyblue', label="Frequency")
plt.xticks(list(freq.keys()))
plt.xlabel("Response")
plt.ylabel("Frequency")
plt.title("Response Frequencies")

# Add percentages as labels
for k, v in freq.items():
    plt.text(k, v, f"{percentages[k]:.1f}%", ha='center', va='bottom')

plt.legend()
plt.show()
