# a module for dynamics-related calculations/equations

# Dynamics: a branch of mechanics that deals with forces and their relation primarily to the motion,
# but sometimes also to the equilibrium of bodies
#   - Dynamics is the "Why" of motion. What causes occur to bring about the changes in motion
#   - Forces (thrust, gravity, drag), Acceleration, Interactions
#   - Answers questions like: "Why is velocity changing?", "What forces are acting?", "What acceleration results?"


def acceleration_from_burn(thrust: float, vehicle_mass: float):

    if not isinstance(thrust, (int, float)):
        raise TypeError("thrust must be a number")
    
    if not isinstance(vehicle_mass, (int, float)):
        raise TypeError("vehicle_mass must be a number")

    return thrust / vehicle_mass

def drag(rho: float, velocity: float, Cd: float, area: float):
    # rho: air density
    # Cd: drag coefficient
    # area: Frontal Cross-Sectional Area

    if not isinstance(rho, (int, float)):
        raise TypeError("rho must be a number")
    
    if not isinstance(velocity, (int, float)):
        raise TypeError("velocity must be a number")
    
    if not isinstance(Cd, (int, float)):
        raise TypeError("Cd must be a number")
    
    if not isinstance(area, (int, float)):
        raise TypeError("area must be a number")

    return 0.5 * rho * (velocity ** 2) * Cd * area

def acceleration(force: float, mass: float):

    if not isinstance(force, (int, float)):
        raise TypeError("force must be a number")
    
    if not isinstance(mass, (int, float)):
        raise TypeError("mass must be a number")

    return force / mass

