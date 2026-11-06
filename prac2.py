def filter_temps(temperatures, min_threshold):
    new_temps = []
    for temp in temperatures:
        if temp >= min_threshold:
            new_temps.append(temp)

    return sorted(new_temps)

temps = [15.5, 22.0, 17.8, 19.5, 25.0, 1.2]

print(filter_temps(temps, min_threshold=25.0))
