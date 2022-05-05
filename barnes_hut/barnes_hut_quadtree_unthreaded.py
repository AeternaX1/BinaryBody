from copy import deepcopy
import numpy as np
import matplotlib.pyplot as plt
import timeit
import threading
import math


"""
Barnes-Hut Algorithm

3 steps

1. Engineer a quadtree 
2. For each particle, traverse the quadtree to a sufficient depth. This gives you the center of masses to which you need to calculate distances, and so this step gives you the acceleration on each particle.
3. Numerically integrate using your algorithm of choice. (Velocity Verlet, Euler, whatever.)
"""

"""
A class for a node within the quadtree.

We use the terminology "child" for nodes in the next quadtree depth level
If a node is "childless" then it represents a body
"""

class node:
    # Quadtree node constructor
    def __init__(self, x, y, px, py, mass):
        """
        mass - Mass of node
        x - x-coordinate for centre of mass of node
        y - y-coordinate for centre of mass of noce
        px - x- coordinate of momentum, acceleration along x-coordinate
        py - y-coordinate of momentum, acceleration along y-coordinate
        pos - centre of mass array; array of center of masses for all bodies
        mom - momentum array; array of momentums of all bodies. Momentum is a measurement of mass in motion
        child - child node
        s - side-length (depth=0 s=1)
        relpos = relative position
        """
        self.mass = mass
        self.pos = np.array([x,y])
        self.mom = np.array([px,py])
        self.child = None
    
    def divide_quadrant(self, i):
        """
        Places node in next level quadrant and recomputes relative position
        """
        self.relpos[i] *= 2.0
        if self.relpos[i] < 1.0:
            quadrant = 0
        else:
            quadrant = 1
            self.relpos[i] -= 1.0
        return quadrant

    def next_quadrant(self):
        """
        Places node in next quadrant and returns quadrant number
        """
        self.s = 0.5*self.s
        return self.divide_quadrant(1) + 2*self.divide_quadrant(0)
    
    def reset_quadrant(self):
        """
        Repositions to the zeroth depth quadrant (full space)
        Goes back to full space / whole area
        """
        self.s = 1.0
        self.relpos = self.pos.copy()
        
        
    def node_distance(self, other):
        """
        Calculates distance between node and another node
        """
        return np.linalg.norm(self.pos - other.pos)
    
    def force_ap(self, other):
        """
        Force applied from current node to other
        """
        d = self.node_distance(other)
        return (self.pos - other.pos) * (self.mass * other.mass / d**3)
    

def add_body(body, node):
    """
    Adds body to a node of quadtree. A minimum quadrant size is imposed
    to limit the recursion depth.
    """
    new_node = body if node is None else None
    min_quad_size = 1.e-5
    if node is not None and node.s > min_quad_size:
        if node.child is None:
            new_node = deepcopy(node)
            new_node.child = [None for i in range(4)]
            quad = node.next_quadrant()
            new_node.child[quad] = node
        else:
            new_node = node

        new_node.mass += body.mass
        new_node.pos += body.pos
        quad = body.next_quadrant()
        new_node.child[quad] = add_body(body, new_node.child[quad])
    return new_node

def force_on(body, node, theta):
    if node.child is None:
        return node.force_ap(body)
    
    if node.s < node.node_distance(body) * theta:
        return node.force_ap(body)

    return sum(force_on(body, c, theta) for c in node.child if c is not None)

# Verlet algorithm
def verlet(bodies, root, theta, G, dt):
    for body in bodies:
        force = G * force_on(body, root, theta)
        body.mom += dt * force
        body.pos += dt * body.mom / body.mass

def model_step(bodies, theta, g, step):
    root = None
    for body in bodies:
        body.reset_quadrant()
        root = add_body(body, root)
    verlet(bodies, root, theta, g, step)


# ********************************************************************************************

""" 
Simulation Parameters
"""
print("*****************************************")
print("BinaryBody - Barnes-Hut Quadtree")
print("*****************************************")

# Number of bodies
number_of_bodies = int(input("Enter the number of bodies: "))
# number_of_bodies = 200

# Theta parameter
theta = 0.7

# Newton's Gravitational Constant
G = 6.67 / 1e11   

# Change in time / Delta time
dt = 0.01

# Number of steps
number_of_timesteps = 10

# Switch on for live plotting animation
live_plot = True   

# Random seed
np.random.seed(50)

# Initial Conditions
# mass = np.random.random(number_of_bodies) * 10

# Body mass of 100, like in Pairwise Algorithm
mass = 100 * np.ones((number_of_bodies, 1)) / number_of_bodies  
X0 = np.random.random(number_of_bodies)
Y0 = np.random.random(number_of_bodies)
PX0 = np.random.random(number_of_bodies) - 0.5
PY0 = np.random.random(number_of_bodies) - 0.5

# Initialize

# LIMIT TO JUST X and Y axis?
Bodies = [node(x0, y0, pX0, pY0, mass) for (x0, y0, pX0, pY0, mass) in zip(X0, Y0, PX0, PY0, mass)]


# Main Model Loop for Barnes Hut
def barnes_hut_simulation_loop(number_of_timesteps):
    for i in range(number_of_timesteps):
        model_step(Bodies, theta, G, dt)


# Time the algorithm
result = timeit.timeit(lambda: barnes_hut_simulation_loop(number_of_timesteps), number=1)
print("\nRunning...")
print("The time taken to run the Barnes-Hut Algorithm simulation with", number_of_bodies, "bodies is:")
print(result, "s")
input()

