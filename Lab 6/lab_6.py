# lab_6.py
#
# Author:
# Student ID:
#
# This library was written as part of Physics 102: Computational Laboratory
# in Physics, Fall 2014.

# import required libraries
import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Physical quantities
m = 1.0
l = 1.0
g = 9.8

# Exercise 1
def theta_1_dot(theta_1=0., theta_2=0., p_theta_1=0., p_theta_2=0.):
    """differential equation for the time derivative of theta_1
    Keyword Arguments
    =========
    theta_1: angle between first pendulum and vertical in radians
    theta_2: angle between second pendulum and vertical in radians
    p_theta_1: angular momentum of the first pendulum
    p_theta_2: angular momentum of the second pendulum
    
    Returns
    ======
    float: time derivative of theta_1
    """
    # start your code here
    
    return None

def theta_2_dot(theta_1=0., theta_2=0., p_theta_1=0., p_theta_2=0.):
    """differential equation for the time derivative of theta_2
    Keyword Arguments
    =========
    theta_1: angle between first pendulum and vertical in radians
    theta_2: angle between second pendulum and vertical in radians
    p_theta_1: angular momentum of the first pendulum
    p_theta_2: angular momentum of the second pendulum
    
    Returns
    ======
    float: time derivative of theta_2
    """
    # start your code here
    
    return None

def p_theta_1_dot(theta_1=0., theta_2=0., p_theta_1=0., p_theta_2=0.):
    """differential equation for the time derivative of p_theta_1
    Keyword Arguments
    =========
    theta_1: angle between first pendulum and vertical in radians
    theta_2: angle between second pendulum and vertical in radians
    p_theta_1: angular momentum of the first pendulum
    p_theta_2: angular momentum of the second pendulum
    
    Returns
    ======
    float: time derivative of p_theta_1
    """
    # start your code here
    
    return None

def p_theta_2_dot(theta_1=0., theta_2=0., p_theta_1=0., p_theta_2=0.):
    """differential equation for the time derivative of p_theta_2
    Keyword Arguments
    =========
    theta_1: angle between first pendulum and vertical in radians
    theta_2: angle between second pendulum and vertical in radians
    p_theta_1: angular momentum of the first pendulum
    p_theta_2: angular momentum of the second pendulum
    
    Returns
    ======
    float: time derivative of p_theta_2
    """
    # start your code here
    
    return None

# Exercise 2
def diff_system(variables, t):
    """system of differential equations for double pendulum
     Arguments
    =========
    variables: a list containing the current values of [theta_1, theta_2, p_theta_1, p_theta_2]
    t: the current time
    
    Returns
    ======
    list: time derivatives of [theta_1, theta_2, p_theta_1, p_theta_2]
    """
    # start your code here
    
    return None

# Exercise 3
def solve_system(theta_1, theta_2, total_time):
    """solves the system of differential equations
     Arguments
    =========
    theta_1: the initial condition for theta_1
    theta_2: the initial condition for theta_2
    total_time: total time for the solutions to run
    
    Returns
    ======
    (array, times): tuple containing the solutions array and the times array
    """
    # start your code here
    
    return None

# Animation helper code
def animate_sol(theta_1, theta_2, times):
    """makes an animation of a double pendulum
     Arguments
    =========
    theta_1: array containing the solutions for theta_1
    theta_2: array containing the solutions for theta_2
    times: array containing the times for the solutions
    
    Returns
    ======
    None
    """
    # start your code here
    
    # Convert angles into locations of the end of the first rod
    end_1_x = l * np.sin(theta_1)
    
    end_1_y = -l * np.cos(theta_1)
    
    # Convert angles into locations of the end of the second rod
    end_2_x = end_1_x + l * np.sin(theta_2)
    end_2_y = end_1_y - l * np.cos(theta_2)
    
    # Create the figure, axes, text, and plot objects
    fig = plt.figure()
    ax = fig.add_subplot(111, autoscale_on=False, xlim=(-2.5, 2.5), ylim=(-2.5, 1.5))
    ax.grid()
    ax.set_aspect('equal')
    time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

    line, = ax.plot([], [], lw=8)
    
    # Get the time step in milliseconds
    delta_t = 0.001*(times[1]-times[0])
    
    # Function to initialize the line and text data
    def init():
        line.set_data([], [])
        time_text.set_text('')
        return line, time_text
    
    # Function to update the line and text data
    def animate(i):
        thisx = [0, end_1_x[i], end_2_x[i]]
        thisy = [0, end_1_y[i], end_2_y[i]]        
        
        time_text.set_text('time = {0:0.2f}'.format(times[i]))

        line.set_data(thisx, thisy)
        return line, time_text

    # Create the animation
    ani = animation.FuncAnimation(fig, animate, np.arange(1, len(end_1_x)),
        interval=delta_t, blit=True, init_func=init)

    # Show the animation
    plt.show()

# Exercise 4
def make_animation(theta_1, theta_2, length):
    """makes an animation of a double pendulum
     Arguments
    =========
    theta_1: the initial condition for theta_1
    theta_2: the initial condition for theta_2
    length: total number of seconds for calculation
    
    Returns
    ======
    None
    """
    # start your code here
    
    return None
