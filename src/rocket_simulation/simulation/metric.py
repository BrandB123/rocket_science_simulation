from dataclasses import dataclass

@dataclass
class Metrics:
    # basic outputs
    apogee_m: float = 0.0
    apogee_ft: float = 0.0
    burnout_altitude_m: float = 0.0
    burnout_velocity_m_s: float = 0.0
    burn_time_s: float = 0.0

    # motor stats
    total_impulse_ns: float = 0.0
    average_thrust_n: float = 0.0
    max_thrust_n: float = 0.0

    # performance stats
    max_velocity_m_s: float = 0.0
    max_acceleration_m_s2: float = 0.0

    # misc
    reached_apogee: bool = False
    crash_velocity_m_s: float = 0.0
    flight_duration_s: float = 0.0

    # TODO: add max Q, dynamic pressure curve, terminal velocity

    # TODO: add a method to listen for given set of events based on the 
    # flight state object to set the above metrics at the time time