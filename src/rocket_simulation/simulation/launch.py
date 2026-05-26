# Flight Simulation Orchestration Functions

from src.rocket_simulation.physics.constants import FEET_PER_METER
from src.rocket_simulation.physics.dynamics import acceleration_from_burn
from src.rocket_simulation.physics.kinematics import burnout_velocity, current_altitude, coast_gained_altitude
from src.rocket_simulation.physics.thrust import average_thrust, simple_thrust_from_burn


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
    burnout_altitude = current_altitude(0, motor.thrust_duration, acceleration )
    print(f"            Altitude @ Burnout:        {burnout_altitude:.2f} m")

    #   altitude gained from coast (final velocity^2 = initial velocity^2 + (2 * acceleration * Δy ) )
    #       also represented as ( (-1 * initial velocity^2) / ( 2 * -9.8 ) )
    coast_phase_altitude = coast_gained_altitude(velocity_at_burnout)
    print(f"            Altitude from Coast Phase: {coast_phase_altitude:.2f} m")

    #   apogee in meters and feet ( altitude from burn + altitude from coast )
    apogee = burnout_altitude + coast_phase_altitude
    print(f"            Apogee:                    {apogee:.2f} m ({(apogee * FEET_PER_METER):.2f} ft)")


def flight_simulation_step(rocket, motor, flight_state, flight_metrics, dt):
    # calculate current thrust from motor
    # calculate drag
    # TODO: calculate weight
    # calculate current net thrust after weight and drag
    # calculate current acceleration
    # calculate current velocity
    # calculate current altitude
    return