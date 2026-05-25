# a module for kinematics-related calculations/equations

# Kinematics: a branch of dynamics that deals with aspects of motion apart from considerations of mass and force
#   - Kinematics is the "What" of motion. Related to states of motion
#   - Position, Velocity, Trajectory, etc are examples of this
#   - Answers questions like: "Where is the rocket?", "How fast is it moving?", "How high did it go?"

from src.rocket_simulation.physics.constants import GRAVITY

def burnout_velocity(initial_velocity: float, acceleration: float, time: float):

    if not isinstance(initial_velocity, (int, float)):
        raise TypeError("initial_velocity must be a number")
    
    if not isinstance(acceleration, (int, float)):
        raise TypeError("acceleration must be a number")
    
    if not isinstance(time, (int, float)):
        raise TypeError("time must be a number")

    return initial_velocity + acceleration * time

def current_altitude(initial_velocity: float, time: float, acceleration: float):

    if not isinstance(initial_velocity, (int, float)):
        raise TypeError("initial_velocity must be a number")
    
    if not isinstance(time, (int, float)):
        raise TypeError("time must be a number")
    
    if not isinstance(acceleration, (int, float)):
        raise TypeError("acceleration must be a number")
    
         
    return (initial_velocity * time) + (0.5 * acceleration * (time ** 2) )

def coast_gained_altitude(initial_velocity: float):
    
    if not isinstance(initial_velocity, (int, float)):
        raise TypeError("initial_velocity must be a number")
    
    return (initial_velocity ** 2) / (2 * GRAVITY)