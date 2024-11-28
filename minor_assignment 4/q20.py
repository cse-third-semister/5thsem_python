import statistics

# List of responses
responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 5]

# Frequency of each rating

print("Frequency of each rating:")
for i in range(1,6):
    print(f"Rating {i}: {responses.count(i)}")

# Response statistics
minimum = min(responses)
maximum = max(responses)
range_ = maximum - minimum
mean = statistics.mean(responses)
median = statistics.median(responses)
mode = statistics.mode(responses)
variance = statistics.variance(responses)
std_dev = statistics.stdev(responses)

# Display statistics
print("\nResponse Statistics:")
print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")
print(f"Range: {range_}")
print(f"Mean: {mean:.2f}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Variance: {variance:.2f}")
print(f"Standard Deviation: {std_dev:.2f}")