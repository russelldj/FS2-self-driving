import numpy as np
import matplotlib.pyplot as plt

#implement a very hacky controler which tries to hit a waypoints on each time step
WAYPOINTS_FILE = "waypoints.npy"
waypoints = np.load(WAYPOINTS_FILE)

location = waypoints[0, 0:2]
velocity = np.array([0.0, 0.0])
last_error = np.array([0.0, 0.0])
error_sum = np.array([0.0, 0.0]) 

NOISE_STRENGTH = 0.0

K_D = 0.6
K_I = 0.01 
K_P = 1 - K_D - K_I
assert K_P > 0

for row in waypoints[1:]:
    # recieve set point
    waypoint = row[:2]
    print(waypoint)
    
    #compute the error w.r.t to the set point
    error = waypoint - location
    error_sum += error
    error_delta = error - last_error
    noise = np.random.normal() * NOISE_STRENGTH
    velocity += (K_P * error + K_D * error_delta + K_I * error_sum)
    location += velocity
    #error = location - row[:2]

    #location += velocity
    x_way, y_way = row[:2] 
    plt.scatter(x_way, y_way, c='c')
    plt.scatter(location[0], location[1], c='b')
    plt.pause(0.05)

plt.show()


   

