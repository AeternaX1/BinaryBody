from copy import deepcopy
import numpy as np
import timeit
import psutil
import cProfile


"""
Barnes-Hut Algorithm
3 steps
1. Engineer a quadtree 
2. For each particle, traverse the quadtree to a sufficient depth. This gives you the center of masses to which you need to calculate distances, and so this step gives you the acceleration on each particle.
3. Numerically integrate using your algorithm of choice. (Velocity Verlet, Euler, whatever.)
"""


# Quadtree node constructor
# A class for a node within the quadtree.
# We use the terminology "subnode" for nodes in the next quadtree depth level
# If a node is "childless" then it represents a body
class node:
    def __init__(self, x, y, x_momentum, y_momentum, mass):
        """
        mass - Mass of node
        x - x-coordinate for centre of mass of node
        y - y-coordinate for centre of mass of noce
        x_momentum - x- coordinate of momentum, acceleration along x-coordinate
        y_momentum - y-coordinate of momentum, acceleration along y-coordinate
        pos - centre of mass array
        momentum - momentum array; array of momentums of all bodies. Momentum is a measurement of mass in motion
        subnode - child node
        side - side-length (depth=0 side=1)
        relative_position = relative position
        """
        self.mass = mass
        self.pos = np.array([x,y])
        self.momentum = np.array([x_momentum,y_momentum])
        self.subnode = None
    

    # Place node in next level quadrant and recalculates relative position
    def quadrant_division(self, i):
        self.relative_position[i] *= 2.0
        if self.relative_position[i] < 1.0:
            quadrant = 0
        else:
            quadrant = 1
            self.relative_position[i] -= 1.0
        return quadrant


    # Places node in next quadrant and returns quadrant number
    def quadrant_next_node(self):
        self.side = 0.5*self.side
        return self.quadrant_division(1) + 2*self.quadrant_division(0)
    

    # Repositions to the root depth quadrant
    # Goes back to full space / whole area
    def quadrant_reposition(self):
        self.side = 1.0
        self.relative_position = self.pos.copy()
        

    # Calculates distance between node and another node
    def node_distance(self, other):
        return np.linalg.norm(self.pos - other.pos)
    

    # Force applied from current node to other node
    # This is the center of mass of the entire cluster of bodies within the node
    def applied_force_current_node(self, other):
            d = self.node_distance(other)
            return (self.pos - other.pos) * (self.mass * other.mass / d**3)
        

# Adds body to a node of quadtree. 
# A minimum quadrant size is imposed to limit recursion depth
# IE: How much/how far the quadtree can recurse/call itself.
# If this is not implementation, a maximum recutrsion depth warning will appear
# Play with this by removing the "min_quad_size" variable
def add_body(body, node):
    # Assign body to node??
    new_node = body if node is None else None
    min_quad_size = 1.e-5
    if node is not None and node.side > min_quad_size:
        if node.subnode is None:
            new_node = deepcopy(node)
            new_node.subnode = [None for i in range(4)]
            quad = node.quadrant_next_node()
            new_node.subnode[quad] = node
        else:
            new_node = node

        new_node.mass += body.mass
        new_node.pos += body.pos
        quad = body.quadrant_next_node()
        new_node.subnode[quad] = add_body(body, new_node.subnode[quad])
    return new_node


def force_on(body, node, theta):
    if node.subnode is None:
        return node.applied_force_current_node(body)
    
    if node.side < node.node_distance(body) * theta:
        return node.applied_force_current_node(body)

    return sum(force_on(body, c, theta) for c in node.subnode if c is not None)


# Verlet algorithm
# More efficient method of calculating velocity
def verlet(bodies, root, theta, G, change_in_time):
    for body in bodies:
        force = G * force_on(body, root, theta)
        body.momentum += change_in_time * force
        body.pos += change_in_time * body.momentum / body.mass


