from dataclasses import dataclass

@dataclass
class Rocket:
    name: str
    mass: float
    drag_coefficient: float
    tube_diameter_m: float