""" 
15-1. Cubes: 

A number raised to the third power is a cube. Plot the first five
cubic numbers, and then plot the first 5000 cubic numbers.

15-2. Colored Cubes: 

Apply a colormap to your cubes plot.
"""

import matplotlib.pyplot as plt

# x_values = list(range(1, 6))
x_values = list(range(1,5001))
y_values = [value**3 for value in x_values]

# plt.plot(x_values, y_values, linewidth=5)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.get_cmap('inferno'), 
    edgecolor='none', s=10)

# Set chart title and label axes.
plt.title("Cubic Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of the Value", fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=12)

# plt.savefig('cubes_plot.png', bbox_inches='tight')
plt.show()
