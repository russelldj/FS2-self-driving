import dubins
import numpy as np
import matplotlib.pyplot as plt
import argparse 
import ast
from math import pi
# this example is modified from: https://pypi.org/project/dubins/ 

def dubins_section(q0, q1, turning_radius, step_size):
    path = dubins.shortest_path(q0, q1, turning_radius)
    configurations, _ = path.sample_many(step_size)
    configs = np.asarray(configurations)
    return configs

#parse the arguements
parser = argparse.ArgumentParser()
parser.add_argument('-p','--points', help='quoted comma-seprated tuples representing the waypoints as (x, y, theta in degrees). Like \"(0, 0, 0), (1, 1, 1)\"', type=str, required=False, default="(0, 0, 0), (1, 1, 1)")
parser.add_argument('-r','--radius', help='The minumum turning radius of the car', type=float, default=5, required=False)
parser.add_argument('-s','--step_size', help='The sampling rate for the final trajectory', type=float, default=0.5, required=False)
args = parser.parse_args()

#parse the points from the string representation
points = args.points
points = "[" + points + "]"
points = ast.literal_eval(points)

#Go through consequentive pairs of points
sections = []
for i in range(len(points) - 1): 
    q0 = (points[i][0], points[i][1], points[i][2] * pi / 180.0)
    q1 = (points[i+1][0], points[i+1][1], points[i+1][2] * pi / 180.0)
    sections.append(dubins_section(q0, q1, args.radius, args.step_size))

#Parse the path based on how many sections there are, yeilding a null path if there are zero
if len(sections) == 0:
    path = np.zeros((0, 3))
if len(sections) == 1:
    configs = sections[0] 
else:
    configs = np.concatenate(sections)

# plot the results
plt.scatter(configs[:,0], configs[:,1], label="trajectories")
plt.scatter([p[0] for p in points], [p[1] for p in points], c='r', label="waypoints")
plt.axis('equal')
plt.legend()
plt.show()
