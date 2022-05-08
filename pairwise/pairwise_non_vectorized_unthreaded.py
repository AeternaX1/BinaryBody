from subprocess import Popen
import numpy as np
import timeit
import math
import psutil
import cProfile
import time


"""
PAIRWISE N-BODY SIMULATION
NON-VECTORIZED

Force Calculation
This system will contain 100 objects, indexed by "i"
i = 1..100

"i" represents the number assigned to the object
This could be any number between 1 and 100

Every object has a:
mass (mᵢ)
    - Simple mass value for each object 

position (pᵢ = [xᵢ, yᵢ, zᵢ])
    - Calculate the position of all objects
    - The object's position will be it's x, y, and z axis]
    - Eg: For object 1's position in the simulation
    - p₁ = [x₁, y₁, z₁]

velocity (vᵢ = [vxᵢ, vyᵢ, vzᵢ])
    - Calculate the velocity of all objects
    - The object's total velocity will be it's velocity on it's x, y, and z axis
    - Eg: For object 1's total velocity in the simulation
    - v₁ = [vx₁, vy₁, vz₁]

Every object feels an gravitational attraction from every other body according to 
Newton's Law of Universal Gravitation - every object feels an acceleration
"""


def get_acceleration(position, mass, G, softening):

    # Give dimensions of the array
    # The array will represent the matrix
    N = position.shape[0]

    # Return an array of the given size, filled with zeroes
    acceleration = np.zeros((N,3))

    # Loop through 2D Array for every body
    for i in range(N): 
        for j in range(N):

            # Particle in question's x,y and z axis
            x = position[j,0] - position[i,0]
            y = position[j,1] - position[i,1]
            z = position[j,2] - position[i,2]

            # Inverse square law
            # Softening is the number added to avoid issues when two bodies are close to one another
            # If not added, the acceleration can go to infinity
            # inverse = (x**2 + y**2 + z**2 + softening**2)**(-1.5)
            inverse = math.pow(math.pow(x, 2) + math.pow(y, 2) + math.pow(z, 2) + math.pow(softening, 2), -1.5)

            acceleration[i,0] +=  G * (x * inverse) * mass[j]
            acceleration[i,1] +=  G * (y * inverse) * mass[j]
            acceleration[i,2] +=  G * (z * inverse) * mass[j]

    return acceleration


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
print("Unthreaded Pairwise Interaction")
print("********************************************************\n")

# Number of bodies
print("*****************")
print("Simulation bodies")
print("*****************")
print("Here, the number of bodies you wish to insert into the simulation can be determined.")
number_of_bodies = int(input("\nEnter the number of bodies: "))
# number_of_bodies = 100

# Number of timesteps
# Fixed amount of time by which the simulation advances/progresses.
print("\n\n*******************")
print("Timestep definition")
print("*******************")
print("This is the fixed amount of time by which the simulation advances")
number_of_timesteps = int(input("\nEnter the number of timesteps: "))
# number_of_timesteps = 100

# Timestep is the change in time between frames/simulation cycles (Delta time)
# Delta time describes the time difference between the previous frame that was drawn 
# and the current frame
timestep = 0.01   

# Softening length
softening = 0.1  

# Newton's Gravitational Constant
G = 6.67 / 1e11   

# Generate Initial Conditions; set the random number generator seed
np.random.seed(50)  

# Each body has a mass of 100
# This can be changed for different gravitational effects
mass = 100 * np.ones((number_of_bodies, 1)) / number_of_bodies  

# Determine positions and velocities at random
position = np.random.randn(number_of_bodies, 3)  
velocity = np.random.randn(number_of_bodies, 3)

# Convert to Center-of-Mass frame
velocity -= np.mean(mass * velocity,0) / np.mean(mass)

# Calculate initial gravitational accelerations
acceleration = get_acceleration(position, mass, G, softening)

print("\nSimulating body movements...")

# Simulation Main Loop
for i in range(number_of_timesteps):
    # Half timestep kick
    velocity += acceleration * timestep / 2.0

    # Full timestep drift
    position += velocity * timestep
    
    # Half timestep kick
    velocity += acceleration * timestep / 2.0

print("\nCalculations complete...")
print("\nPlease wait...")
print("\n")

# Time the get_acceleration() fucntion's execution time
result = timeit.timeit(lambda: get_acceleration(position, mass, G, softening), number=1)
print("The time taken to run the Pairwise Interaction simulation with", number_of_bodies, "bodies is: ")
print(result, "s")

# Record function calls
print("\n")
cProfile.run("get_acceleration(position, mass, G, softening)")

# System CPU usage
print("The overall system CPU usage is : ", psutil.cpu_percent())
input("Press ENTER to exit")
input()