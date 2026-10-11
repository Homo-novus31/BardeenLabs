import numpy as np
import matplotlib.pyplot as plt

mass=1.0
g=9.81
e=0.8
gravtity = np.array([0.0,-g])
position = np.array([5.0,10.0])
velocity = np.array([0.0,0.0])
time=0.0
times = [time]
positions = [position.copy()]
threshold = 0.1
ppf = 100
while positions[1] > 0 or velocity[1] >threshold:
  t_hit = (velocity[1] + np.sqrt(velocity[1]**2 + 2*g
