from random import choice

import matplotlib.pyplot as plt  # v 1.19.2
import numpy as np  # v 3.3.2

def linear_function():
    # Select length of axes and the space between tick labels
    xmin, xmax, ymin, ymax = -5, 5, -5, 5
    ticks_frequency = 1

    # Enter x and y coordinates of points and colors
    xs = [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6]
    a = choice([-4, -3, -2, -1, -0.5, -0.25, 0.25, 0.5, 1, 2, 2.5, 3])
    b = choice([-4, -3, -2, -1, 1, 2, 3, 4])
    ys = []
    for argument in xs:
        ys.append(a * argument + b)
    # Plot points
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.plot(xs, ys)

    # Set identical scales for both axes
    ax.set(xlim=(xmin - 1, xmax + 1), ylim=(ymin - 1, ymax + 1), aspect='equal')

    # Set bottom and left spines as x and y axes of coordinate system
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Create 'x' and 'y' labels placed at the end of the axes
    ax.set_xlabel('x', size=14, labelpad=15)
    ax.set_ylabel('y', size=14, labelpad=15, rotation=0)
    ax.xaxis.set_label_coords(1.03, 0.49)
    ax.yaxis.set_label_coords(0.55, 1.02)

    # Create custom major ticks to determine position of tick labels
    x_ticks = np.arange(xmin, xmax + 1, ticks_frequency)
    x_ticks_major = x_ticks[x_ticks != 0]
    y_ticks = np.arange(ymin, ymax + 1, ticks_frequency)
    y_ticks_major = y_ticks[y_ticks != 0]
    ax.set_xticks(x_ticks_major)
    ax.set_yticks(y_ticks_major)

    # Create custom minor ticks to enable drawing of minor grid lines
    ax.set_xticks(np.arange(xmin, xmax + 1), minor=True)
    ax.set_yticks(np.arange(ymin, ymax + 1), minor=True)

    # Draw major and minor grid lines
    ax.grid(which='both', color='grey', linewidth=1, linestyle='-', alpha=0.2)

    # Draw arrows
    ax.plot(1, 0, linestyle='', marker='>', markersize=4, color='black',
            transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, linestyle='', marker='^', markersize=4, color='black',
            transform=ax.get_xaxis_transform(), clip_on=False)
    plt.savefig('linearFunction.png', transparent=True, bbox_inches='tight')
