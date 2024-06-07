def calc_distance():
    speed = float(input("Enter speed in Mph per hour: "))
    time = float(input("Enter time in hours: "))
    return f"You would travel {speed * time} Mph"

def calc_required_speed():
    distance = float(input("Enter distance in Miles: "))
    time = float(input("Enter time in hours: "))
    return f"You would need to average {distance/time} Mph"


print(calc_distance())
print(calc_required_speed())