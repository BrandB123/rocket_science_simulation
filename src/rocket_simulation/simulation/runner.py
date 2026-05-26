from src.rocket_simulation.simulation.launch import basic_flight_simulation, flight_simulation_step

def run_simulation(rocket, motor, state = None, metrics = None, type: str | None = None):
    print(
        f"""
        ---------------------------------------

                  FLIGHT SIMULATION:

        ---------------------------------------

                  ROCKET: {rocket.name}
                  MOTOR:  {motor.name}

        ---------------------------------------
        """
    )

    if (type == "basic"):
        basic_runner(rocket, motor)

    if (type == "ascent"):
        ascent_runner(rocket, motor, state, metrics)
    
def basic_runner(rocket, motor):
    try:    
        print("           RESULTS: ")
        basic_flight_simulation(rocket, motor)
        print(""" 
        --------------------------------------- 
            
            FLIGHT SIMULATION COMPLETED
            
        --------------------------------------- 
        """)
    except TypeError as e:
        print(f"Type Error: {e}")
    except ValueError as e:
        print(f"Value Error: {e}") 

def ascent_runner(rocket, motor, state, metrics):
    dt = 0.01
    state.mass = rocket.mass + motor.mass

    print("""|   TIME   |     ALTITUDE     | VELOCITY | ACCELERATION |   MASS    |
---------------------------------------------------------------------""")
    while True:
        flight_simulation_step(rocket, motor, state, metrics, dt)

        if state.velocity <= 0 and state.time > 0:
            break