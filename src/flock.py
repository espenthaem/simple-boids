import numpy as np


class Flock:
    def __init__(self, boids, width, height, obstacles=[]):
        self.Boids = boids
        self.width = width
        self.height = height
        self.obstacles = obstacles

    def update_flock(self):
        for Boid in self.Boids:
            Boid.check_edges(self.width, self.height)
            Boid.update(self.Boids)

            if self.obstacles:
                Boid.avoid_collisions(self.obstacles)

    def heatmap(self, resolution=(10, 10)):
        x_res = resolution[0]
        y_res = resolution[1]

        x_voxels = np.array([int(boid.position[0]/x_res) for boid in self.Boids])
        y_voxels = np.array([int(boid.position[1]/y_res) for boid in self.Boids])

        x_voxels[x_voxels > x_res - 1] = x_res - 1
        y_voxels[y_voxels > y_res - 1] = y_res - 1

        heatmap_array = np.zeros(resolution)
        heatmap_array[x_voxels, y_voxels] = 1

        return heatmap_array