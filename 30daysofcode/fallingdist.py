def falling_distance(time):
    return f"The distance that the object has fallen in {time} seconds is {round(12 * 9.8 * time ** 2, 2)} metres."

[print(falling_distance(i)) for i in range(1, 11)]