# One simulation cycle
def model_step(bodies, theta, g, step):
    root = None
    for body in bodies:
        body.quadrant_reposition()
        root = add_body(body, root)
    verlet(bodies, root, theta, g, step)


# ********************************************************************************************

""" 
Simulation Parameters
"""
print("********************************************************")
print(" ____  _                        ____            _       ")
print("|  _ \(_)                      |  _ \          | |      ") 
print("| |_) |_ _ __   __ _ _ __ _   _| |_) | ___   __| |_   _ ")
print("|  _ <| | '_ \ / _` | '__| | | |  _ < / _ \ / _` | | | |")
print("| |_) | | | | | (_| | |  | |_| | |_) | (_) | (_| | |_| |")
print("|____/|_|_| |_|\__,_|_|   \__, |____/ \___/ \__,_|\__, |")
print("                           __/ |                   __/ |")
print("                          |___/                   |___/ ")
print("********************************************************\n")

print("********************************************************")
print("Barnes-Hut Quadtree")
print("********************************************************\n")

# Number of bodies
number_of_bodies = int(input("Enter the number of bodies: "))

# Theta parameter
# This determines what is considered short and long range
# We consider both the distance to the center of a quadtree cell and that cell’s width. 
# If the ratio width / distance falls below a chosen threshold, then
# we treat the quadtree cell as a source of long-range gravitational forces and use its center of mass. 
# Otherwise, we will recursively visit the child cells in the quadtree.
# 0.5 is commonly used in practice
theta = 0.5

# Newton'side Gravitational Constant
G = 6.67 / 1e11   

# Change in time between frames/simulation cycles (Delta time)
# Delta time describes the time difference between the previous frame that was drawn 
# and the current frame
change_in_time = 0.01

# Number of steps
number_of_timesteps = 100

# Random seed
np.random.seed(50)





# Initial Conditions

# BODY PROPERTIES TO BE INSERTED INTO THE ARRAY
# Bodies all have mass of 100, like in Pairwise Algorithm
# Keeps things fair
# Mass property of body, multiplied by number of bodies specified by user
mass = 100 * np.ones((number_of_bodies, 1)) / number_of_bodies  

# Random x coordinate, multiply random x cooridinates by number of bodies specified by user
X0 = np.random.random(number_of_bodies)

# Random y coordinate, multiply random x cooridinates by number of bodies specified by user  
Y0 = np.random.random(number_of_bodies)

# Random x momentum coordinate
PX0 = np.random.random(number_of_bodies) - 0.5

# Random y momentum coordinate
PY0 = np.random.random(number_of_bodies) - 0.5






# Create array of bodies
# An array of bodies which have a positional x,y coordinate, momentum x, coordinate, and mass
Bodies = [
    node(x0, y0, pX0, pY0, mass) 
    # Zip function used to iterate through a tuple; an unchangable ordered list
    # List of iterables which are collected into a tuple, and returned
    # This will be multiplied by the number of bodies, as specified when defining the properties of each body
    # COULD MAYBE JUST MULTIPLY THE ENTIRE TUPLE BY NUMBER OF BODIES, although may break script??
    for (x0, y0, pX0, pY0, mass) in zip(X0, Y0, PX0, PY0, mass)
]









# Main Model Loop for Barnes Hut
# Loop the function for one simulation cycle, for a number of iterations equal to the number of timesteps
def barnes_hut_simulation_loop(number_of_timesteps):
    for i in range(number_of_timesteps):
        model_step(Bodies, theta, G, change_in_time)


# Initialise
print("\nRunning...")

# Time the algorithm
result = timeit.timeit(lambda: barnes_hut_simulation_loop(number_of_timesteps), number=1)
print("The time taken to run the Barnes-Hut Algorithm simulation with", number_of_bodies, "bodies is:")
print(result, "s")

# Record function calls
cProfile.run("barnes_hut_simulation_loop(number_of_timesteps)")

# System CPU usage
print("The overall system CPU usage is : ", psutil.cpu_percent())
input("Press ENTER to exit")
