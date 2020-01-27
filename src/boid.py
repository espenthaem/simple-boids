import numpy as np
import config


class Boid:
    def __init__(self, x, y, v_x, v_y):
        self.position = np.array([x, y])
        self.speed = np.array([v_x, v_y])
        self.acceleration = np.array([0.0, 0.0])

    def update(self, boids):
        self.position += self.speed

        self.speed += self.acceleration

        if np.linalg.norm(self.speed) > config.MAX_SPEED:
            self.speed = self.speed / np.linalg.norm(self.speed) * config.MAX_SPEED

        local_boids = []
        for boid in boids:
            if np.linalg.norm(self.position - boid.position) < config.PERCEPTION and boid.position is not self.position:
                local_boids.append(boid)

        if len(local_boids) > 0:
            self.separation(local_boids)
            self.align(local_boids)
            self.cohesion(local_boids)

    def avoid_collisions(self, obstacles):
        # Collision avoidance assumes non-overlapping obstacles
        see_ahead = self.position + (self.speed / np.linalg.norm(self.speed) * config.MAX_SEE_AHEAD)

        for obstacle in obstacles:
            obstacle_difference = obstacle.position - see_ahead

            if np.linalg.norm(obstacle_difference) < obstacle.radius:
                force = - obstacle_difference / np.linalg.norm(obstacle_difference) * config.AVOIDANCE_MAX_FORCE
                self.acceleration += force

    def align(self, local_boids):
        mean_v = np.array([local_boid.speed for local_boid in local_boids]).mean(axis=0)
        mean_v = mean_v / np.linalg.norm(mean_v) * config.MAX_SPEED

        force = mean_v - self.speed

        force = force / np.linalg.norm(force) * config.ALIGN_MAX_FORCE

        self.acceleration += force

    def cohesion(self, local_boids):
        center_mass = np.array([local_boid.position for local_boid in local_boids]).mean()
        difference = center_mass - self.position

        difference = difference / np.linalg.norm(difference) * config.MAX_SPEED

        force = difference - self.speed

        force = force / np.linalg.norm(force) * config.COHESION_MAX_FORCE

        self.acceleration += force

    def separation(self, local_boids):
        average_inverse_distance = np.array([(local_boid.position - self.position) /
                                             np.linalg.norm(self.position - local_boid.position)
                                             for local_boid in local_boids]).mean()

        force = average_inverse_distance - self.speed

        force = force / np.linalg.norm(force) * config.SEPARATION_MAX_FORCE

        self.acceleration += force

    def check_edges(self, width, height):
        if self.position[0] < 0:
            self.position[0] = width
        elif self.position[0] > width:
            self.position[0] = 0

        if self.position[1] < 0:
            self.position[1] = height
        elif self.position[1] > height:
            self.position[1] = 0

