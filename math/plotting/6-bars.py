#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

# Define colors for each fruit
colors = ['red', 'yellow', '#ff8000', '#ffe5b4']
fruits = ['apples', 'bananas', 'oranges', 'peaches']
persons = ['Farrah', 'Fred', 'Felicia']

# Plotting the stacked bar graph
plt.figure()

for i in range(len(fruit)):
    plt.bar(persons, fruit[i], bottom=np.sum(fruit[:i], axis=0),
            color=colors[i], label=fruits[i], width=0.5)

# Add legend
plt.legend()

# Add labels and title
plt.xlabel('Person')
plt.ylabel('Quantity of Fruit')
plt.title('Number of Fruit per Person')

# Set y-axis range and ticks
plt.ylim(0, 80)
plt.yticks(np.arange(0, 81, 10))

# Show plot
plt.show()
