# Flight Simulation Orchestration Functions

from src.rocket_simulation.physics.constants import AIR_DENSITY_AT_SEA_LEVEL, FEET_PER_METER, GRAVITY
from src.rocket_simulation.physics.dynamics import acceleration, acceleration_from_burn, drag
from src.rocket_simulation.physics.kinematics import burnout_velocity, altitude, coast_gained_altitude, step_altitude, velocity
from src.rocket_simulation.physics.thrust import average_thrust, net_force, simple_thrust_from_burn

import math


# implement function for "gross" flight results and call it here
def basic_flight_simulation(rocket, motor):

    # average thrust (motor.average_thrust)
    avg_thrust = average_thrust(total_impulse=motor.total_impulse, burn_time=motor.thrust_duration)
    print(f"            Average Thrust:            {avg_thrust:.2f} N")
    
    #   thrust from burn (net thrust = avg thrust - mass * gravity)
    net_thrust = simple_thrust_from_burn(avg_thrust=avg_thrust, vehicle_mass=(rocket.mass + motor.mass))
    print(f"            Thrust from Burn Phase:    {net_thrust:.2f} N")

    #   acceleration from burn (a = net thrust / mass)
    acceleration = acceleration_from_burn(net_thrust, (rocket.mass + motor.mass))
    print(f"            Acceleration:             {acceleration:.2f} m/s²")

    #   velocity at burnout (final velocity = initial velocity + acceleration * time)
    velocity_at_burnout = burnout_velocity(0, acceleration, motor.thrust_duration)
    print(f"            Velocity @ Burnout:        {velocity_at_burnout:.2f} m/s")

    #   altitude at burnout (distance/altitude = (initial velocity * time) + (0.5 * acceleration * time^2 ) )
    burnout_altitude = altitude(0, motor.thrust_duration, acceleration )
    print(f"            Altitude @ Burnout:        {burnout_altitude:.2f} m")

    #   altitude gained from coast (final velocity^2 = initial velocity^2 + (2 * acceleration * Δy ) )
    #       also represented as ( (-1 * initial velocity^2) / ( 2 * -9.8 ) )
    coast_phase_altitude = coast_gained_altitude(velocity_at_burnout)
    print(f"            Altitude from Coast Phase: {coast_phase_altitude:.2f} m")

    #   apogee in meters and feet ( altitude from burn + altitude from coast )
    apogee = burnout_altitude + coast_phase_altitude
    print(f"            Apogee:                    {apogee:.2f} m ({(apogee * FEET_PER_METER):.2f} ft)")


def flight_simulation_step(rocket, motor, flight_state, flight_metrics, dt):
    
    # get current state 
    current_time = flight_state.time
    current_altitude = flight_state.altitude
    current_velocity = flight_state.velocity
    current_acceleration = flight_state.acceleration
    current_mass = flight_state.mass
    
    # calculate forces
    #TODO: use the motor class method
    thrust_force = 0
    
    if current_time < motor.thrust_duration:
        thrust_force = average_thrust(total_impulse=motor.total_impulse, burn_time=motor.thrust_duration)

    radius = rocket.tube_diameter_m / 2
    area = math.pi * radius ** 2

    drag_force = drag(AIR_DENSITY_AT_SEA_LEVEL, abs(current_velocity), rocket.drag_coefficient, area)

    # TODO: calculate weight dynamically
    weight_force = current_mass * GRAVITY

    # dynamics
    net_f = net_force(thrust_force, drag_force, weight_force)
    current_acceleration = acceleration(net_f, current_mass)

    # new state
    new_velocity = velocity(current_velocity, current_acceleration, dt)
    # TODO: move this into a function
    new_altitude = step_altitude(current_altitude, new_velocity, dt)

    # update state
    flight_state.time += dt
    flight_state.altitude = new_altitude
    flight_state.velocity = new_velocity
    flight_state.acceleration = current_acceleration
    # TODO: add something later to deduct mass due to propellant burn
    flight_state.mass = current_mass

    print(
        f"""|  {flight_state.time:.2f} s  | {flight_state.altitude:.2f} m ({flight_state.altitude * FEET_PER_METER:.2f} ft) | {flight_state.velocity:.2f} m/s |  {flight_state.acceleration:.2f} m/s²  |  {flight_state.mass:.2f} kg  |
---------------------------------------------------------------------""")

    # update metrics
    end_sim_condition = flight_state.velocity <= 0
    flight_metrics.update(end_sim_condition, flight_state) 

    return