## Simple, bare-bones Implementation of the Boids algorithm 

### Background
Object Oriented implementation of the [Boids](https://en.wikipedia.org/wiki/Boids) algorithm, including obstacle avoidance,  using as few dependencies as possible.

### Usage
The basic workflow is described in `main.py`. The implementation is centered around multiple objects. The physical behaviour of the individual Boids in contained in the `Boid` class, which are combined with the `Obstacle` objects in the `Flock` object. The `Flock` is used as an interface to perform the simulation. The parameters of the simulation are defined in `config.py`: 
```
# Simulation parameters
WIDTH = 150
HEIGHT = 150
N_boids = 15
N_obstacles = 1
R_obstacle = 25
# Boid behaviour parameters
MAX_SPEED = 2.5
ALIGN_MAX_FORCE = 0.5
COHESION_MAX_FORCE = 0.025
SEPARATION_MAX_FORCE = 0.025
AVOIDANCE_MAX_FORCE = 0.5
PERCEPTION = 5
MAX_SEE_AHEAD = 10
FRAME_RATE = 20
```


A random flock is generated based on these parameters. Using `matplotlib.FuncAnimation` the behaviour of the flock is displayed and saved to an `*.mp4` file, as demonstrated in `main.py`.

```
python main.py --frames 300 --fps 15 --out_path out.mp4
``` 

Yields the following simulation:

![Output sample](https://github.com/espenthaem/simple-boids/out.gif)