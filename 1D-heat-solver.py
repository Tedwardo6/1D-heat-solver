import math
import numpy as np
import matplotlib.pyplot as plt


# initial_behav = math.sin(dx*t)
L = 20  #length 
dx = 1  # distance between x points
dt = 1 # time between steps 
alpha = 0.1 # diffusion constant
xi = 0
xf = L
ti = 0
tf = 60

K = int((xf - xi) / dx)
N = int((tf-ti) / dt)
u = [0] * K
u_next = [0] * K
u_left = [0] * K
u_right = [0] * K
x_i = [0] * K

color_test = (1, 0, 0)


a = (alpha*dt)/(dx**2)

# set initial condition
for i in range(xi, K, 1):
    u[i] = math.sin(dx * i)
for i in range(xi, K, 1):
    x_i[i] = dx * i

u_left = np.roll(u, 1)
u_right = np.roll(u, -1)

plt.plot(x_i,u, color='blue', label=f"t = {ti}")

# compare values
for j in range(0,N,1):
    for i in range(0, K, 1):
        diff_left = u[i] - u_left[i]
        diff_right = u[i] - u_right[i]
        # if diff is negative, neighbors have more heat, heat should flow into u, u[i] should increase based on the magnitude of their differences
        # u_left and u_right should decrease based on their contributions, but this should be done when u_left and right are treated as u
        surrounding = diff_left + diff_right
        u_next[i] = u[i] - (surrounding * a)
        #plt.plot(x_i,u, color = color_test)
        #color_test = (1,0,(i*(1/K)))
        print(j,i,max(u),min(u))
    u = u_next 
    u_next = [0] * K
    u_left = np.roll(u, 1)
    u_right = np.roll(u, -1)

plt.plot(x_i,u, color='red',label=f"t = {tf}")
plt.xlabel("x")
plt.ylabel("u")
plt.legend()
plt.show()