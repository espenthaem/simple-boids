import config
import numpy as np
from numpy.random import uniform
from src.boid import Boid
from src.flock import Flock
from src.obstacle import Obstacle


def check_obstacle(pos, obsts):
    # Check x-coordinate
    if not config.R_obstacle < pos[0] < config.WIDTH - config.R_obstacle:
        return False

    # Check y-coordinate
    elif not config.R_obstacle < pos[1] < config.HEIGHT - config.R_obstacle:
        return False

    # Check overlap with existing obstacles
    for obst in obsts:
        distance = np.linalg.norm(obst.position - pos)
        if distance < config.R_obstacle:
            return False

    return True


def create_random_flock(WIDTH, HEIGHT, N_boids, N_obstacles, R_obstacle):
    # Initialize the Boid Objects
    boids = [Boid(uniform(WIDTH), uniform(HEIGHT), uniform(-1, 1), uniform(-1, 1))
             for _ in range(N_boids)]

    # Initialize the Obstacle Objects
    obstacles = []
    for i in range(N_obstacles):
        position = np.array([uniform(WIDTH), uniform(HEIGHT)])

        # Check if new obstacle is valid
        while not check_obstacle(position, obstacles):
            position = np.array([uniform(WIDTH), uniform(HEIGHT)])

        obstacles.append(Obstacle(position, R_obstacle))

    # Create the Flock object
    flock = Flock(boids, WIDTH, HEIGHT, obstacles)

    return flock, boids, obstacles

