import numpy as np
import os
import matplotlib.pyplot as plt

def acc(x,y): #calculates the acceleration after dt time step based on the position from previous timestep
    ax = -x/(((x**2)+(y**2))**(3/2))
    ay = -y/(((x**2)+(y**2))**(3/2))
    #print(ax, ay)
    return ax, ay

def vel(t, dt, vx_o, vy_o, ax, ay): #calculates velocity after dt/2 half timestep based on calculated acceleration
    vx = vx_o+ax*(dt/2)
    vy = vy_o+ay*(dt/2)
    vx_o, vy_o = vx, vy
    #print(vx, vy)
    return vx, vy

def pos(t, dt, x, y, vx, vy): #calculates new position after dt timestep based on calculated velocity
    ox = x+vx*(dt)
    oy = y+vy*(dt)
    #print(ox, oy)
    return ox, oy

def calc(t, dt, x, y, vx_o, vy_o): #calculates the parameters sequencially
    ax, ay = acc(x, y)
    vx, vy = vel(t, dt, vx_o, vy_o, ax, ay)
    vx_o, vy_o = vx, vy
    x, y = pos(t, dt, x, y, vx, vy)
    t+=dt
    return t, vx, vy, ax, ay, x, y

'''x = 0.70
y = 0.0
vx = 0.0
vy = 1.0
t = 0.0
dt = 0.1'''

def run(n):
    # to find the text file from the same directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "param.txt")
    file_path2 = os.path.join(script_dir, f"orbitout{n}.txt")
    #data read from a file
    with open(file_path, "r") as f: #reads initial parameters off of a file
        t, dt, x, y, vx, vy = list(map(float, f.readline().split()))
    f.close()
    lx, ly = [], [] #to store the x and y positions at each timestep
    with open(file_path2, 'w') as g: #stores all the output parameters
        for _ in range(n): #number of iterations
            t, vx, vy, ax, ay, x, y = calc(t, dt, x, y, vx, vy) #nth iteration calculation and assignment
            lx.append(x)
            ly.append(y)
            print(f"after t={t} seconds, the parameters estimated: ", file=g)
            print(f"vertical velocity and acceleration: {vy} and {ay}", file=g)
            print(f"horizontal velocity and acceleration: {vx} and {ax}", file=g)
            print(f"current coordinate: x = {x}, y = {y}", file=g)
    g.close()
    return lx, ly

#plotting the trajectories
lx1, ly1 = run(10)
lx2, ly2 = run(25)
lx3, ly3 = run(50)
lx4, ly4 = run(100)
lx = [lx1, lx2, lx3, lx4]
ly = [ly1, ly2, ly3, ly4]


fig, axes = plt.subplots(2, 2, figsize=(10, 10))
axes = axes.ravel()
for i, (x, y) in enumerate(zip(lx, ly)):
    axes[i].plot(x, y, 'ro')
    axes[i].axis([-2*max(x), 2*max(x), -2*max(y), 2*max(y)])
    axes[i].set_xlabel(f'x position of planet')
    axes[i].set_ylabel(f'y position of planet')
    axes[i].set_title(f"Orbital trajectory after {len(x)} iterations", pad=-20)
plt.tight_layout(h_pad=5.0)
plt.show()

    
    
     
    
    
    
    
    
    
