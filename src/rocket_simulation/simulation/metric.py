from dataclasses import asdict, dataclass
from src.rocket_simulation.physics.constants import FEET_PER_METER

@dataclass
class Metrics:
    # basic outputs
    apogee_m: float = 0.0
    apogee_ft: float = 0.0
    burnout_altitude_m: float = 0.0
    burnout_velocity_m_s: float = 0.0
    burnout_time_s: float = 0.0

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

    def update(self, end_sim_condition: bool, state):
        
        if not isinstance(end_sim_condition, bool):
            raise TypeError("end_sim_condition must be a boolean")
        
        if state.acceleration <= 0 and not self.burnout_time_s:
            self.burnout_altitude_m = state.altitude
            self.burnout_velocity_m_s = state.velocity
            self.burnout_time_s = state.time

        if state.velocity <= 0 and not self.reached_apogee:
            self.apogee_m = state.altitude
            self.apogee_ft = state.altitude * FEET_PER_METER
            self.reached_apogee = True

        if self.max_velocity_m_s < state.velocity:
            self.max_velocity_m_s = state.velocity
        
        if self.max_acceleration_m_s2 < state.acceleration:
            self.max_acceleration_m_s2 = state.acceleration

        if end_sim_condition:
            self.flight_duration_s = state.time
    
    def log(self):
        print("\nMETRICS:")

        print("\nBurnout:")
        print(f" - Altitude @ Burnout: {self.burnout_altitude_m:.2f} m")
        print(f" - Velocity @ Burnout: {self.burnout_velocity_m_s:.2f} m/s")
        print(f" - Time @ Burnout: {self.burnout_time_s:.2f} s")

        print("\nMaximums:")
        print(f" - Max Velocity: {self.max_velocity_m_s:.2f} m/s")
        print(f" - Max Acceleration: {self.max_acceleration_m_s2:.2f} m/s²")

        print(f"\nApogee: {self.apogee_m:.2f} m ({self.apogee_ft:.2f} ft)")
        print(f"Time: {self.flight_duration_s:.2f} s")

        

        
        