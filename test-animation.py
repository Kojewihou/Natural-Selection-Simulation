import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frame_rate = 60  # Desired frame rate in frames per second
interval = 1000 / frame_rate  # Interval in milliseconds

# Define the Organism class


class Organism:
    def __init__(self, x, y, size, speed):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.direction = np.random.uniform(0, 2*np.pi)

    def move_randomly(self, max_step=0.1):
        self.x += self.speed * np.cos(self.direction)
        self.y += self.speed * np.sin(self.direction)

        # Reverse direction if out of bounds
        if self.x < 0 or self.x > 1:
            self.direction = np.pi - self.direction
        if self.y < 0 or self.y > 1:
            self.direction = -self.direction


# Create a figure and axis for the plot
fig, ax = plt.subplots()
ax.set_title(label="Simulation")
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

num_organisms = 1000
#TODO fill np.empty
organisms = [
    Organism(0.5, 0.5, np.random.uniform(2,10), np.random.uniform(0.01, 0.03))
    for _ in range(num_organisms)
]

# Create plot elements for the organisms with different sizes
#TODO vectorize
organism_plots = [
    ax.plot([], [], 'o', markersize=organism.size, color=np.random.rand(3,))[0] for organism in organisms
]

# Animation update function


def update(frame):
    for organism, organism_plot in zip(organisms, organism_plots):
        organism.move_randomly()
        organism_plot.set_data(organism.x, organism.y)
    return organism_plots


# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(
    0, 100), blit=True, interval=interval)

plt.show()
