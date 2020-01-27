import numpy as np
import argparse
import config
import time
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import animation
from src.utils import create_random_flock

plt.style.use('seaborn-pastel')


def animate(_):
    flock.update_flock()
    scatter.set_offsets(np.array(
        [
            [boid.position[0] for boid in flock.Boids],
            [boid.position[1] for boid in flock.Boids]
        ]).T
    )
    time.sleep(1./config.FRAME_RATE)


parser = argparse.ArgumentParser()
parser.add_argument('--fps', type=int, default=15,
                    help="frames per second")
parser.add_argument('--frames', type=int, default=300,
                    help="number of frames")
parser.add_argument('--out_path', type=str, default='out.mp4',
                    help="path to output")

args = parser.parse_args()


flock, _, obstacles = create_random_flock(config.WIDTH,
                                          config.HEIGHT,
                                          config.N_boids,
                                          config.N_obstacles,
                                          config.R_obstacle)

# Prepare the scatter plot that has to be animated
fig = plt.figure()
ax = plt.axes(xlim=(0, config.WIDTH), ylim=(0, config.WIDTH))
ax.set_aspect('equal')
scatter = ax.scatter(
    [boid.position[0] for boid in flock.Boids],
    [boid.position[1] for boid in flock.Boids]
)

# Insert the obstacle outlines
for obstacle in obstacles:
    scatter.axes.add_artist(plt.Circle(obstacle.position, obstacle.radius, fill=False))

# Animate
anim = FuncAnimation(fig, animate, interval=1, frames=args.frames)

FFwriter = animation.FFMpegWriter(fps=args.fps)
anim.save(writer=FFwriter, filename=args.out_path)

plt.show()
