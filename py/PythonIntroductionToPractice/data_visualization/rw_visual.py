import matplotlib.pyplot as plt

from random_walk import RandomWalk

#if progame is active,it will be continuously simulate random walks
while True:
    #create an instance for RandomWalk, and draw its all points
    rw = RandomWalk(50000)
    rw.fill_walk()

    #set figure size
    plt.figure(dpi=128, figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    #highlighting the starting point and the ending point
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,edgecolor='none', s=1)

    #hidden coordinate axis
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n):")
    if keep_running == 'n':
        break