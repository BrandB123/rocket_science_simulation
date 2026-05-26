from src.rocket_simulation.simulation.launch import basic_flight_simulation

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

    if (type is "basic"):
        basic_runner(rocket, motor)
    
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

def dynamic_runner(rocket, motor, state, metrics):
    return