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

