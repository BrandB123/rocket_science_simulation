## Purpose
- Repository for model rocket flight simulation written in python.


## Libraries to Keep in Mind
- Numeric/Math
  - NumPy

- Plotting
  - Matplotlib

- Data Handling
  - Pandas

- Interpolation
  - SciPy

- Trajectory Simulation
  - RocketPy

## TODO
- Flight simulation for one rocket with one type of motor
  - ✅ Basic "gross" calculations
    - Log all the data as added to program
      - ✅ time
      - ✅ altitude
      - ✅ velocity
      - ✅ acceleration
      - ✅ thrust
      - drag
      - ✅ mass
      - dynamic pressure
      - NOTE: These logs can be easily transformed to graphs later
      - NOTE: This will make it easy to see:
        - ✅ burnout
        - drag buildup 
        - ✅ coast phase
        - max Q
        - Terminal Behavior
  - ✅ account for drag
  - account for changing mass of rocket during flight
  - account for thrust curve
  - account for changes in atmosphere
    - air density vs altitude
  - simulate parachute deployment and descent 
- Build in ability to easily change out rocket and motor settings
  - Add CLI selection for both based on rocket and motor configs
- Build out visual aspects of simulation instead of just logging data/results


## Potential File Structure
rocket_science_simulation/
│
├── pyproject.toml
├── README.md
├── .gitignore
│
├── src/
│   └── rocket_sim/
│       ├── __init__.py
│       ├── main.py
│       │
│       ├── physics/
│       │   ├── atmosphere.py
│       │   ├── drag.py
│       │   ├── gravity.py
│       │   └── thrust.py
│       │
│       ├── simulation/
│       │   ├── integrator.py
│       │   ├── flight.py
│       │   └── state.py
│       │
│       ├── vehicles/
│       │   ├── rocket.py
│       │   └── motors.py
│       │
│       ├── telemetry/
│       │   ├── logger.py
│       │   └── metrics.py
│       │
│       └── utils/
│           └── units.py
│
├── tests/
│
├── scripts/
│   └── run_simple_flight.py
│
└── data/
      └── motors/
