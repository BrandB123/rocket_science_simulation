from src.rocket_simulation.vehicles.motors import Motor
from src.rocket_simulation.vehicles.rockets import Rocket
import json
from pathlib import Path

rocket_path = Path("data/rockets/estes_amazon.json")
motor_path = Path("data/motors/estes_b6_4.json")


def main():
    with open(rocket_path) as f:
        rocket_data = json.load(f)

    with open(motor_path) as f:
        motor_data = json.load(f)

    rocket = Rocket(**rocket_data)
    motor = Motor(**motor_data)

    print(f"Rocket: {rocket.name}")
    
    print(f"Motor: {motor.name}")

main()