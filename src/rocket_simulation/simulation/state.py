from dataclasses import dataclass

@dataclass
class FlightState:
    time: float = 0.00
    altitude: float = 0.00
    velocity: float = 0.00
    acceleration: float = 0.00
    mass: float = 0.00