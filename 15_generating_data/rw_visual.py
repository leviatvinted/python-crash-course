import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk(50000)
    rw.fill_walk()

    plt.style.use('dark_background')
    plt.figure(dpi=128, figsize=(10, 6))

    point_numbers = list(range(rw.num_points))

    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.cool,
                edgecolors='none', s=[i/1000 for i in point_numbers], alpha=0.5)
    
    # Emphasize the first and last points.
    plt.scatter(0, 0, c='green', edgecolors ='none', s=150, marker='*')
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
                s=150)
    
    # Remove the axes.
    plt.axis('off')

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
