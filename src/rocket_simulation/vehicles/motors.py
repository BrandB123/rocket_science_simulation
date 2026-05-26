from dataclasses import dataclass

@dataclass
class Motor:
    name: str
    mass: float
    thrust_duration: float
    average_thrust: float
    thrust_curve: list
    delay: float
    total_impulse: float
    def current_thrust(thrust_curve, time):
        for i in range(len(thrust_curve) - 1):
            time1, force1 = thrust_curve[i]
            time2, force2 = thrust_curve[i + 1]

            if time1 == time:
                return force1
            
            if time2 == time:
                return force2

            if time1 <= time <= time2:
                # linear interpolation
                return force1 + ((time - time1) / (time2 - time2)) * (force2 - force1)
            
            # before or after the curve
            if time < thrust_curve[0][0]:
                return 0

            return 0