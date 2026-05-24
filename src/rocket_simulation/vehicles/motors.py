from dataclasses import dataclass

@dataclass
class Motor:
    name: str
    mass: float
    thrust_duration: float
    average_thrust: float
    delay: float
    total_impulse: float