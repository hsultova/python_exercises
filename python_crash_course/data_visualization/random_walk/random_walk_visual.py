import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    random_walk = RandomWalk(50000)
    random_walk.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
    point_numbers = range(random_walk.num_points)
    ax.scatter(random_walk.x_values, random_walk.y_values, c=point_numbers, cmap=plt.cm.Reds, edgecolors='none', s=2)
    ax.set_aspect('equal')

    # Emphasize the first and last points
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(random_walk.x_values[-1], random_walk.y_values[-1], c='blue', edgecolors='none', s=100)

     # Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break