# a module for thrust related calculations/equations
# NOTE: might move this into dynamics in the future

from src.rocket_simulation.physics.constants import GRAVITY

def average_thrust( total_impulse: float, burn_time: float, avg_thrust: float | None = None) -> float:

    if avg_thrust is not None: 
        return avg_thrust
    
    if not isinstance(total_impulse, (int , float)):
        raise TypeError("total_impulse must be a number")    
    
    if not isinstance(burn_time, (int , float)):
        raise TypeError("total_impulse must be a number")    

    return total_impulse/burn_time

def simple_thrust_from_burn(avg_thrust: float, vehicle_mass: float):

    if not isinstance(avg_thrust, (int, float)):
        raise TypeError("avg_thrust must be a number")
    
    if not isinstance(vehicle_mass, (int, float)):
        raise TypeError("vehicle_mass must be a number")
    
    if vehicle_mass <= 0:
        raise ValueError("vehicle_mass must be greater than zero")
    
    weight  = vehicle_mass * GRAVITY
    
    return avg_thrust - weight

