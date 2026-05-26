from src.rocket_simulation.simulation.metric import Metrics
from src.rocket_simulation.simulation.runner import run_simulation
from src.rocket_simulation.simulation.state import FlightState

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

    state = FlightState()
    metrics = Metrics()

    simulation_type = "basic"

    # run_simulation(rocket, motor, simulation_type)
    run_simulation(rocket, motor, state, metrics)


    # implemnt function for flight results with drag and call it here
    #   for each time slice
    #       calculate drag ( drag = 1/2 * air density * drag coefficient * frontal cross-sectional area * velocity^2 )
    #       calculate forces at the current instant
    #       compute accelaration
    #       update velocity
    #       update altitude
    #       advance time
    #       repeat

main()