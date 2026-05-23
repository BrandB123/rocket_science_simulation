## Purpose
- Repository for model rocket flight simulation written in python.

## TODO
- Flight simulation for one rocket with one type of motor
  - Basic "gross" calculations
    - Log all the data
      - time
      - altitude
      - velocity
      - acceleration
      - thrust
      - drag
      - mass
      - dynamic pressure
      - NOTE: These logs can be easily transformed to graphs later
      - NOTE: This will make it easy to see:
        - burnout
        - drag buildup 
        - coast phase
        - max Q
        - Terminal Behavior
  - account for drag
  - account for changing mass of rocket during flight
  - account for thrust curve
  - account for changes in atmosphere
    - air density vs altitude
  - simulate parachute deployment and descent 
- Build in ability to easily change out rocket and motor settings
- Build out visual aspects of simulation instead of just logging data/results

