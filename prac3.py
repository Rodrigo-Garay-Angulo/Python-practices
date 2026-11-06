import math

def calculate_distance(p1, p2=(0,0)):
    distance = math.sqrt(pow((p2[0] - p1[0]), 2) + pow((p2[1] - p1[1]), 2))

    return round(distance, 2)

print(calculate_distance((3, 4), (2, 1)))