# sourcery skip: for-index-underscore
from die import Die

# Creating a D6 die
die = Die()

# Making some rolls and adding the results to the list
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

print(results)
